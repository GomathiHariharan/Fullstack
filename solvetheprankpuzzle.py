import os

def renamefiles():
    filelist = os.listdir(r"C:\OOP\prank")
    print(filelist)
    os.chdir(r"C:\OOP\prank")
    for filename in filelist:
        print("oldfilename:",filename)
        os.rename(filename, filename.translate(str.maketrans(' ',' ','0123456789')))
        '''os.rename(filename,filename[3:]'''

    newfilelist = os.listdir(r"C:\OOP\prank")
    print(newfilelist)
    os.chdir(r"C:\OOP\prank")
    for filename in newfilelist:
        print("newfilename:",filename)
           
renamefiles()
