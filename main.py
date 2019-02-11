from shutil import copyfile
from sys import exit

source = input("Enter source file with full path: ")
target = input("Enter target file with full path: ")

# adding exception handling
try:
    copyfile(source, target)
except IOError as e:
    print("Unable to copy file. Error: " + e)
    exit(1)
except:
    print("Unexpected error: ", sys.exc_info())
    exit(1)

print("\nFile copy done!\n")

while True:
    print("Do you want to print the file ? (y/n): ")
    check = input()
    if check == 'n':
        break
    elif check == 'y':
        file = open(target, "r")
        print("\nFile contents:\n")
        print(file.read())
        file.close()
        print()
        break
    else:
        continue

print("hello")
