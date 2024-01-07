#!/bin/bash

devices="SRX300"
commands="edit; set interfaces ge-0/0/1 description To-PE ; show | compare; commit check; commit; exit; exit;"
for i in ${devices}; do 
    echo "Working on device: ${i}"
    sshpass -p "Juniper" ssh -o StrictHostKeyChecking=no admin@${i} ${commands}
    echo =======================
done 