#!/bin/bash

devices="SRX300"
read -p "enter a username" username
read -p "enter a password" password
commands="edit; set interfaces ge-0/0/1 description To-PE ; show | compare; commit check; commit; exit; exit;"
for i in ${devices}; do 
    echo "Working on device: ${i}"
    sshpass -p ${password} ssh -o StrictHostKeyChecking=no ${username}@${i} ${commands}
    echo =======================
done 