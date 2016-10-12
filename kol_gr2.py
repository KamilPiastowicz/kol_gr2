#-*- encoding=utf-8 -*-

#Write a library that contains a class that can represent any 2𝑥2 real matrice. 
#Include two functions to calculate the sum and product of two matrices. 
#Next, write a program that imports this library module and use it to perform calculations.
#Examples:
#
# matrix_1 = Matrix(4,5,6,7)
# matrix_2 = Matrix(2,2,2,1)
#
# matrix_3 = matrix_2.add(matrix_1)
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#(If you want you can expand implementation to NxN matrix.)
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#When you are done upload this code to your github repository. 
#The whole repository MUST be named "kol_gr2"! 
#
#Delete these comments before commit!
#Good luck.

#assumes that given tuple represents square matrix
class Matrix:
 def __init__(self,tple,n):
  self.matrix = tple
  self.size = n
  
 def __add__(self,mtrix):
  if self.size != mtrix.size:  
   print "matrixes aren't equally big"
  else:
   sumMatrix = []
   for i in range(len(self.matrix)):
    tmpTple = []
    for j in range(len(self.matrix[1])):
     tmpTple.append(self.matrix[i][j])
    sumMatrix.extend(tmpTple)
   return Matrix(sumMatrix,self.size)

def printMatrix(mtrix):
 for i in range(mtrix.size):
  row = ""
  for j in range(mtrix.size):
   row += str(mtrix.matrix[i][j]) 
   row += " "
  print row
 print "\n"



print "matrix_1 = Matrix(((4,7),(2,5)), 2)"
print "matrix_2 = Matrix(((2,2),(2,1)), 2)"

matrix_1 = Matrix(((4,7),(2,5)), 2)
matrix_2 = Matrix(((2,2),(2,1)), 2)

printMatrix(matrix_1)
printMatrix(matrix_2)

print "matrix_3 = matrix_1 + matrix_2"
matrix_3 = matrix_1 + matrix_2

print matrix_3

printMatrix(matrix_3)



