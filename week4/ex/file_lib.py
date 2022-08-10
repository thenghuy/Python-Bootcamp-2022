import os
class FileLib:
    def inspect(self):
        x=dir(FileLib)
        print(x)
    def currentpath(self):
      print(os.getcwd())
    def read_file(self,filename):
        file = open(filename, "r")
        print(file.read())
        file.close()
    def write_file(self,filename,content):
        file = open(filename, "w")
        file.write(content)
        file.close()
    def append_file(self,filename,content):
        file = open(filename, "a")
        file.write(content)
        file.close()
    def remove_file(self,filename):
        if os.path.exists(filename):
            os.remove(filename)
    def create_folder(self,foldername):
        os.mkdir(foldername)
    def remove_folder(self,foldername):
        os.rmdir(foldername)







