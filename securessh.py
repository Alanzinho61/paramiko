import paramiko
import getpass

passwd=getpass.getpass("sifregir")
connection=paramiko.SSHClient()
connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
connection.connect("10.1.1.10",22,"muco",passwd)
connection.close()