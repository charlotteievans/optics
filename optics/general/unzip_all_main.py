from optics.general import fileutil

#Finds all the zipped files in a directory and unzips them to a destination directory

directory='C:\\DOCUMENTS\\Projects\\Gratings\\Data\\2016\\Sept 21\\Gphoto'
destination_directory='C:\\DOCUMENTS\\Projects\\Gratings\\Data\\2016\\Sept 21\\Gphoto\\TestedAgain'

#Don't change this
listedfiles= fileutil.listdir(directory)
only_zip= fileutil.list_only_zip_files(listedfiles)
for item in only_zip:
    fileutil.unzip_file(item, destination_directory)