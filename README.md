# timeserviceapp
Study app for docker-compose learning.
Project directories:
-  **timeserviceapp**: source code
- **timeserviceapp-compose**: docker-compose file and haproxy config

To start service with compose:
```bash
cd ./timeserviceapp-compose
sudo docker-compose up
```
This command will start 4 containers: 3 instances of timeservice app and 1 instance of haproxy. 
Running service will be avaialable at `http://docker_host_ip/get-time`
HAproxy stats will be available at `http://docker_host_ip:9000/haproxy_stats`