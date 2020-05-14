import hashlib


hashedPassword = "2bf6ce327a109513cd06e3062f193fc93c98d31f3fe5e7e45215628311d8e0b3"


inputPassword = True
while inputPassword:
    inputPassword = input("input password to example.com: ")
    if str(hashlib.sha256(inputPassword.encode('utf-8')).hexdigest()) == hashedPassword:
        print("correct")
        break
    else:
        print("access denied")
