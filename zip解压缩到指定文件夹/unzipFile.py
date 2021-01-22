import zipfile
import shutil
import os


file = zipfile.ZipFile('temp\\temp.zip', 'r')
file.extractall('temp')
file.close()

all_list = os.listdir('temp')
for i in all_list:
    name, suffix = i.rsplit('.')
    if suffix == 'pdf':
        shutil.copyfile('temp\\' + name + '.pdf', 'file20201027\\4355445.pdf')
        os.remove('temp\\temp.zip')
        os.remove('temp\\' + name + '.pdf')



