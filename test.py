import subprocess # import the subprocess module

dump = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', 'Pakt_287', 'key=clear']).decode('CP866', errors='ignore').split('\n') # get the list of all wifi configs
for line in dump:
    if "Содержимое ключа" in line:
        wifi_pass = line.split(":")[1][1:-1]
        break
print(wifi_pass)