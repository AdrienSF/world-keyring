import hashlib
'''
I eventually realised that something like a hash fits the requirements for
this project. Simply concatenate the master password P and the site name X, and
use it's hash as the password for site X. This ensures a high level of security
across all passwords, and it's impossible to deduce other passwords
(or the master password) even if one password is leaked.
However... it's increadibly lame. There's no elaborate code or fancy tricks, so
I am quite dissapointed that the best solution seems to be the simplest one.
'''

# input master password and site name
toHash = input("input [master pasword][site name]: ")

# compute hash
hash = hashlib.sha256(toHash.encode('utf-8')).hexdigest()

# output password
print("password:")
print(hash)
