from sshConnection import SSHConnection
from apache import ApacheMNG
from systemCtl import SystemCtlMNG
import getpass
import os
import sys
import platform

# Main run
if __name__ == "__main__":

    sys_plat = sys.platform
    if sys_plat.startswith("linux") or sys_plat.startswith("darwin"):
        os.system("clear")
    elif sys_plat.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")

    serverIp = input("Enter server IP: ")
    userName = input("Enter username: ")
    # password = input("Enter password: ") # Input will show the password in output
    # using getPass for unvisibel password
    password = getpass.getpass("Enter password \n[You can not see the password in putput]: ")

    # Connecting to ssh using username, password and server ip-address
    ssh = SSHConnection(serverIp, userName, password)
    ssh.connectionToSSH(22)

    # sessionLog = SessionLogger()
    ssh.sessionLog.add(f"User: {userName} is connected to {serverIp}")

    # Main menu
    while True:
        print("#" * 30)
        print("[1] Apache Management")
        print("[2] System CTL Management")
        print("+"*30)
        print("[3] Enter direct commands")
        print("+"*30)
        print("[4] Exit")
        print("#" * 30)
        print("")

        choice = input("Enter your choice (1-4): ")

        match choice:
            case "1":
                ApacheMNG(ssh)  # Passing connection to apache management class
            case "2":
                SystemCtlMNG(ssh)
            case "3":
                print("Enter direct command")
                ssh.excecuteDirectCommand()
            case "4":
                break
            case _:
                print("Invalid choice. You showld choice [1-4]")

    answer = input("If you want to save the log enter (y): ")
    if answer == "y":
        ssh.connectingToSSHClose()



