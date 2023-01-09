import get_wifi as wifi

import os
import ctypes
import locale

def main():
    vers=os.name
    if vers=="nt":
        win_lang=ctypes.windll.kernel32
        win_lang=locale.windows_locale[win_lang.GetUserDefaultUILanguage()]

        if win_lang=="ru_RU":

            wifi_list=wifi.get_wifi_win("ru")
        else:
            wifi_list=wifi.get_wifi_win("en")
        print(wifi_list)
    if vers=="posix":
        wifi_list=wifi.get_wifi_linux()
        print(wifi_list)
    
    