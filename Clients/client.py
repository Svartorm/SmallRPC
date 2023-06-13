import xmlrpc.client

EXT = (".txt", ".md")

#% Create a proxy to connect to the server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

#% Main loop
while True:
    try:
        #= Read the user input
        command = input("Enter command: ").split()

        #= Call the server function
        #$ Create function
        if command[0] == "create":
            if len(command) < 3:
                print("Error: 'create' wrongful input.\nUsage: create <filename> <content>")
                continue
            if command[2].endswith(EXT):   #? If the content is a filename
                with open(command[2], "r") as f:
                    content = f.read()
            else:
                content = " ".join(command[2:])
            filename = command[1]
            proxy.create_file(filename, content)
            print("File successfully created.")

        #$ Read function
        elif command[0] == "read":
            if len(command) != 2:
                print("Error: 'read' wrongful input.\nUsage: read <filename>")
                continue
            filename = command[1]
            content = proxy.read_file(filename)
            print(">>>>> File content:\n", content)
            print("<<<<< End of file content.")

        #$ Update function
        elif command[0] == "update":
            if len(command) < 3:
                print("Error: 'update' wrongful input.\nUsage: update <filename> <content>")
                continue
            if command[2].endswith(EXT):   #? If the content is a filename
                with open(command[2], "r") as f:
                    content = f.read()
            else:
                content = " ".join(command[2:])
            filename = command[1]
            proxy.update_file(filename, content)
            print("File successfully updated.")

        #$ Delete function
        elif command[0] == "delete":
            if len(command) != 2:
                print("Error: 'delete' wrongful input.\nUsage: delete <filename>")
                continue
            filename = command[1]
            proxy.delete_file(filename)
            print("File successfully deleted.")

        #$ List function
        elif command[0] == "list":
            content = proxy.list_files()
            print(">>> List of files:")
            for filename in content:
                print("\t", filename)
            print("<<< End of list")
        
        #$ Exit function
        elif command[0] == "exit":
            break

    except xmlrpc.client.Fault as error:
        print("RPC error:", error)

    except ConnectionRefusedError:
        print("Error connecting to the server.")

#$ Closing the connection
print("Connection closed.")