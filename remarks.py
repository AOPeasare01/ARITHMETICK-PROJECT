import time
import sys
from driver_functions import expectedTime
from colorama import Fore, Style

def warning():
    print(Fore.RED + 'WARNING : For full functionality of the program, run on Replit Online IDE!' + Style.RESET_ALL)
    
intro = '''Arithmetic is numbers you squeeze from your head to your hand to your pencil to your paper till you get the answer'''

def welcome():
    lis = list(intro)
    for char in lis:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.15)
    time.sleep(2)

    print('                                     ---Carl Sandburg')
    time.sleep(2)
    print(Fore.GREEN + 'WELCOME TO ARITHMETICK✔✔✔!' + Style.RESET_ALL)

def test_intro(stage):
    intro = 'Welcome to Level {}. You have {} seconds to enter solution after the submission instruction'.format(stage, expectedTime(stage))

    lis = list(intro)
    for char in lis:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.15)
        
def wrong_remarks():
    print(Fore.RED + "Try again!" + Style.RESET_ALL)

def congrats(stage):
        if stage == 8:
            print(Fore.GREEN + 'Congratulations! You are a proud BRONZE medal holder.🥉' + Style.RESET_ALL)
            time.sleep(2)

        if stage == 9:
            print(Fore.GREEN + 'Congratulations! You are a proud SILVER medal holder.🥈' + Style.RESET_ALL)
            time.sleep(2)

        if stage == 10:
            print(Fore.GREEN + 'ALL HAIL THE KING! You are a proud GOLD medal holder.🥇' + Style.RESET_ALL)
            time.sleep(2)


    