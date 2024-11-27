#import os
import os
#define main function
def main():
    #make myfiles directory
    os.mkdir('MyFiles')
    #make docs subdirectory
    os.mkdir('MyFiles//Docs')
    #make images subdirectory
    os.mkdir('MyFiles//Images')
    #make videos subdirectory
    os.mkdir('MyFiles//Videos')
#call main function
main()