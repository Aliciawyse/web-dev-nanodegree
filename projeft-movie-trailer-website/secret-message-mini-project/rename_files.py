#rename a bunch of files on computer to reveal a secret message

import os
import re


def rename_files():
    #get files from folder
    file_list = os.listdir("C:\\Users\\abarrett\\Desktop\\prank\\prank\\")

    #ensure program is in correct directory
    saved_path = os.getcwd()

    #program is not in correct directory so we change it
    print("Current Working Directory is " +saved_path)
    os.chdir("C:\\Users\\abarrett\\Desktop\\prank\\prank\\")

    #update saved_path variable and double check that we are in right directory
    saved_path = os.getcwd()
    print("Current Working Directory is " +saved_path)

    #rename files devoid of numbers
    for file_name in file_list:
        output = re.sub('[0-9]+', '', file_name)
        os.rename(file_name, output)
        
    #os.chdir(saved_path)

rename_files()

    
    
