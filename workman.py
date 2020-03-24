# workman 1.0.0 for python 3.0.0 +
#-------------------------------------------------------------------------
import sys
from time import *
import os
from zipfile import ZipFile

print("WORKMAN PACKAGE MANAGER FOR PYTHON")
print("----------------------------------")
print("version = version info")
print("creators = creator info")
print("forget = delete the entire manager (not packages)")
print("-------------------")
print("install: installs packages, on prompt type the EXACT PACKAGE NAME!")
print("uninstall: deletes the package ZIP")
print("-------------------")
print("config")

cli = input("workman>> ")

if cli == "version": # version number
  print("workman ver. 1.0.0 for python 3.0.0")
  
if cli == "creators": # creators!
  print("ProTechCEO, i think")
  
if cli == "forget": # deletes this manager
  forget = input("this will delete the manager, you can always reinstall. Continue? Y/N: ")
  
  if forget == "Y":
    print("bye bye, nice knowing you")
    sleep(2)
    os.remove("workman.py")
    print("workman has been deleted")
    
  if forget ==  "N":
    os.system("python3 workman.py")
    
# package management ----------------------------------------------------------

if cli == "install":
  install = input("install: ")
  
  os.system("wget https://workman-source.glitch.me/" + install + ".zip")
  print("decompressing " + install)
  sleep(2)
  with ZipFile(install + '.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()
  print("done. installed " + install + "successfully")
  
if cli == "uninstall":
  uninstall = input("uninstall: ")
  
  os.remove(uninstall + ".zip")
  
#----------------------------------------------------------------------------
# config

if cli == "config":
  os.system("clear")
  print("--------config----------")
  
  
#-----------------------------------------------------------------------------