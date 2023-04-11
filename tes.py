test = [[0 for i in range(3)] for i in range(10)]
with open("user.csv") as f:
  reader = f.readlines()
  i = 0
  for line in reader :
    test[i] = line
    i += 1
  print(test)


def itung(line):
  count = 0
  i = 0
  j = 0
  while line[i][j] != "\n" :
    count +=1
    j += 1
  return count



  



    