import ctypes
import locale


def get_win_lang():
    win_lang=ctypes.windll.kernel32
    win_lang=locale.windows_locale[win_lang.GetUserDefaultUILanguage()]
    return win_lang