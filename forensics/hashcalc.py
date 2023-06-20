import hashlib
import sys


args = sys.argv[1:]

if (len(args)==0):
    print ("""usage : 
              hashcalc.py file - to get file hash
              hashcalc.py file1 file2 - to compare files 
              """)

elif (len(args)==1):
    file = args[0]
    filehash = hashlib.sha256(open(file, "rb").read()).hexdigest()
    print (f"SHA256 HASH  : {filehash}")

elif (len(args)==2):
    file1 = args[0]
    file2 = args[1]
    file1hash =  hashlib.sha256(open(file1, "rb").read()).hexdigest()
    file2hash =  hashlib.sha256(open(file2, "rb").read()).hexdigest()
    if(file1hash == file2hash):
        print(f"file {file1} hash : {file1hash}")
        print(f"file {file2} hash : {file2hash}")
        print(" [!] Hash verfied")
    else:
        print(f"file {file1} hash : {file1hash}")
        print(f"file {file2} hash : {file2hash}")
        print(" [x] hash verficition failed")

else:
    print ("""usage : 
            hashcalc.py file - to get file hash
            hashcalc.py file1 file2 - to compare files 
            """)