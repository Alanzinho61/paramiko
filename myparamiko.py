import time
import paramiko


def connect(ipaddr,portno,usern,passwd):
    client=paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ipaddr,port=portno,username=usern,password=passwd)
    return client

def shell (client):
    ishell=client.invoke_shell()
    return  ishell

def send_command (ishell,command,t=1):
    ishell.send(command + "\n")
    time.sleep(t)

def send_command_list (ishell,commands):
    for i in commands:
        send_command(ishell,i)

def sen_from_file(ishell,file_name):
    with open(file_name,"r+")as f:
        commands=f.read().splitlines()
    for a in commands:
        send_command(ishell,a)


def get_result (ishell):
    result=ishell.recv(1000).decode()
    print(result)

def close(client):
    client.close()

if __name__=="__main__":
    router={"ipaddr":"10.1.1.10","portno":"22","usern":"muco","passwd":"1234"}
    connection=connect(**router)
    cikti=shell(connection)

    # commands = ['enable', '1234', 'conf t', 'username admin1 secret 1234', 'access-list 1 permit any', 'end',
    #             'terminal length 0', 'sh run | i user']
    # send_command_list(cikti,commands)
    sen_from_file(cikti,"commands.txt")
    get_result(cikti)