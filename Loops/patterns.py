#         *****
#         *****
#         *****
#         *****
#         *****

def p1():
  for i in range(1,6):
    for j in range(1,6):
      print("*",end=" ")

    print()

# p1()


#   *
#   * *
#   * * *
#   * * * *
#   * * * * *

def p2():
  for i in range(1,6):
    for j in range(1,i+1):
      print("*",end=" ")
    print()

p2()
