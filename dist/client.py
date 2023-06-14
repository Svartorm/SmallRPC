import xmlrpc.client

EXT = (".txt", ".md")

class colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    END = "\033[0m"

#% Create a proxy to connect to the server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

print(colors.GREEN + "Successfully connected to the server" + colors.END)
print(colors.YELLOW + "Welcome to SmallRPC" + colors.END)

#% Main loop
while True:
    try:
        #= Read the user input
        command = input("Enter command: ").split()

        #= Call the server function
        #$ Create function
        if command[0] == "create":
            if len(command) < 3:
                print(colors.RED + "Error: 'create' wrongful input.\nUsage: create <filename> <content>" + colors.END)
                continue
            if command[2].endswith(EXT):   #? If the content is a filename
                with open(command[2], "r") as f:
                    content = f.read()
            else:
                content = " ".join(command[2:])
            filename = command[1]
            proxy.create_file(filename, content)
            print(colors.GREEN + "File successfully created." + colors.END)

        #$ Read function
        elif command[0] == "read":
            if len(command) != 2:
                print(colors.RED + "Error: 'read' wrongful input.\nUsage: read <filename>" + colors.END)
                continue
            filename = command[1]
            content = proxy.read_file(filename)
            print(colors.YELLOW + ">>>>> File content:\n", content)
            print("<<<<< End of file content." + colors.END)

        #$ Update function
        elif command[0] == "update":
            if len(command) < 3:
                print(colors.RED + "Error: 'update' wrongful input.\nUsage: update <filename> <content>" + colors.END)
                continue
            if command[2].endswith(EXT):   #? If the content is a filename
                with open(command[2], "r") as f:
                    content = f.read()
            else:
                content = " ".join(command[2:])
            filename = command[1]
            proxy.update_file(filename, content)
            print(colors.GREEN + "File successfully updated." + colors.END)

        #$ Delete function
        elif command[0] == "delete":
            if len(command) != 2:
                print(colors.RED + "Error: 'delete' wrongful input.\nUsage: delete <filename>" + colors.END)
                continue
            filename = command[1]
            proxy.delete_file(filename)
            print(colors.GREEN + "File successfully deleted." + colors.END)

        #$ List function
        elif command[0] == "list":
            content = proxy.list_files()
            print(colors.YELLOW + ">>> List of files:")
            for filename in content:
                print("\t", filename)
            print("<<< End of list" + colors.END)
        
        #$ Exit function
        elif command[0] == "exit":
            break

    except xmlrpc.client.Fault as error:
        print(colors.RED + "RPC error:")
        print("\tFault code:", error.faultCode)
        print(error.faultString)
        print(colors.END)

    except ConnectionRefusedError:
        print(colors.RED + "Error connecting to the server." + colors.END)

#$ Closing the connection
print(colors.GREEN + "Connection closed." + colors.END)