#!/bin/python3

import yaml
from jinja2 import Environment, FileSystemLoader, Template
import os
from jnpr.junos.utils.config import Config
from jnpr.junos import Device

fwtemplatepath = '/Users/echo/Documents/Juniper/Junos_Python/Configure/SRX-configuration-template.j2'
fwinputpath = '/Users/echo/Documents/Juniper/Junos_Python/Configure/SRX-vars.yml'
#load vars/YAML file into dictionary for python
with open ('/Users/echo/Documents/Juniper/Junos_Python/Configure/SRX-vars.yml', "r") as f2:
    fwinputvars = yaml.safe_load(f2)
#set env for j2 template 
jenvironment = Environment(loader=FileSystemLoader('/Users/echo/Documents/Juniper/Junos_Python/Configure/'))
#set path for j2
template = jenvironment.get_template('SRX-configuration-template.j2')
#merge vars and j2
fwtemplate = template.render(fwinputvars)
#path to device inventory 
fwinventory = '/Users/echo/Documents/Juniper/Junos_Python/Monitor/firewalls.txt'
#Get username and password
username = input("username:")
password = input("password:")
#Retreive device hostnames from file
with open(fwinventory, 'r') as file:
    firewalls = file.read().splitlines()
    #Connect to each device with PYEZ context manager
    for firewall in firewalls:
        cd = Device(host=firewall,user=username, passwd=password)
        with cd as dev:
            print("working on "+ firewall + " now")
            cu = Config(dev, mode='private')
            cu.load(fwtemplate, format='set')
            cu.pdiff()
            #cu.commit()