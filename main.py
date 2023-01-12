import get_wifi as wi_fi
import get_wifi_pass as wifi_pass_func
import service as serv

import os




def wifi_list(vers):

    if vers=="nt":
        
        win_lang=serv.get_win_lang()

        if win_lang=="ru_RU":

            wifi_list=wi_fi.get_wifi_win("ru")

        else:
            wifi_list=wi_fi.get_wifi_win("en")
        
       
    if vers=="posix":
        wifi_list=wi_fi.get_wifi_linux()
    
    return wifi_list

def wifi_pass(wifi_name, vers):
    if vers=="nt":

        win_lang=serv.get_win_lang()

        if win_lang=="ru_RU":
            pass_= wifi_pass_func.get_pass_win("ru", wifi_name)
        else:
            pass_= wifi_pass_func.get_pass_win("en", wifi_name)
    if vers=="posix":
        pass_=wifi_pass_func.get_pass_linux(wifi_name)

    return pass_ 

        
def main():
    
    
    wifi=wifi_list(os.name)
    print('Enter the number of the network you want to get the pass to')
    for i in range(len(wifi)):
        print(i + 1, ')', wifi[i])
    print('0 ) Exit')
    num=int(input())
    if num==0:
        exit()
    pass_=wifi_pass(wifi[num-1], os.name)
    print('Name:', wifi[num-1],
                'Password:', pass_)
    


    

if __name__ == "__main__":
    main()
    