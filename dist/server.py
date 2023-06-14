from xmlrpc.server import SimpleXMLRPCServer

class ResourceManager:
    """
    This class implements the server functions.

    The functions are:
    - create_file(filename, content)
    - read_file(filename)
    - update_file(filename, content)
    - delete_file(filename)
    - list_files()

    The functions create_file, read_file, update_file and delete_file
    receive a filename as a string and return True if the operation
    was successful. The function list_files receives no arguments and
    returns a list of strings with the names of the files stored in
    the server.
    """
    def __init__(self):
        self.files = {}

    def create_file(self, filename, content):
        self.files[filename] = content
        return True

    def read_file(self, filename):
        if filename in self.files:
            return self.files[filename]
        else:
            raise ValueError("File not found.")

    def update_file(self, filename, content):
        if filename in self.files:
            self.files[filename] = content
            return True
        else:
            raise ValueError("File not found.")

    def delete_file(self, filename):
        if filename in self.files:
            del self.files[filename]
            return True
        else:
            raise ValueError("File not found.")

    def list_files(self):
        return list(self.files.keys())

#% Create the server
server = SimpleXMLRPCServer(("localhost", 8000))
rm = ResourceManager()

#% Register functions
server.register_function(rm.create_file)
server.register_function(rm.read_file)
server.register_function(rm.update_file)
server.register_function(rm.delete_file)
server.register_function(rm.list_files)

#% Start the server
print("Server listening on port 8000...")
server.serve_forever()
