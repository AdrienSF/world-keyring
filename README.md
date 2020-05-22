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
This extension takes a master password and the current page URL as input and inserts a password into any password input
fields present on the page. Since the URL of the current page does not uniquely identify an account, this implementation cannot be used in practice. For example, it won't be possible to different passwords for multiple accounts on the same website. A practical implementation would need to use information "stored" in the world around
us that doesn't have the limitations of a URL.

## Cryptographic Security
The world keyring firefox extension uses uses the following password P for a given website W:

sha1("master password" ⊕ "W") = P

where '⊕' is the XOR binary operation.

sha1 is known to be vulnerable to collision attacks, but such attacks are irrelevant here since their purpose is not to crack passwords. In this case the fact that there are collisions is beneficial, and I chose sha1 as it shows collisions that are quite evenly distributed compared to other hash algorithms[1].

pre-hash(W) = "master password" ⊕ "W" is a bijective function, so every website W will have a distinct pre-hash. Furthermore, sha1 has a collision probability on the order of 10^-45[2] for under 100 inputs, so in practice every website will have a different password. As such, if an attacker obtains your password P to website W, no other accounts will be directly compromised. To access other accounts, the attacker will need the master password. To find this master password, the attacker would first need to "unhash" P to get the pre-hash, something largely considered implausible, and then compute "pre-hash" ⊕ "W" to obtain a possible master password. I say possible master password, because there are on average 2^(10^19)[3] strings S such that sha1(S) = pre-hash, so it is almost certain that the attacker would only find a useless piece of information. In this case the attacker can only start over and work towards the implausible task of "unhashing" P once again.


[1] https://michiel.buddingh.eu/distribution-of-hash-values
[1] http://web.archive.org/web/20110725085124/http://bitcache.org/faq/hash-collision-probabilities
[2] 2^(2^64)/2^160 ~= 2^(10^19), https://crypto.stackexchange.com/questions/34518/sha-1-number-of-possible-inputs-number-of-possible-outputs-how-many-inputs-ha
From [1] I can conclude that the average of 2^(10^19) is relatively consistent.

## DISCLAIMER
The firefox extension included in this project is a proof of concept that is not
intended for use. Never entrust your passwords to third-party software.

## Installation
If you wish to test the firefox extension included in this project, go to the
about:debugging page in firefox, press "load temporary extension" and select
the "manifest.json" file in this repository.

## Usage
With the firefox extension loaded, a master password input field will appear at
the top of the page. After filling this field and pressing the adjacent
auto-fill password button, the password for that given site will appear in any
password input fields present on the page (login and account creation fields).
