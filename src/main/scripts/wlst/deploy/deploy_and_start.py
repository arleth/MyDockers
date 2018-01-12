# coding=utf-8
__author__ = 'Soren Arleth'
#if __name__ == '__main__':
#    from updateDeployment import deployment_artifact,deployment_target,staging_area

''' 'D:/TEMP/wlst/PortalEAR.ear' '''
def get_stage_location():
    return staging_area + '/'+deployment_artifact

print 'deploying....'

def main():
    print 'main test area'
    print 'Staging: '+get_stage_location()

if __name__ == '__main__':
    print __name__
    main()

def wlst_main():
    deploy(deployment_artifact, get_stage_location(), targets=deployment_target)
    startApplication(deployment_artifact)



if __name__ == "main":
    print __name__
    wlst_main()
