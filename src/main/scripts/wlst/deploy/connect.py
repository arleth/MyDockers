# coding=utf-8
__author__ = 'Soren Arleth'
#if __name__ == '__main__':
#    from updateDeployment import admin_username,admin_port,admin_name,admin_pass,domain_name,host_name

print 'connecting to admin server....'

def getconnect_string():
    return "t3://"+host_name+":"+str(admin_port)

def wlst_main():
    connect(admin_username, admin_pass, getconnect_string() , adminServerName=admin_name)

def main():
    print 'main test area'
    print "host connect string is: "+str(getconnect_string())

if __name__ == '__main__':
    print __name__
    main()

if __name__ == "main":
    print __name__
    wlst_main()
