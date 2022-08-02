import paramiko
import time

connect=paramiko.SSHClient()
connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
connect.connect("10.1.1.10",22,"muco","1234")
shell=connect.invoke_shell()
shell.send("enable\n")
shell.send("1234\n")
shell.send("show users\n")
time.sleep(2)
result=shell.recv(1000).decode()
print(result)

with open("routerinfo.txt","w") as f:
    f.write(result)


connect.close()
