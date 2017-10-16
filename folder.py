import os
def rename_files():
    #Read the file names
    file_list = os.listdir(r"/Users/adishakti/Desktop/Portfolio/Python/prank")
    #print(file_list)
    #Change the file names
    print(os.getcwd())
    os.chdir(r"/Users/adishakti/Desktop/Portfolio/Python/prank")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
rename_files()
    
