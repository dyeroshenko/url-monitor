# URL Monitor

Url Monitor is a simple tool to check the HTTP status and configuration (host ip, round-trip-time, etc) of any URL! Supported statuses - [here](https://github.com/dyeroshenko/url-monitor/blob/5a463da138d77c488687b919d04621eac9f1e1b9/components/status.py#L9)

![image](https://raw.githubusercontent.com/dyeroshenko/url-monitor/master/screenshot.gif)


## Functionality and stack

Back-end:
 * Python3
 * Flask
 * SQLAlchemy

Front-end:
 * Vanilla JS, HTML & CSS 


  
Application uses these network services / libraries:
 * Socket
 * Requests 
 * Ping3 
 
to check the current status. 

## How to install (with Docker)

1. Clone or download repository
2. Use Dockerfile to build a docker-image on your machine:
```
docker build --tag [project_name] .
```
3. Run image in container: 
```
docker run -p 5000:5000 [project_name]
```
4. Run http://127.0.0.1:5000/ in your browser 

5. Enjoy! 
 
