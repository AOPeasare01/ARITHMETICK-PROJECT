from driver_functions import stage_results
from remarks import welcome, test_intro, wrong_remarks, congrats, warning
from guide import startWork, rules
import time
from colorama import Fore, Style

def main():
    warning()
    welcome()
    time.sleep(2)
    start = startWork()
    while start != '':
        count = rules()
        if count == '':
            start = startWork()
    stage = 1
    answer = ''
    count = 0
    while answer == '' and count == 0 and stage < 10:
        test_intro(stage)
        print()
        result = stage_results(stage)
        stage += 1
        if result == 0:
            wrong_remarks()
            stage = 1
            while True:
                answer = input(
                    'Press Enter to restart from Level 1 or enter Q to quit\n')
                if answer == '' or answer == 'q' or answer == 'Q':
                    break
                print(Fore.RED + 'Invalid entry❌' + Style.RESET_ALL)
            if answer == 'q' or answer == 'Q':
                count = 1
        else:
            while True:
                answer = input(
                    'Press Enter to continue to Level {} or enter Q to quit\n'.
                    format(stage))
                if answer == '' or answer =='Q' or answer == 'q':
                    break
                print(Fore.RED + 'Invalid entry❌' + Style.RESET_ALL)
            if answer == 'q' or answer == 'Q':
                count = 1

        #checkpoint
        while stage >= 5:
            if stage == 5:
                print(Fore.RED + 'Congratulations! You made it to the checkpoint.🏁' + Style.RESET_ALL)
                time.sleep(2)
            test_intro(stage)
            print()
            result = stage_results(stage)
            while result == 0:
                wrong_remarks()
                while True:
                    answer = input(
                        'Press Enter to restart Level {} or enter Q to quit\n'.
                        format(stage))
                    if answer == '' or answer == 'q' or answer == 'Q':
                        break
                    print(Fore.RED + 'Invalid entry❌' + Style.RESET_ALL)
                if answer == 'q' or answer == 'Q':
                    count = 1
                result = stage_results(stage)
            congrats(stage)
            if stage > 10:
                count = 1
            while stage != 10:
                answer = input(
                    'Press Enter to continue to Level {} or enter Q to quit\n'.
                    format(stage + 1))
                if answer == '' or answer == 'q' or answer == 'Q':
                    break
                print()
            if answer == 'q' or answer == 'Q':
                count = 1
            stage += 1

    print('Level Rank : Level {}'.format(stage))
    if stage < 8:
        award = 'None'
    elif stage == 8:
        award = 'Bronze'
    elif stage == 9:
        award = 'Silver'
    elif stage == 10:
        award = 'Gold'
    print('Award Won🏆: {}'.format(award))

if __name__ == "__main__":
    main()

