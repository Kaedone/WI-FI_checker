import subprocess # import subprocess module

wifi_pass=""

def get_pass_win(language, wifi_name):

    if language == 'ru':
        dump = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', wifi_name, 'key=clear']).decode('CP866', errors='ignore').split('\n') # get the list of all wifi configs
        for line in dump:
            if "Содержимое ключа" in line:
                wifi_pass = line.split(":")[1][1:-1]
                break
        
    if language == 'en':
        dump = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', wifi_name, 'key=clear']).decode('utf-8', errors='ignore').split('\n') # get the list of all wifi configs
        for line in dump:
            if "Key Content" in line:
                wifi_pass = line.split(":")[1][1:-1]
                break

    return wifi_pass

def get_pass_linux(wifi_name):
    subprocess.run(f"sudo cat /etc/NetworkManager/system-connections/{wifi_name} > wifi_pass.txt", shell=True)

    #TODO: debug this function