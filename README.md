# omidocker
a application service manager for linux servers same docker but simplify.

 in iran internet speed is a very slow and a large of resource get 403 error for development, so iranian developers cant use early docker on the vps on iran local. this package help to us for service managment easyly and faster on yout vps.

* [Getting start](#getting-start)
    * [Installing](#installing)
    * [Config for project](#config-for-project)
        * [Fields description](#fields-description)
        * [Examples](#full-example-of-omidockeryml)
* [Command Helper](#command-helper)

# Requirement:
* OS: linux based system ( in future available for mac )

# Getting start

## Installing
first you should get install.sh file from repository or etc resource and get execute access to this file.
- get file: `wget https://raw.githubusercontent.com/omidima/omidocker/main/install.sh`
- get executable access: `sudo chmod +x install.sh`
- run script: `./install.sh`

after run script run `omidocker -h` command on terminal and should can see output same this:
```
usage: omidocker.py [-h] [-f FILE_PATH] build {status,start,stop} 

...
```

now, enjoy it.

## Config for project
for usign this service creator tool, you should create a `omidocker.[yml|yaml]` file with this schema:
```yaml
service_name: <name of your service>
service_desc: <description of your service>
workdir: <root of your application source code>
command: <commands for install and rin your application>
restart: <boolean>
```

### Fields description:
- **service_name**: <required>
    every services in your system have a name for know system how od service and can managment your service.
- **command**: <required> like a CMD in dockerfile & commands in docker-compose
    for install script dependencies and execute script you sohuld fill this field.
    - examples:
        - run a command
            ```yaml
            ...
            command: uvicorn main:app --host 0.0.0.0 --port 8080 --workers 4

            ...
            ```
        - run more commands.
            ```yaml
            ...
            command: |
                source .venv/bin/activate
                pip install uvicorn
                pip install fastapi
                uvicorn main:app --host 0.0.0.0 --port 8080 --workers 4

            ...
            ```

- **service_desc**: <optional>
    description of your application service.
- **workdir**: <optional> like workdir in docker
    Specifies your application source code path and where command field execute.
- **restart**: <default: false>
    This field specifies whether the script should be restarted after stopping.
      If you set this field to "true" when the service is stopped, the service will be restarted automatically.

### full example of omidocker.yml
```yaml
service_name: fastapi application
service_desc: cerateed a test fatapi service
workdir: /home/omidima/application
command: |
    source .venv/bin/activate
    pip install uvicorn
    pip install fastapi
    uvicorn main:app --host 0.0.0.0 --port 8080 --workers 4
restart: true
```

# Command Helper
Usage: omidocker [command] [options...] ...

```
positional arguments:
  build                 build script from file path or .

services:
  managment services

    status              show status of a service
    start               start a service
    stop                stop a service

options:
  -h, --help            show this help message and exit
  -f FILE_PATH, --file FILE_PATH    omidocker file path
```

# Tasks:
- [x] Create linux script
- [ ] Create mac script
- [x] Config build option
- [x] Config start option
- [x] Config stop option
- [x] Config status option
- [ ] Create logger for services
- [ ] Create ls option for get services list
- [ ] other ...
