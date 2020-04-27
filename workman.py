# workman 1.0.0 for python 3.0.0 +
#-------------------------------------------------------------------------
import sys
from time import *
import os
from configparser import ConfigParser
from zipfile import ZipFile
import subprocess

config = ConfigParser()

print("WORKMAN PACKAGE MANAGER FOR PYTHON")
print("----------------------------------")
print("exit = exits manager")
print("version = version info")
print("creators = creator info")
print("forget = delete the entire manager (not packages)")
print("-------------------")
print("install: installs packages, on prompt type the EXACT PACKAGE NAME!")
print("uninstall: deletes the package")
print("quote: prints an all important quote")

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
    
if cli == "exit":
  sys.exit("exited, no problems found")
  
if cli == "config url":
  parser = ConfigParser()
  parser.read('workman.ini')

  url = input("new URL> ")
  config.set("workman_url", "url", url)
    
# package management ----------------------------------------------------------

if cli == "install": 
  install = input("install: ") # installation scripts
  
  os.system("wget https://workman-source.glitch.me/" + install + ".zip")
  print("decompressing " + install)
  sleep(2)
  with ZipFile(install + '.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()
  print("done. installed  " + install + "successfully")
  
if cli == "uninstall":
  uninstall = input("uninstall: ")  # uninstallation scripts
  os.system(uninstall + "/uninstall.py")

  # hmmm, what next?
  
if cli == "quote":
  print("a man with the questions is king, but a man with all the answers is god")
  print("Paddy Spooner- Quiz")