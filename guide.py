def startWork():
    start_response = input('Press Enter to START THE TEST or enter any other key to view rules and guidelines for ARITHMETICK\n')
    return start_response

def rules():
    print('''i. All tests are specially measured to increase brain power and under no circumstance should a calculator or machine be used as aid in assessment.

Allow all numbers to print on screen and until you see the 'Enter answer below' instruction do not attempt to make a submission else you score null.

There are 10 levels to the game, arranged in order of increasing difficulty.

For wrong submissions from Level 1 to Level 4, you restart from Level 1.

Level 5 is the checkpoint after which you can restart from the most recent level you exited.

With the completion of the last 3 levels, comes a bronze, silver and gold(the ultimate indication of mastery)

Good luck Scholar!''')
    continue_response = input('Press Enter to return to main game\n')
    return continue_response

