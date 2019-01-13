import subprocess

contacts = subprocess.check_output(
    'gcalcli --nocolor agenda "`date`" 11:59pm', shell=True).decode('utf-8')

holiday = subprocess.check_output(
    'gcalcli --nocolor --cal "Holidays in India" agenda "`date`" 11:59pm', shell=True).decode('utf-8')

output = []

if 'No Events Found...' not in contacts:
    for event in contacts[16:].split('\n')[:-2]:
        output.append(event.strip())

if 'No Events Found...' not in holiday:
    for event in holiday[16:].split('\n')[:-2]:
        output.append(event.strip())

if output == []:
    output.append('No event today')

print(output)
