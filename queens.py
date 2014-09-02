#!/usr/bin/env python

#^^^^^^^^^^^^^^^^^^^#
#^^^^^^IMPORTS^^^^^^#
#-------------------#

import math
import csv
import numpy as np
import random
from sys import stdout

#^^^^^^^^^^^^^^^^^^^#
#^^^^^FUNCTIONS^^^^^#
#-------------------#

def increment_board(board,size):
   #zero out current board
   for i in range(len(board)):
      for j in range(len(board)):
         board[i][j] = 0

   #Populate board with 8 queens
   for i in xrange(size):
      queenps = random.randint(0,7)
      board[i][queenps] = 1

#   printarray = np.array(board)
#   print printarray
   return board
   
def check_verticle(board,exitcheck):
   for i in xrange(len(board)):
      sum = 0
      for j in xrange(len(board[i])):
         sum = sum + board[j][i]
      if sum > 1:
         exitcheck = 1
         break
      else:
         pass   
   return exitcheck
   
def check_diagonal(board,exitcheck):
   for row in xrange(len(board)):
      for column in xrange(len(board[row])):
         if board[row][column] == 1:
            offset = 0
            for lower_row in xrange(row+1,len(board)):
               offset = offset + 1
               leftcolumn = column-offset
               rightcolumn = column+offset
               if leftcolumn >= 0:
                  if board[lower_row][leftcolumn] == 1:
                     exitcheck = 1
                     break
               if rightcolumn <= 7:   
                  if board[lower_row][rightcolumn] == 1:
                     exitcheck = 1
                     break
   return exitcheck
   


#^^^^^^^^^^^^^^^^^^^#
#^^^PROGRAM START^^^#
#-------------------#

size = 8

#create board
board = []
for i in xrange(8):
   board.append([])
   for j in xrange(8):
      board[i].append(0)
         
board = increment_board(board,size)

fail = True
count = 0
while fail == True:
   count = count + 1
   stdout.write(" Trials" + "\r%d" % count)
   stdout.flush()
   exitcheck = 0
   board = increment_board(board,size)
   exitcheck = check_verticle(board,exitcheck)
   if exitcheck == 1:
      continue
   exitcheck = check_diagonal(board,exitcheck)
   if exitcheck == 1:
      continue   
   
   
   
   if exitcheck == 0:
      print "\nPASSED"
      print np.array(board)
      exit()

         









