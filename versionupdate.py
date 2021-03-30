import tkinter as tk
from tkinter import ttk
import json
import os
import sys

prefix = sys.argv[1]

os.chdir(f"./{prefix}")

packagefile = open('package.json','r')
data = json.load(packagefile)
packagefile.close()
# print(data)
currentVersion = data['version']
patchversion = int(currentVersion.split(".")[2])
minorversion = int(currentVersion.split(".")[1])
majorversion = int(currentVersion.split(".")[0])

def majorVersion():
    print("major")
    newVersion = f"{majorversion+1}.0.0"
    updateVersion(newVersion)
    quit()

def minorVersion():
    newVersion = f"{majorversion}.{minorversion+1}.0"
    updateVersion(newVersion)
    print("minor")
    quit()

def patchVersion():
    print("patch")
    newVersion = f"{majorversion}.{minorversion}.{patchversion+1}"
    updateVersion(newVersion)
    quit()

def noVersion():
    print("no change")
    quit()

def updateVersion(versionInput):
    packagefile = open('package.json','w')
    data['version'] = versionInput
    packagefile.write(json.dumps(data,indent=4))    
    packagefile.close()
    print(versionInput)
    quit()

root = tk.Tk()
root.title("Backend Version Update")
root.geometry("250x300")

desc = ttk.Label(root,text=f"{prefix.upper()}\nPlease select a version numbering update from the below options.\n\nIf it looks bad, please press cancel and go fix it manually",wraplength=150)

patchButton = ttk.Button(root,command=patchVersion,text=f"Patch: {currentVersion} -> {majorversion}.{minorversion}.{patchversion+1}")
minorButton = ttk.Button(root,command=minorVersion,text=f"Minor {currentVersion} -> {majorversion}.{minorversion+1}.0")
majorButton = ttk.Button(root,command=majorVersion,text=f"Major {currentVersion} -> {majorversion+1}.0.0")
noButton = ttk.Button(root,command=noVersion,text=f"No change {currentVersion}")

desc.pack(padx=10,pady=5)
majorButton.pack(padx=10,pady=5)
minorButton.pack(padx=10,pady=5)
patchButton.pack(padx=10,pady=5)
noButton.pack(padx=10,pady=20)

root.mainloop()

print("No selection was made, aborting.")
quit = 1/0