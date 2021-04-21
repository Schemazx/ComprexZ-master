import shutil
import os

def logo():
    print("  _____                                                    ______")
    print(" / ____|                                                  |___  /")
    print("| |        ___    _ __ ___    _ __    _ __    ___  __  __    / /")
    print("| |       / _ \  | '_ ` _ \  | '_ \  | '__|  / _ \ \ \/ /   / /")
    print("| |____  | (_) | | | | | | | | |_) | | |    |  __/  >  <   / /_")
    print(" \_____|  \___/  |_| |_| |_| | .__/  |_|     \___| /_/\_\ /_____|")
    print("                             | |")
    print("                             |_| Version 0.1 - Developed by Schema")
    print("\n")

logo()

_check = True


while (_check == True):
    type = str(input("Write the file type(zip, tar): "))
    name = str(input("Write the name of the "+type+": "))
    compress = str(input("Write the file you want to compress: "))
    if os.path.isfile(compress):
        shutil.make_archive(name,type,'./', compress)
        print("\nCompressed the file: "+compress+" in "+name+"."+type+", folder: "+os.getcwd()+"")
        delete = str(input("\nDo you want to delete the original file?: (y/n): "))
        if (delete == "y"):
            print("\nThe file "+compress+" was deleted")
            os.remove(compress)
            _check = False
        else:
            print("Thanks for using ComprexZ!")
            _check = False 
    else:
        print ("\nThe file "+compress+" does not exist!")
        _check = False

