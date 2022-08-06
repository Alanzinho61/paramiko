import paramiko
import time

connect=paramiko.SSHClient()
connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())

connect.connect(hostname="10.1.1.10",port=22,username="muco",password="1234")

with open("commands.txt","r+") as f:
    commands=f.read().splitlines()

shell=connect.invoke_shell()
for i in commands:
    shell.send(i+"\n")
    time.sleep(1)

result=shell.recv(1000).decode()
print(result)
connect.close()
