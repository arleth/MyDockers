# coding=utf-8
__author__ = 'Soren Arleth'

import os

deployment_artifact = os.environ.get("APP_FILE","TestJEEApp.ear")
deployment_target = os.environ.get("DEPLOY_TARGET",'AdminServer')
staging_area = os.environ.get("STAGING_AREA","~/stage")
host_name = os.environ.get("HOST_NAME","localhost")
domain_name  = os.environ.get("DOMAIN_NAME", "base_domain")
admin_name  = os.environ.get("ADMIN_NAME", "AdminServer")
admin_username  = os.environ.get("ADMIN_USERNAME", "weblogic")
admin_pass  = os.environ.get("ADMIN_PASSWORD","manager1")
admin_port   = int(os.environ.get("ADMIN_PORT", "7001"))
domain_path  = '/u01/oracle/user_projects/domains/%s' % domain_name
production_mode = os.environ.get("PRODUCTION_MODE", "prod")

print('domain_name     : [%s]' % domain_name);
print('admin_port      : [%s]' % admin_port);
print('domain_path     : [%s]' % domain_path);
print('production_mode : [%s]' % production_mode);
print('admin password  : [%s]' % admin_pass);
print('admin name      : [%s]' % admin_name);
print('admin username  : [%s]' % admin_username);

execfile('connect.py')
execfile('stop_and_undeploy.py')
execfile('deploy_and_start.py')
execfile('disconnect.py')