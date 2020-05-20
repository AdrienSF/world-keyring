# World Keyring

In a conventional digital keyring or keychain passwords are encrypted and stored
on a system, and a master password is used to retrieve them. The goal for this
project is to create a keyring system that entirely avoids the need to store
passwords. For every account, there is information "stored" in the world around
us related to said account: the date the site or service was launched, the email
address tied to the account, or even the URL to the wikipedia page about the site.
World keyring is in effect a function that takes this type of information and a
master password as input, and computes a password.

The advantage of this concept over conventional keyrings is that you can use
your keyring on any machine, since no passwords need to be stored. You could
log into a library computer, and still use your master password to access all
your accounts.
The disadvantage is that you can't create your own passwords, you'll need to set
every password based on this system.

## Project status
I've completed a proof of concept in the form of a simple firefox extension.
This extension simply concatenates a given master password and the URL of the
current page, hashes it, and finally inserts this hash into any password input
fields present on the page.

## Cryptographic Security
The world keyring firefox extension uses sha256, which is well known and largely
considered secure. However if it is known that this extension is being used,
this proof of concept is no better than using one password for all your accounts.
To crack the password of any given account, one only needs to check the hashes
of concat("possible master password", "URL"), in which case the master password
will be found and all accounts will be compromised. There are many possible
inputs to sha256 that will output the correct password, but there is likely
only one such input of the form "masterpassword" + "URL".
In the future I would like to make an implementation of the world keyring idea
that is actually secure. To achieve this, I need a system where there are many,
many different possible master passwords that map to the same output password.
In this way, even if one password is compromised, it will not be feasible to
deduce the master password.

## DISCLAIMER
The firefox extension included in this project is a proof of concept that is not
intended for use. It is not a secure keyring for one, but more importantly never
entrust your passwords to third-party software.

## Installation
If you wish to test the firefox extension included in this project, go to the
about:debugging page in firefox, press "load temporary extension" and select
the "manifest.json" file in this repository.

## Usage
With the firefox extension loaded, a master password input field will appear at
the top of the page. After filling this field and pressing the adjacent
auto-fill password button, the password for that given site will appear in any
password input fields present on the page (login and account creation fields).
