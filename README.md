# network-scanner
network scanner to scan the ip, mac and open port and live

# install everything inside the virtual environment
# windows
pip install virtualenv
py -3 -m venv .venv
.venv/scripts/activate

# ubuntu
sudo pip3 install virtualenv
virtualenv -p python3 env1
. env1/bin/activate

# pip install -r requirements.txt


# NETSCAN
myip - to see my ip and my hostnmae
main-scapy.py - to see all ip, macaddress in my network (UI based pyQT5) & port scanning on a ip possible
main.py - scan and show ip but not proper some issue
