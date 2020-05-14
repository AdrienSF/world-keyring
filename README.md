# World Keyring

In a conventional digital keyring or keychain passwords are encrypted and stored
on a system, and a master password is used to retrieve them. The idea for this
project is to create a keyring system that entirely avoids the need to store
passwords. The world keyring is in effect a function that maps master passwords
to functions.

What I aim for world keyring to do:
- take master password as input
- map the password to a function
- this function takes the website name as input, and outputs the password to said site
  
This system should be just as secure in principle as a conventional keyring.
Even if the password P of website W is leaked, the master password cannot be
inferred as there are many functions (and thus master passwords) that map
website W to P. Suppose you find a function that maps W to P. If you try to use
this function to find the password to a different site X for example, there is
only an insignificant chance that it will map to the correct password.

The advantage of this concept over conventional keyrings is that you can use
your keyring on any machine, you only need to run this python script. You could
log into a library computer, and still use your master password.

This project is intended to be a proof of concept, so I am not planing on
implementing features to auto-complete password input fields. This script simply
takes a master password and website name, and outputs the password for said
website.

Besides just the site name, the system's function could use any number of other
inputs that are "stored" in the world around us: the date the site or service
was launched, the email adress tied to the account, or even the URL to the
wikipedia page about the site. The idea is to use the world to keep your
passwords. The world is your keyring.

## DISCLAIMER
I claim this system is secure, but I have not yet evaluated it's cryptographic
security in theory, nor have I tested it in practice, so this may end up being
just a cool idea that doesn't actually work. (like communism)

## Project status
I've only just started with a simple prototype.
