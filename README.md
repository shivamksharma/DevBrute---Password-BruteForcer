# **DevBrute - A Password Brute Forcer**


Devbrute is my first project in InfoSec. It is basically a Brute Force Tool for All Social Media Platform. Basically Brute force attacks are usually used to obtain personal information such as passwords, passphrases, usernames and Personal Identification Numbers (PINS), and use a script, hacking application, or similar process to carry out a string of continuous attempts to get the information required. A brute force attack, also known as an exhaustive search, is a cryptographic hack that relies on guessing possible combinations of a targeted password until the correct password is discovered. The longer the password, the more combinations that will need to be tested. A brute force attack can be time consuming, difficult to perform if methods such as data obfuscation are used, and at times down right impossible. However, if the password is weak it could merely take seconds with hardly any effort. Weak passwords are like shooting fish in a barrel for attackers, which is why all organizations should enforce a strong password policy across all users and systems.


# Installation in Linux

  - Git Clone
    ```
    git clone https://github.com/shivamksharma/DevBrute.git
    cd DevBrute
    ```

  - Install the Requirements
    ```
    pip3 install -r setup.py
    ```

  - Run DevBrute 
    ```
    python3 devbrute.py -s (socilamediaurl) -username (username) -w (wordlist)
    ```



### Version 
  > CURRENT VERSION - 1.1

### What's New
  - Fixed Some Bugs
  - Fixed Social Media Links Error
  - Fixed Wordlist Problem