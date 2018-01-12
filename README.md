#### All kinds of scripts in order to prepare for Docker images

https://blogs.oracle.com/jamesbayer/automate-wls-console-tasks-with-wlst


docker build -t sarleth/mywlsapp:latest .

docker run -i -t --name mywlsrun1 sarleth/mywlsapp /bin/bash

### clean up
docker ps -a
docker rm mywlsrun1
docker rmi sarleth/mywlsapp


