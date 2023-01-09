import subprocess # import subprocess module

wi_fi_list=subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('CP866', errors='ignore').split('\n')# get the list of all the wifi profiles
# if you system languade is not Russian - use UTF-8

wi_fi_names=[]

for wi_fi in wi_fi_list:
    if "Все профили пользователей" in wi_fi:
        wi_fi_names.append(wi_fi.split(":")[1][1:-1]) # get the name of the wifi profile

print(wi_fi_names)

