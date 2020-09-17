# Author: Cole Carter ctc5367@psu.edu
# Collaborator: eric zhang ecz5032@psu.edu
# Collaborator: Andrew Wang aqw5628@psu.edu
# Collaborator: Ryan Attia rka5347@psu.edu
# Section: 5 
# Breakout: 14

def sum_n(n):
  if n > 0:
    return  n + sum_n(n-1)
  else:
    return 0
    
def print_n(s, n):
  if n > 0:
    print(s)
    print_n(s, n-1)

def run():
  num = input("Enter an int: ")
  num = int(num)
  print(f"sum is {sum_n(num)}.")

  s = input("Enter a string: ")
  print_n(s, num)

if __name__ ==  "__main__":
  run()