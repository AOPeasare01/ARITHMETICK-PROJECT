import time
from random import randint
import sys
import select
from colorama import Fore,Style

def time_interval(stage):
  intervals = [0, 5, 4.5, 4, 3.5, 3, 2.5, 2, 1.5, 1.0, 0.5]
  time.sleep(intervals[stage])

def questions(stage):
  occurence = [0, 5, 7, 9, 9, 9, 11, 11, 13, 13, 15]
  y = occurence[stage]
  return y

def numbers(stage):
  if stage == 1:
    a = randint(1, 9)
  elif stage == 2:
    a = randint(1, 20)
  elif stage == 3 or stage == 4:
    a = randint(10, 50)
  elif stage == 5 or stage == 6:
    a = randint(1, 50)
  elif stage == 7 or stage == 8:
    a = randint(1, 20)
  elif stage > 8:
    a = randint(1, 10)
  return a

def arithmeticSign(stage):
  if stage >= 1 and stage <= 5:
    b = randint(0,1)
  if stage > 5 and stage < 9:
    b = randint(0,2)
  if stage > 8:
    b = randint(0, 3)
  return b

def expectedTime(stage):
  expectIme = [0, 40, 40, 35, 30, 30, 35, 30, 30, 20, 15]
  y = expectIme[stage]
  return y

def input_with_timeout(seconds):
  response, _, _ = select.select([sys.stdin], [], [], seconds)
  if response:
    return sys.stdin.readline().strip()
  else:
    return ''

def intro():
    for remaining in range(5, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write(Fore.RED + "Test begins in{:2d}".format(remaining) + Style.RESET_ALL) 
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write(Fore.GREEN + "\rStart!               \n" + Style.RESET_ALL)

def error_sound():
    from replit import audio
    source = audio.play_file("error.mp3")

def kudos_sound():
    from replit import audio
    source = audio.play_file("kudos.mp3")

def game_level(stage):
  intro()
  time.sleep(0.5)
  cycles = 0
  sum1 = 0

  while cycles <= questions(stage):
    num = numbers(stage)
    if cycles == 0:
      print(num)
      sum1 += num
    else:
      z = arithmeticSign(stage)
      if z == 0:
        print('+'+ str(num))
        sum1 += num
      elif z == 1:
        print('-'+ str(num))
        sum1 -= num
      elif z == 2:
        print('x' + str(num))
        sum1 *= num
      elif z == 3:
        print('÷' + str(num))
        sum1 /= num
    time_interval(stage)
    cycles += 1

  print('Enter answer below:')
  if stage >= 8:
      print('''Correct all decimals to 2 d.p if applicable''')
  start = time.time()
  ans = input_with_timeout(expectedTime(stage))
  end = time.time()
  diff = round(end - start)
  
  if ans == '':
      error_sound()
      print(Fore.RED + 'You got timed out ⌛ or you entered nothing!' + Style.RESET_ALL)
      print('Performance review: Your response time exceeded {} seconds or your submission was incomplete'.format(expectedTime(stage)))
      result = 'failed'
  if ans.isalpha():
      error_sound()
      print(Fore.RED + 'Invalid entry for arithmetic solution.❌' + Style.RESET_ALL)
      print('Performance review: Your response time,however, was about {} seconds'.format(diff))
      result = 'failed'
  if float(sum1).is_integer() == False:
      if ans == round(sum1, 2):
        kudos_sound()
        print(Fore.GREEN + "Bravo! That's correct👍." + Style.RESET_ALL)
        print('Performance review: Your response time, however, was about {} seconds'.format(diff))
        result = 'passed'
      else:
          error_sound()
          print('Sorry😥😥😥! The correct answer is ' + Fore.RED + Style.BRIGHT + '{}.'.format(round(sum1, 2)) + Style.RESET_ALL)
          print('Performance review: Your response time, however, was about {} seconds'.format(diff))
          result = 'failed'
  else:
    if ans == '':
        result == 'failed'
    elif ans.isalpha():
        result == 'failed'
    
    elif float(ans) == sum1:
            kudos_sound()
            print('Performance review: Your response time was about {} seconds'.format(diff))
            print(Fore.GREEN + "Bravo! That's correct👍" + Style.RESET_ALL)
            result = 'passed'
    else:
            error_sound()
            print('Sorry😔😔😔! The correct answer is ' + Fore.RED + Style.BRIGHT + '{}.'.format(sum1) + Style.RESET_ALL)
            print('Performance review: Your response time, however, was about {} seconds'.format(diff))
            result = 'failed'

  return result

def stage_results(stage):
  level = game_level(stage)
  if level == 'passed':
    num = 1
  elif level == 'failed':
    num = 0

  return num