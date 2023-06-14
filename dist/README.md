# SmallRPC
A simple Remote File Management System using RPC implemented in Python

## Requirements:
1. Python 3.6 or above
2. Python libraries: xmlrpc
## Usage:
1. Extract the contents of the zip file located in `dist/SmallRPC.zip`
1. Start the server by running the command: `python server.py`
2. Run the client application by executing the command: `python client.py`
3. The client will interact with the server using RPC to perform file management operations.
4. The server runs on port 8000 by default. Make sure the port is not being used by any other application.
5. The client can be run on any machine in the same network as the server. The client needs to know the IP address of the server to connect to it. The IP address of the server can be changed in the client.py file.
## Features:
1. Starting the client application will connect to the server automatically: 
![Client](docs/img/launch.png)
2. The client can perform the following operations on the server:
    1. **Create a file:**</br>
Creating from text : 
Just writting text after the command will create a file with the text as content for the file:
![Create](docs/img/create.png)
Creating from a file :
Writting a file name with a supported extension ('.txt', '.md') after the command will create a file with the content of the file:
![Create](docs/img/createfromfiletxt.png)
![Create](docs/img/createmd.png)
    1. Read a file :</br>
This command will read the content of the file and display it on the console:
![Read](docs/img/read.png)
    2. Write to a file :</br>
The update command will update the content of the file with the text or file provided:
![Update](docs/img/update.png)
    3. Delete a file :</br>
![Delete](docs/img/delete.png)
    4. List all files in the server :</br>
![List](docs/img/list_empty.png)
    5. Exit the client :</br>
![Exit](docs/img/exit.png)

## More Information:
 - If you have question, open an issue on this repository or contact me at: [svartorm@proton.ne](mailto:svartorm@proton.me)
 - Contribution are welcome. Feel free to open a pull request.

