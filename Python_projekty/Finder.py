import os
import re
import win32api

def najdi_subor(root_folder, rex):
    for root,dirs,files in os.walk(root_folder):
        for f in files:
            result = rex.search(f)
            if result:
                print('-', os.path.join(root, f))
                break 

def najdi_subor_vsade(file_name):
    rex = re.compile(file_name)
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        najdi_subor( drive, rex )
print('========================================')
hladaj = input('Zadajte názov súboru: ')
print('========================================')
najdi_subor_vsade(hladaj)
print('========================================')
print('Dokončené')
input('Stačte ENTER pre ukončenie')