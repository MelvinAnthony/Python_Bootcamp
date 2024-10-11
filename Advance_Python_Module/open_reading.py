import os
import sys

#TO fing the correct directory
'''script_directory = os.path.dirname(os.path.abspath(sys.argv[0])) 
print(script_directory)

print(os.getcwd)'''

#Open the file and and write something 
'''
f = open("pratice.txt","w+")
f.write("Hi Melvin")
f.close()
'''
#To list out the what are the directory are pressent in my current usage location or we give some location to find the what are the directory are present.
#print(os.listdir("c:/Users/melvi/Desktop"))


# we have to move the file from different directory
import shutil
#shutil.move('pratice.txt',os.getcwd())

#print(os.listdir())

#remove the file or directory
import send2trash 
'''
print(os.listdir())

send2trash.send2trash("mytext.txt")
'''

