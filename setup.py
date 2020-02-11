import os, math, sys

#OS_bit = (round(math.log(sys.maxint,2)+1))  # get the bit

os.system("sudo apt-get install python-pip && sudo apt-get install tor")   # installing dependencies
os.system("pip install -U selenium")
os.system("pip install Pysocks")
os.system("pip install pyvirtualdisplay && apt-get install xvfb")

#print("\n \n {} \n \n".format(OS_bit))


os.system('firefox -v > tmp')                  # store result of firefox -v in tmp
result   =  open('tmp', 'r').read()            # result var reads the output
marker   = result.find('Firefox') + 8          # marker marks the 8th letter from the word "Firefox"
version  = result[marker:].splitlines()[0]     # spliting the output, the version is something like aa.bb.cc
a,b,c = version.split(".")                     # a is the var with the aa
os.remove('tmp')                               # removing the temporary file

FirefoxVersion = int(a)
second = 0

if FirefoxVersion  < 53:

    first = 16
    second = 1
    OS_bit = 64

elif FirefoxVersion == 53 or FirefoxVersion == 54:

    first = 18

elif FirefoxVersion > 54:

    first = 19

os.system("wget https://github.com/mozilla/geckodriver/releases/download/v0.{}.{}/geckodriver-v0.{}.{}-linux{}.tar.gz".format(first,second,first,second,OS_bit))
os.system("tar -xvzf geckodriver-v0.{}.{}-linux{}.tar.gz".format(first,second,OS_bit))
os.system("rm geckodriver-v0.{}.{}-linux{}.tar.gz".format(first,second,OS_bit))
os.system("chmod +x geckodriver")
os.system("mv geckodriver /usr/local/bin/")
chmod +x faitagram && chmod +x setup.py