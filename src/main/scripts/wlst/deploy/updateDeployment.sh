#!/usr/bin/env bash

${DOMAIN_HOME}/bin/setDomainEnv.sh
wlst.sh /u01/deploy/updateDeployment.py

