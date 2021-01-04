# -*- coding: utf-8 -*-

from pmkssh import SSH
import json

ssh = SSH()

# Pega os dados para acesso no arquivo config.json
# O caminho completo dentro do container deve ser passado para o comando open abaixo
with open('/app/config.json','r') as fjson:
    data = json.load(fjson)

ssh.conn(data['conn']['host'],data['conn']['user'],data['conn']['passwd'])
output = ssh.exec_cmd("ls -l;hostname;date")
for i in output:
    print(i.rstrip('\n'))

# Para executar este script no container utilize o seguinte comando:
#
# docker run --rm -it -v "$PWD:/app" acarlos01/paramiko:tag python /app/example.py