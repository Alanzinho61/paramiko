import paramiko
import time
connect=paramiko.SSHClient()
connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())

connect.connect(hostname="10.1.1.10",port=22,username="muco",password="1234")

commands=['enable\n', '1234\n', 'conf t\n', 'username admin1 secret cisco\n', 'access-list 1 permit any\n', 'end\n', 'terminal length 0\n', 'sh run | i user\n']

shell=connect.invoke_shell()
for i in commands:
    shell.send(i)
    time.sleep(1)

result=shell.recv(1000).decode()
print(result)
connect.close()
