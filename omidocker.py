import os
import sys
import yaml
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f",'--file', dest='file_path', type=str, help='Add product_id')
parser.add_argument("build", help="build script from file path or .", type=str)

status = parser.add_subparsers(help="[name of service]", title="services", description="managment services", dest="service")
status_parser = status.add_parser(name="status", help="show status of a service")
start_parser = status.add_parser(name="start", help="start a service")
stop_parser = status.add_parser(name="stop", help="stop a service")
status_parser.add_argument("service_name", type=str, help="name of service")
start_parser.add_argument("service_name", type=str, help="name of service")
stop_parser.add_argument("service_name", type=str, help="name of service")

args = parser.parse_args()


def create_service(service_name:str, service_desc:str, workdir = "/", command="", restart=False):
    data = f'''
[Unit]
Description={service_name} - {service_desc}

[Service]
User=root
WorkingDirectory={workdir}
ExecStart=/bin/bash -c '{command}'
{"Restart=always" if restart else ""}
{"RestartSec=3" if restart else ""}

[Install]
WantedBy=multi-user.target
'''
    open(f"/etc/systemd/system/{service_name}.service","w").write(data)

    return True


def restart_service(service_name:str):
    os.system(f"systemctl stop {service_name}.service")
    os.system(f"systemctl daemon-reload")
    os.system(f"systemctl start {service_name}.service")

    return os.system(f"systemctl status {service_name}")


def build(args):
    with open(args.get("file_path") if args.get("file_path") is not None else "./omidocker.yml", "r") as f:
        yaml_content = f.read()

    yaml_data = yaml.safe_load_all(yaml_content)
    data = list(yaml_data)[0]

    service_name = data.get("service_name")
    service_desc = data.get("service_desc", service_name)
    workdir = data.get("workdir", "./")
    command = data.get("command").replace("\n","\\")
    restart = data.get("restart", False)

    if (service_name == None) or (command == None):
        raise "service_name and command is required."
    
    create_service(
        service_name=service_name,
        service_desc=service_desc,
        workdir=workdir,
        command=command,
        restart=restart
    )

    status = restart_service(service_name=service_name)

    print(f"Service: {service_name}\nLocation: {workdir}\n Status:\n",status)


def start_service(name):
    return os.system(f"systemctl start {name}.service")


def status_service(name):
    return os.system(f"systemctl status {name}.service")


def stop_service(name):
    return os.system(f"systemctl stop {name}.service")


if __name__ == "__main__":
    args = args.__dict__

    if (args.get("build") == "build"):
        build(args)
    elif (args.get("services") == "start"):
        start_service(args.get("service_name"))
    elif (args.get("services") == "status"):
        status_service(args.get("service_name"))
    elif (args.get("services") == "stop"):
        stop_service(args.get("service_name"))

    