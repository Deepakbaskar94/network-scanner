# network-scanner
network scanner to scan the ip, mac and open port and live <br />

# install everything inside the virtual environment
# windows
pip install virtualenv <br />
py -3 -m venv .venv <br />
.venv/scripts/activate <br />

# ubuntu
sudo pip3 install virtualenv <br />
virtualenv -p python3 env1 <br />
. env1/bin/activate <br />

# pip install -r requirements.txt


# NETSCAN
myip - to see my ip and my hostname <br />
main-scapy.py - to see all ip, macaddress in my network (UI based pyQT5) & port scanning on a ip possible <br />
main.py - scan and show ip but not proper some issue <br />

# portscan
netscanport.py - to scan the port of a particular ip <br />
netscanlive.py - to scan the live ip depends on port so edit the port to see the live ip <br />

