"""
in remote system we have to type

sudo netcat -l 999
and password of that system
output:
hi bangalore message is printed in remote system  

"""




#!user/bin/python
import telnetlib
import getpass
host="localhost"
#tn=telnetlib.Telnet(host,"999")


user = raw_input("Enter your remote account: ")
password = getpass.getpass()
tn=telnetlib.Telnet(host,"999")
tn = telnetlib.Telnet(host)

tn.read_until("login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("ls\n")
tn.write("exit\n")


#tn.write("hi bangalore\n")
print tn.read_all()

