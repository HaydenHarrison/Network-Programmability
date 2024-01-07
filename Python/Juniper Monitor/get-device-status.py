#!/bin/python3

#Retrieve basic device information from a list of devices 
#Import Juniper PYEZ modules 
from jnpr.junos import Device
from jnpr.junos.utils import config
from jnpr.junos.utils import sw
from pprint import pprint
from lxml import etree  
#Path to list of Juniper devices to run script on 
file_path = "/Users/echo/Documents/Juniper/Junos_Python/Monitor/firewalls.txt" 
#Get username and password
username = input("username:")
password = input("password:")
#Retreive device hostnames from file
with open(file_path, 'r') as file:
    firewalls = file.read().splitlines()
    #Connect to each device with PYEZ context manager
    for firewall in firewalls:
        cd = Device(host=firewall,user=username, passwd=password)
        #Run CLI commands or XML RPC's against target device
        with cd as dev:
            pprint(dev.facts['version'])
            #print(dev.cli("show configuration"))
            int = dev.rpc.get_interface_information({'format':'text'}, terse = True)
            print(etree.tounicode(int))