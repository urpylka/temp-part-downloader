#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:set ts=4 sw=4 et:

# Copyright 2018 Artem Smirnov

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from json_array import JsonArray
from source_flir_duo import FlirDuoCamera
from target_ftp import FTP
from logger import get_logger

import os.path, time
from threading import Thread, Event
from queue import Queue

def finder(number, args):
    db, source, search_interval, record, key, dq, logger = args
    logger.debug("Finder-" + str(number) + " was created.")
    """
    Function for searching files on remote device
    """
    while True:
        source.is_remote_available.wait()
        try:
            logger.debug("Finder-" + str(number) + ": Searching a new files in source...")
            my_list = source.get_list_of_files()
            if my_list != None:
                logger.debug("Finder-" + str(number) + ": List of source:\n" + str(my_list))
                for item in my_list:
                    if not db.in_records(key, item):
                        logger.info("Finder-" + str(number) + ": Found a new file: " + str(item))
                        # prepare the new object
                        record[key] = item
                        # save the new object
                        db.append(record.copy())
                        # add the new object to the upload queue
                        # индекс не сместится, потому что только finder добавляет в бд записи
                        # ТОЛЬКО ЕСЛИ COUNT OF FINDERs = 1
                        dq.put(db[len(db) - 1])
            else: logger.debug("Finder-" + str(number) + ": List of source is None")

        except Exception as ex:
            logger.error("Finder-" + str(number) + ": " + str(ex))

        time.sleep(search_interval)


def downloader(number, args):
    source, local_directory, dq, uq, logger = args
    logger.debug("Downloader-" + str(number) + " was created.")
    """
    Function for downloading files from remote device
    """
    while True:
        # объект из очереди передается по ссылке,
        # поэтому изменение record приведет к изменению record в JsonArray
        record = dq.get()
        source_path = record['source_path']
        local_path = local_directory + '/' + os.path.basename(os.path.dirname(source_path)).replace('-','') + '_' + os.path.basename(source_path).replace('_','')
        logger.debug("Downloader-" + str(number) + ": source_path " + source_path + " local_path " + local_path)
        while not record['downloaded']:
            try:
                source.is_remote_available.wait()
                if source.download(source_path, local_path):
                    record["downloaded"] = True
                    record["local_path"] = local_path
                    dq.task_done()
                    logger.info("Downloader-" + str(number) + ": File " + source_path + " was downloaded to " + local_path)
                    uq.put(record)
            except Exception as ex:
                # может быть ошибка что флешка на пиксе не доступна (ошибка 110 например)
                logger.error("Downloader-" + str(number) + ": " + str(ex) + " with file " + source_path)
                # закрыть поток на ftp "rosservice call /mavros/ftp/close NAME_OF_FILE" & сбросить ftp "rosservice call /mavros/ftp/reset"    
                time.sleep(2)
                # вообще, в случае этой ошибки можно перейти к другому элементу из очереди


def uploader(number, args):
    target, uq, logger = args
    verbose = True
    logger.debug("Uploader-" + str(number) + " was created.")
    while True:

        record = uq.get()
        local_path = record['local_path']
        target_path = '/' + os.path.basename(local_path)

        while not record['uploaded']:
            target.is_remote_available.wait()
            try:
                if target.upload(local_path, target_path):
                    record['uploaded'] = True
                    record['target_path'] = target_path
                    uq.task_done()
                    logger.info("Uploader-" + str(number) + ": File " + local_path + " was uploaded to " + target_path)
            except Exception as ex:
                logger.error("Uploader-" + str(number) + ": " + str(ex) + " with file " + local_path + " and target path " + target_path)
                time.sleep(2)


def create_threads(count, function, *args):
    for i in range(count):
        t = Thread(target = function, args = (i+1, args,))
        t.daemon = True
        t.start()


def main():

    logger = logger.get_logger("/home/pi/flir/filesync.log")

    db = JsonArray("/home/pi/flir/db.json", 5, logger)

    dq = Queue()
    uq = Queue()
    for record in db:
        if not record['downloaded']: dq.put(record)
        elif not record['uploaded']: uq.put(record)

    source = FlirDuoCamera("66F8-E5D9", ['JPG', 'png'], "/mnt", logger)
    target = FTP("192.168.0.41", "test-1", "passwd", logger)

    default_record = { "source_path": "", "downloaded": False, "local_path": "", "uploaded": False, "target_path": "" }
    name_of_key = "source_path"

    create_threads(1, finder, db, source, 10, default_record, name_of_key, dq, logger)
    create_threads(5, downloader, source, "/home/pi/flir", dq, uq, logger)
    create_threads(3, uploader, target, uq, logger)

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        return 0

if __name__ == '__main__':
    main()