# Remote Linux Service Manager
This project is a tool for managing Linux services remotely (via SSH).
You can start/stop/restart services like **Apache2** and also view the status of all system services.



## Installation

### Linux / macOS
```bash
bash install.sh
source venv/bin/activate
python main.py


### Windows
install.bat
venv\Scripts\activate
python main.py


### Features
### Apache Management:
### Start
### Stop
### Restart
### Status

### Manage services with systemctl
### Execute commands directly on the server
### Save session log to JSON file

### Requirements
### Python 3.10 or higher
### Access to Linux server with SSH
### Paramiko library

### To run the program from the file:
### main.py
### Enter the server IP
### Provide the username and password
### From the program menu, select Apache Management or Services