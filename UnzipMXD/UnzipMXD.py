import os, zipfile

output_dir_name = 'C://Users//jcarey//Downloads'
import_dir_name = 'C://Users//jcarey//Documents//Unzip'
extension = ".zip"

 # change directory from working dir to dir with files
os.chdir(output_dir_name)
for item in os.listdir(output_dir_name): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        file_name = os.path.abspath(item) # get full path of files
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        os.chdir(import_dir_name) # change to import dir
        slice = len(output_dir_name) # get number of characters to delete from full path
        slice_number = slice-2 # remove '
        new_file_name = file_name[slice_number:-4] # set new folder name (without.zip)
        os.mkdir(new_file_name) # make new folder
        new_output_dir = import_dir_name + '//' + new_file_name # set destination for extract in new folder
        zip_ref.extractall(new_output_dir) # extract file to dir
        zip_ref.close() # close file
        os.remove(file_name) # delete zipped file
        os.chdir(output_dir_name) # change back to output dir for loop