# Скрипт для перезагрузки ПК с Linux через SSH
# На ПК с Linux должны быть установлены модули pip и paramiko

# --Установка модулей на примере AltLinux--
# apt-get install python3-module-pip
# python3 -m pip install --upgrade pip --proxy
# pip3 install paramiko


#!/usr/bin/python3
import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('HOSTNAME or IP-address', username='NAME', password='*******')
client.exec_command('sudo reboot')