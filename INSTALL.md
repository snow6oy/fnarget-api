# Installation notes for Launchkey Python SDK

# Ubunutu
## ubuntu LTS v14 ships with python 2.7 
## install vanilla OS
```
ubuntu-14.04.3-server-amd64.iso
```
# stuff we will need later
```
sudo apt-get install openssh-server
sudo apt-get install gcc
sudo apt-get install libgmp-dev
sudo apt-get install python-dev
sudo apt-get install python-setuptools
```

# Launchkey

## Install the SDK
```
git clone https://github.com/LaunchKey/launchkey-python.git
cd launchkey-python/
sudo python setup.py install
```
## Test with
```
gavin@fnarg:~/launchKey/fnarget$ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13)
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import launchkey
```
## Note about pcrypto 
Most install fails were down to pcrypto, after a few tries v2.6.1 worked for me
## Running fnarget
fnarget.py should now run, but to authenticate agaisnt the API you will need to update file location of the private key to match your system
```
9 pvtKey=open('/home/gavin/launchKey/fnarget/fnarget.key', "r").read()
```
