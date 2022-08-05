import paramiko

connection=paramiko.SSHClient()
connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
router={"hostname":"10.1.1.10","port":"22","username":"muco","password":"1234"}
connection.connect(**router)
connection.close()
print("kapandi")