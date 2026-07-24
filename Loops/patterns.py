#         *****
#         *****
#         *****
#         *****
#         *****

def p1():
  for i in range(5):
    for j in range(5):
      print("*",end=" ")
    print()

# p1()


#   *
#   * *
#   * * *
#   * * * *
#   * * * * *

def p2():
  for i in range(5):
    for j in range(i+1):
      print("*",end=" ")
    print()

# p2()

# *****
# ****
#  ***
#  **
#  *

# 1st way
# for i in range(5,0,-1):
#   print(i,end=" ")
#   for j in range(1,i+1):
#     print("*", end=" ")
#   print()

# 2nd way
def p3():
  for i in range(1,6):
    for j in range(5-i+1):
      print("*",end='')
    print()


# p3()

# 1
# 12
# 123
# 1234
# 12345
def p4():
  for i in range(1,6):
    for j in range(1,i+1):
      print(j,end='')
    print()

# p4()


# 1
# 22
# 333
# 4444
# 55555

def p5():
  for i in range(1,6):
    for j in range(1,i+1):
      print(i,end='')
    print()

# p5()

# * * * * *
# * * * *
# * * *
# * *
# *
def p6():
  n= int(input("Enter the rows you want: "))
  for i in range(1, n+1):
    for j in range(n-i+1):
      # 1st loop => 1 to 6(5-1+2)->  * * * * *
      # 2nd loop => 1 to 5(5-2+2)->  * * * *
      # 3rd loop => 1 to 4(5-3+2)->  * * *
      # 4th loop => 1 to 3(5-4+2)->  * *
      # 5th loop => 1 to 2(5-5+2)->  *
      print("*", end=" ")
    print()
# p6()


# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
def p7():
  n= int(input("Enter the rows you want: "))
  for i in range(1, n+1):
    for j in range(1, n-i+2):
      # 1st loop => 1 to 6(5-1+2)->  1 2 3 4 5
      # 2nd loop => 1 to 5(5-2+2)->  1 2 3 4
      # 3rd loop => 1 to 4(5-3+2)->  1 2 3
      # 4th loop => 1 to 3(5-4+2)->  1 2
      # 5th loop => 1 to 2(5-5+2)->  1
      print(j, end=" ")
    print()
# p7()

# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

def p8():
  n= int(input("Enter the rows you want: "))
  for i in range(1, n+1):
    for j in range(1, n-i+2):
      # 1st loop => 1 to 6(5-1+2)->  1 1 1 1 1
      # 2nd loop => 1 to 5(5-2+2)->  2 2 2 2
      # 3rd loop => 1 to 4(5-3+2)->  3 3 3
      # 4th loop => 1 to 3(5-4+2)->  4 4
      # 5th loop => 1 to 2(5-5+2)->  5
      print(i, end=" ")
    print()
# p8()

#                 another way

# This does the exact same thing as range(1, n - i + 2)

# for i in range(5, 0, -1):
#     for j in range(1, i + 1):
#         print(*, end=" ")
#     print()



#        *
#      * *
#    * * *
#  * * * *


def p9():
  for i in range(1, 6):
    # printing spaces
    for j in range(1, 6-i+1):
      print(" ", end=" ")

    for k in range(1, i+1):
      print("*", end=" ")
    print()

# p9()



  #         *
  #       * * *
  #     * * * * *
  #   * * * * * * *
  # * * * * * * * * *

#  n = int(input("Enter the number of rows: "))
def p10(n):

    for i in range(1,n+1):
  # printing spaces
        for j in range(i,n+1):
          print(" ",end=" ")

        for k in range(1,i):
          print("*", end=" ")

        for l in range(1,i+1):
          print("*", end=" ")

        print()

# p10(n)

