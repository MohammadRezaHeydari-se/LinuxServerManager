from sshConnection import SSHConnection

class SystemCtlMNG:

    def __init__(self, sshConnection):
        # Saving sshConnection into sshcon
        self.sshcon = sshConnection
        
        # Show menu
        self.menu()


        
    def menu(self):
        while True:
            print("#"*50)
            print("[1] Show all active services")
            print("[2] Show all inactivat-Stop services")
            print("[3] Show all services (Active - Deactive)")
            print("+"*50)
            print("[4] Exit")
            print("#"*50)
            print("")

            choice = input("Enter your choice (1-5): ")

            match choice:
                case "1":
                    self.allActiveServices()
                case "2":
                    self.allDeactiveServices()
                case "3":
                    self.allServices()
                case "4":
                    break
                case _:
                    print("Invalid choice. You showld choice [1-4]")

    def allActiveServices(self):
        self.sshcon.executeCommands("systemctl list-units --type=service --state=running")

    def allDeactiveServices(self):
        self.sshcon.executeCommands("systemctl list-units --type=service --state=inactive")

    def allServices(self):
        self.sshcon.executeCommands("systemctl list-unit-files --type=service")

    
        
