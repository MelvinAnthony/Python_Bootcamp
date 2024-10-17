file = open("pratice.txt","w+")
file.write("Hi melvin")
file.close()

file_2 = open("exercise.txt","w+")
file_2.write("And how are you")
file_2.close()

#Zip this two file

import zipfile

com_file = zipfile.ZipFile("Com_file","w")
com_file.write('pratice.txt',compress_type=zipfile.ZIP_DEFLATED)
com_file.write('exercise.txt',compress_type=zipfile.ZIP_DEFLATED)
com_file.close()

#unzip the file
zip_obj = zipfile.ZipFile("com_file","r")
zip_obj.extractall("content_extraction")

#using shutil also to zip used to pack file
import shutil

dir_to_zip = "C:\\Users\\melvi\\Desktop\\bot\\Advance_Python_Module"
output_file_name = "example"
shutil.make_archive(output_file_name,"zip",dir_to_zip)

#unpack the file
shutil.unpack_archive("example.zip","final_unzip","zip")
