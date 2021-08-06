import pandas as pd
import os
import shutil

# Script to get a folder with all the .cif files of the crystals

df = pd.read_csv('./properties.csv')
xtals = df['name'].values
xtals.sort()

# Change this to where your directory of .cifs is located.
cif_dir = '../CURATED-COFs/cifs/'

# make the directory or delete and remake if exists.
if (os.path.isdir('./cifs')):
    shutil.rmtree('./cifs')
    os.mkdir('./cifs')
else:
    os.mkdir('./cifs')

missing = 0
for xtal in xtals:
    try:
        path = ''.join([cif_dir, xtal, '.cif'])
        shutil.copy(path, './cifs')
    except:
        missing += 1
        print(f'could not find {xtal}.cif in directory {path}')
    
print(f'{missing} missing files')
