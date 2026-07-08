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

p1()


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

p2()

# *****
# ****
#  ***
#  **
#  *

def p3():
  for i in range(1,6):
    for j in range(5-i+1):
      print("*",end='')
    print()


p3()
