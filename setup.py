import os
import sys 
from shutil import copyfile


length = len(sys.argv)
if len(sys.argv) != 3:
    sys.exit("Usage: python $env:setuppath [ARGUMENT] [NAME]")


current = os.getcwd()

web = #Path to web directory
webext = #Path to web extension directory
webflask = #Path to web flask directory

print(length)

print(sys.argv[2])

# Path to new directory
path = os.path.join(current, sys.argv[2])

def goThrough(source_dir, target_dir):
    # Go through each item in the source directory
    for item in os.listdir(source_dir):

        source_item = os.path.join(source_dir, item)
        target_item = os.path.join(target_dir, item)
    
        # If the item is a file, copy it
        if os.path.isfile(source_item):
            # Note to self: this created a new file if there's no file there
            copyfile(source_item, target_item)
            print(f"Copied file: {source_item} to {target_item}")
        
        # If the item is a directory, create it and copy its contents recursively
        elif os.path.isdir(source_item):
            # Make new directory at targeted location
            os.makedirs(target_item, exist_ok=True)
            print(f"Created directory: {target_item}")
            # Recursive call to copy contents of the directory
            goThrough(source_item, target_item)


def setup():
    directory = sys.argv[1]

    match directory:
        case "web":
            os.makedirs(path, exist_ok=True)
            goThrough(web, path)
            print("Created web directory and copied files and directories")

        case 'webext':
            os.makedirs(path, exist_ok=True)
            goThrough(webext, path)
            print("Created web extension directory and copied files and directories")

        case 'webflask':
            os.makedirs(path, exist_ok=True)
            goThrough(webflask, path)
            print("Created web flask directory and copied files and directories")


setup()


