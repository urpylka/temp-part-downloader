#! /usr/bin/env bash

#
# deploy-ftp.sh – script for deploy filesync to linux services
# Copyright 2019 Artem B. Smirnov
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

cat <<EOF | sudo tee /lib/systemd/system/ftpserver.service > /dev/null
[Unit]
Description=FTP-server

[Service]
ExecStart=$(pwd)/src/ftp_server.py
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl enable ftpserver
sudo systemctl start ftpserver
