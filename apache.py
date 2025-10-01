from sshConnection import SSHConnection

class ApacheMNG:

    def __init__(self, sshConnection):
        # Saving sshConnection into sshcon
        self.sshcon = sshConnection
        
        # Show menu
        self.menu()


        
    def menu(self):
        while True:
            print("#"*30)
            print("[1] Apache Status")
            print("[2] Apache Start")
            print("[3] Apache Stop")
            print("[4] Apache Restart")
            print("+"*30)
            print("[5] Exit")
            print("#"*30)
            print("")

            choice = input("Enter your choice (1-5): ")

            match choice:
                case "1":
                    self.apacheStatus()
                case "2":
                    print("Try starting apache")
                    self.apacheStart()
                case "3":
                    self.apacheStop()
                    print("apache stoped.")
                case "4":
                    self.apacheRestart()
                case "5":
                    break
                case _:
                    print("Invalid choice. You showld choice [1-5]")

    def apacheStatus(self):
        self.sshcon.executeCommands("systemctl status apache2")

    def apacheStart(self):
        self.sshcon.executeCommands("systemctl start apache2")

    def apacheStop(self):
        self.sshcon.executeCommands("systemctl stop apache2")
       
    def apacheRestart(self):
        self.sshcon.executeCommands("systemctl reload apache2")

    
        
