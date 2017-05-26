import os
def rename_files():


   #(1) get file names from a folder
   

    file_list = os.listdir(r"F:\Python_programming\prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current working Directory is "+saved_path)
    os.chdir(r"F:\Python_programming\prank")

    #(2) for each file, rename filename

    for file_name in file_list:
        os.rename(file_name, file_name.translate(str.maketrans('', '', '0123456789')))
    os.chdir(saved_path)
rename_files()
    
