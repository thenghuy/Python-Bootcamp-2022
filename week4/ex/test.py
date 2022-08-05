from file_lib import FileLib
FileLib().currentpath()
#FileLib().read_file("63_read_file.py")
FileLib().write_file("bc_test3.txt","Hello!world!")
FileLib().append_file("bc_test3.txt","Hello!world!")
FileLib().remove_file("bc_test3.txt")
#FileLib().remove_folder("hello")
FileLib().inspect()