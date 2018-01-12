# LICENSE UPL 1.0
#
# Copyright (c) 2018 Søren Arleth. All rights reserved.
#
FROM sarleth/wls12.2.1.3:latest

MAINTAINER Søren Arleth <soren@arleth.net>

ENV APP_FILE=TestJEEApp.ear STAGING_AREA=/tmp/stage ADMIN_PASSWORD=manager1

RUN mkdir /tmp/stage && chmod a+rwx /tmp/stage && mkdir /u01/deploy && chown oracle:oracle -R /u01/deploy && chmod a+wxr /u01/deploy

COPY wlst/deploy/$APP_FILE $STAGING_AREA
COPY wlst/deploy/*.py /u01/deploy/
COPY wlst/deploy/*.sh /u01/deploy/
USER root
RUN chmod a+xr /u01/deploy/updateDeployment.sh && chown oracle:oracle -R /u01/deploy/*.py  && chown oracle:oracle -R /u01/deploy/*.sh

USER oracle
# Define default command to start script.
ENTRYPOINT ["/u01/oracle/createAndStartEmptyDomain.sh"]
CMD ["/u01/deploy/updateDeployment.sh"]

