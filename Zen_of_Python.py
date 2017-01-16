#!/usr/bin/python3
#Zen_of_Python.py by Michael Akintuyosi
#Copyright(c) 2016


"""Working with Python's Input Method"""

import time
from datetime import date


class Man:

    def call(self):
       time.sleep(4)
       print()
       print('\t*************************************************\n')
       print('\t*******The Zen of Python is Beautiful************\n')
       print('\t****************************************************\n')
  
       
       import this
    

    def Cuz(self):
      today = date.today()
      self.n = input('What is your name:')
      print('Now your Birthday, The Month and Day, in numbers only')
      time.sleep(2)
      self.month = int(input('Give me the Month >> :'))
      self.day = int(input('Give me the Day >> :'))
      self.year = today.year
      self.bday = date(self.year,(self.month),(self.day))
      print('Thanks {} , I\'ll take care of the rest...... '.format(self.n))
      time.sleep(3)
      self.time_to_bday = abs(self.bday - today)
      time.sleep(2)
      if self.bday < today:
           print('Wow your birthday was {} days ago'.format(self.time_to_bday.days))
      else:
          print('Wow Your Birthday is in {} days '.format(self.time_to_bday.days))
      time.sleep(3)

      print('Anyway {}, Here comes the lovely part!'.format(self.n))



def main():
    man = Man()
    try:
      man.Cuz()
    except:
      print('Oops! There seems to be an error, Try again {} to see the Zen of Python'.format(man.n))
    else:
     man.call()

if __name__ =='__main__':main()
