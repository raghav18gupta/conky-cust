# -*- coding: utf-8 -*-
import subprocess
import pickle

output = []

try:
    contacts = subprocess.check_output(
        'gcalcli --nocolor agenda "`date`" 11:59pm', shell=True, stderr=subprocess.STDOUT, timeout=5).decode('utf-8')

    holiday = subprocess.check_output(
        'gcalcli --nocolor --cal "Holidays in India" agenda "`date`" 11:59pm', shell=True, stderr=subprocess.STDOUT, timeout=5).decode('utf-8')

    if 'No Events Found...' not in contacts:
        for event in contacts[16:].split('\n')[:-2]:
            output.append(event.strip())

    if 'No Events Found...' not in holiday:
        for event in holiday[16:].split('\n')[:-2]:
            output.append(event.strip())

    if output == []:
        output.append('No e vent today')

    with open('/home/raghav18gupta/Desktop/gitHub/projects/conky-cust/pkl.pkl', 'wb') as f:
        pickle.dump(output, f)

except:
    with open('/home/raghav18gupta/Desktop/gitHub/projects/conky-cust/pkl.pkl', 'rb') as f:
        output = pickle.load(f)
    print(r'✘ Connect to internet')

for event in output:
    print(r'➜ ', event)
