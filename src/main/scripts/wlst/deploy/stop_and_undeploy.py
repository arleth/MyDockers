# coding=utf-8
__author__ = 'Soren Arleth'

print 'stopping and undeploying ....'

def wlst_main():
    stopApplication(deployment_artifact)
    undeploy(deployment_artifact)

if __name__ == "main":
    print __name__
    wlst_main()

def main():
    print 'main test area...'
    print 'Undedeploying: '+deployment_artifact

if __name__ == '__main__':
    print __name__
    main()