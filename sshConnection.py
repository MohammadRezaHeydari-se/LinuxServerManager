import paramiko 
from getpass import getpass
from sessionLog import SessionLogger

# Class SSHConnectio is used for connecting to a linux base server and execute commands 
class SSHConnection:
    
    # Defining variabels
    #port = 22

    # SSHConnection constractor
    def __init__(self, serverIp: str, userName: str, password: str):
        self.serverIp = serverIp
        self.userName = userName
        self.password = password
        self.sessionLog = SessionLogger()

    # Connecting to server using SSH protocol and paramiko library 
    def connectionToSSH(self, port: int = 22):
        result = False # This result is using for successfull or not to a SSH connection

        self.paramikoClient = paramiko.SSHClient()
        self.paramikoClient.load_system_host_keys()
        self.paramikoClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.paramikoClient.connect(self.serverIp, port, self.userName, self.password)

        # Show this message if connection is sucsessful and if not it runs the exception and show error
        print(f"User: {self.userName} is connected to Server: {self.serverIp}")

    def connectingToSSHClose(self):
        try:
            self.paramikoClient.close()
            self.sessionLog.close()
        except Exception as ex:
            print(f"Connection cannot close: {ex}")
    
    # Running linux commands
    """
    def executeCommands(self, command):
        # Get the out put of commands ...
        stdin, stdout, stderr = self.paramikoClient.exec_command(command)
        result = stdout.read().decode()
        print(result)
        return result
    """
    def executeCommands(self, command) -> str:
        stdin, stdout, stderr = self.paramikoClient.exec_command(f"sudo -n {command}") # -n tells sudo not to prompt for a password; if a password is required, sudo will exit with an error.
        out = stdout.read().decode()
        err = stderr.read().decode()

        if "password" in err.lower(): # If sudo fails because a password is required, we can detect that and then prompt the user for the password.
            sudo_pass = getpass("Enter sudo password: ")
            stdin, stdout, stderr = self.paramikoClient.exec_command(f"sudo -S {command}") #-S makes sudo read the password from standard input (stdin), so we can send the password programmatically.
            stdin.write(sudo_pass + "\n")
            stdin.flush() # Run the command
            out = stdout.read().decode()
            err = stderr.read().decode()

        if out:
            print(out)
        if err:
            print(err)
        
        
        self.sessionLog.add(f"Output: {out} \n Error: {err}")


        return out + err
    
    def excecuteDirectCommand(self):
        while True:
            try:
                cmd = input(f" ${self.userName}@ {self.serverIp} > ")
                if cmd == "exit" : 
                    break
                else:
                    stdin, stdout, stderr = self.paramikoClient.exec_command(f"sudo -n {cmd}") # -n tells sudo not to prompt for a password; if a password is required, sudo will exit with an error.
                    out = stdout.read().decode()
                    err = stderr.read().decode()

                    if "password" in err.lower(): # If sudo fails because a password is required, we can detect that and then prompt the user for the password.
                        sudo_pass = getpass("Enter sudo password: ")
                        stdin, stdout, stderr = self.paramikoClient.exec_command(f"sudo -S {cmd}") #-S makes sudo read the password from standard input (stdin), so we can send the password programmatically.
                        stdin.write(sudo_pass + "\n")
                        stdin.flush() # Run the command
                        out = stdout.read().decode()
                        err = stderr.read().decode()

                    if out:
                        print(out)
                    if err:
                        print(err)
                    
                    
                    self.sessionLog.add(f"Output: {out} \n Error: {err}")
            except Exception as ex:
                print(f">> Command Error:{ex}")
