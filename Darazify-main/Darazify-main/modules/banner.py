from colorama import init, Fore, Style
from modules import clrscr
 
class Banner:
    def __init__(self):
        print(Fore.CYAN + '''
        
                 ███████                                     ██   ████         
                ░██░░░░██                                   ░░   ░██░   ██   ██
                ░██    ░██  ██████   ██████  ██████   ██████ ██ ██████ ░░██ ██ 
                ░██    ░██ ░░░░░░██ ░░██░░█ ░░░░░░██ ░░░░██ ░██░░░██░   ░░███  
                ░██    ░██  ███████  ░██ ░   ███████    ██  ░██  ░██     ░██   
                ░██    ██  ██░░░░██  ░██    ██░░░░██   ██   ░██  ░██     ██    
                ░███████  ░░████████░███   ░░████████ ██████░██  ░██    ██     
                ░░░░░░░    ░░░░░░░░ ░░░     ░░░░░░░░ ░░░░░░ ░░   ░░    ░░   
    ''' + Style.RESET_ALL)

        print(f'''

                                        {Fore.RED}♥{Style.RESET_ALL} v 1.01 {Fore.LIGHTCYAN_EX}♥{Style.RESET_ALL}
                                Created by : {Fore.CYAN} MaRyAm KhANaM{Style.RESET_ALL}
                                  {Fore.RED}https://github.com/mazuu06{Style.RESET_ALL}
                                    
            {Fore.WHITE}Welcome to {Style.RESET_ALL}

            {Fore.MAGENTA}This tool is for educational purposes only and the creator is not responsible for any actions performed by the users.{Style.RESET_ALL}
            
        ''')

        temp = input(f'{Fore.CYAN}Your output also save in {Fore.WHITE}{Fore.GREEN}output.txt{Style.RESET_ALL}{Fore.LIGHTYELLOW_EX} file.{Style.RESET_ALL} Press ENTER to continue: ')
