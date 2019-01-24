
# zip-cracker

  Overview:
  ========
zip-cracker is a password cracker for password protected zip file. It takes a word-list/dictionary-list to brute force the password. If the password contains in the word-list/dictionary-list file, this program will crack that password guaranteed. The password cracking time depends on the computer speed and performance.   

Dependencies
========
 This program written in Python 2.7

Compatibility: 
========
This program will run in any python installed Linux distros and windows machine. Tested on Kali Linux and Windows 10 (python 2.7 installed)

 USAGE: 
========
Navigate to the program folder and run the following command:

python zipfile-cracker.py -f (password protected zip file) -d (word list or dictionary file)
 
optional arguments:
  -h /  --help           == show this help message 
python zipfile-cracker.py  == Program usage

Examples
========
python zipfile-cracker.py -f evil.zip -d dictionary.txt

Bugs & Contact
==============
Feel free to email me with any problem, bug, suggestions or fixes at:
Sazzad Ovi <ovisecret@gmail.com>
