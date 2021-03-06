# -*- coding: utf-8 -*-

from paramiko import SSHClient
import paramiko

class SSH:
    def __init__(self):
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.__rcode = 0

    def conn(self,host,user,passw):
        try:
            self.ssh.connect(hostname=host,username=user,password=passw)
        except Exception:
            self.connected = False
        else:
            self.connected = True 

    def exec_cmd(self,cmd):
        if self.connected:
            stdin,stdout,stderr = self.ssh.exec_command(cmd)
            self.__rcode = stderr.channel.recv_exit_status()
            if self.__rcode != 0:
                return stderr
            else:
                return stdout

    @property
    def rc(self):
        return self.__rcode
