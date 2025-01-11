"""
Try and except blocks
Let's use the navigator example to create code that opens configuration files for the Mars mission. 
Configuration files can have all kinds of problems, so it's critical to report problems accurately when they come up. We know that if a file or directory doesn't exist, FileNotFoundError is raised. 
If we want to handle that exception, we can do that with a try and except block
"""
try:
     open('config.txt')
except FileNotFoundError:
     print("Couldn't find the config.txt file!")
print("***********")
def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")


if __name__ == '__main__':
    main()
" With the previous code you will get a PERMISSION DENIED error, because the file does not exist and CONFIG.TXT is a DIRECTORY"


