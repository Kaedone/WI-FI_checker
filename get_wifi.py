import subprocess # import subprocess module

def get_wifi_win(language):

    if language == 'ru':
    
        wi_fi_list=subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('CP866', errors='ignore').split('\n')# get the list of all the wifi profiles
        

        wi_fi_names=[]

        for wi_fi in wi_fi_list:
            if "Все профили пользователей" in wi_fi: 
                wi_fi_names.append(wi_fi.split(":")[1][1:-1]) # get the name of the wifi profile
        
        return wi_fi_names
    
    if language == 'en':

        wi_fi_list=subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors='ignore').split('\n')# get the list of all the wifi profiles
        

        wi_fi_names=[]

        for wi_fi in wi_fi_list:
            if "All User Profile" in wi_fi:
                wi_fi_names.append(wi_fi.split(":")[1][1:-1]) # get the name of the wifi profile
        
        return wi_fi_names


def get_wifi_linux():
    
    subprocess.run("sudo ls /etc/NetworkManager/system-connections/ > wifi_list.txt", shell=True)
    
    with open("wifi_list.txt", "r") as file:
        wifi_list = file.read().split("\n")
    
    for i in range(len(wifi_list)):
        temp=wifi_list[i]
        for j in range(len(temp)):
            if temp[j]==".":
                wifi_list[i]=temp[:j]
                break

        