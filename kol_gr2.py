#-*- encoding=utf-8 -*-

class MatrixSizeMismatchException(Exception):
 def __init__(self,size1,size2):
  self.expected_size = size1
  self.got_size = size2
 def __str__(self):
  return "Matrix size  mismatch - size "+ str(self.expected_size)+" needed, size "+ str(self.got_size)+" given."

# init assumes that given tuple represents square matrix
class Matrix(object):
 def __init__(self,tple,n):
  self.matrix = tple
  self.size = n
  self.i = 0

 def __iter__(self):
  return self.matrix[i]
  
 def __add__(self,mtrix):
  if self.size != mtrix.size:  
   raise MatrixSizeMismatchException(self.size,mtrix.size)
  else:
   sum_matrix = []
   for i in range(len(self.matrix)):
    tmp_tple = []
    for j in range(len(self.matrix[1])):
     tmp_tple.append(self.matrix[i][j])
    sum_matrix.append(tmp_tple)
  return Matrix(sum_matrix,self.size)

 def __mul__(self,mtrix):
  if self.size != mtrix.size:
   raise MatrixSizeMismatchException(self.size,mtrix.size)
  else:
   mtrxmult = [[0]*self.size]*self.size
   for i in range(self.size):
    for j in range(self.size):
     for k in range(self.size):
      mtrxmult[i][j] +=  self.matrix[i][k] * mtrix.matrix[k][j]
  return Matrix(mtrxmult,self.size)

 def __str__(self):
  mtrx = ""
  for i in range(self.size):
   row = ""
   for j in range(self.size):
    row += str(self.matrix[i][j]) + " "
   row += "\n"
   mtrx += row
  return mtrx

 def next(self):
  if self.i < self.size:
   i = self.i
   self.i += 1
   return self.matrix[i]
  else:
   raise StopIteration()

if __name__ == '__main__':

 print "matrix_1 = Matrix(((4,7),(2,5)), 2)"
 print "matrix_2 = Matrix(((2,2),(2,1)), 2)"

 matrix_1 = Matrix(((4,7),(2,5)), 2)
 matrix_2 = Matrix(((2,2),(2,1)), 2)

 print matrix_1
 print matrix_2

 print "matrix_3 = matrix_1 + matrix_2\n"
 matrix_3 = matrix_1 + matrix_2

 print matrix_3

 try:
  matrix_4 = matrix_1 * matrix_2
  print matrix_4
 except MatrixSizeMismatchException as msme:
  print msme
 
 matrix_5 = Matrix(((1,2,3),(2,3,4),(5,6,7)),3)

 try:
  matrix_4 = matrix_1 * matrix_5
  print matrix_4
 except MatrixSizeMismatchException as msme:
  print msme

 for i in range(matrix_3.size):
  print str(i+1) +". vector of matrix" + str(matrix_3.next())
