import shutil, os
from pathlib import Path
def Clean_IRC_Search():
    #Prompt user for path to folder containing IRC search files
    file_name = input('Enter path to IRC downloads folder:\n')
    #Default path for mIRC client is 'C:\Users\loacal_user_name\AppData\Roaming\mIRC\downloads' 
    folder = Path(file_name)
    #Check if directory exists
    if folder.exists() and folder.is_dir():
        #Confirm removal
        confirm = input('Okay to delete all Searchbot files in folder? (y/n) ')
        if confirm.lower() == 'y':
            #Select all files where name begins with Search
            for file in folder.glob('Search*'):
                file.unlink() #deletes file
                print(f'Deleted: {file}')
            print('All SearchBot and SearchOok files deleted')
        else:
            print('Delete canceled.')
    else:('The path you entered does not exist or is not a folder')

if __name__== '__main__':
    Clean_IRC_Search()

