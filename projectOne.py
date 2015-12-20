import re
import sys
import math


fp = open(sys.argv[1])
c = fp.readline()
c = fp.readline()
mainArray = []

#read input
while c != '':
  c = fp.readline()
  if c == '':
    break
  mainArray.append(c.split(','))

everything = {}
totalSet = []
theAverages = []
usableDataArray = []
totalSetCounter = 0;

#convert input to floats
for i in range(len(mainArray)):
  usableDataArray.append([])
  for j in range(len(mainArray[i]) - 2):
    usableDataArray[i].append(float(mainArray[i][j + 2]))

#normalize measurements
rotated = list(zip(*usableDataArray[::-1]))
for j in range(len(rotated)):
  maxNum = max(rotated[j])
  minNum = min(rotated[j])
  for k in range(len(rotated[j])):
    if(maxNum != minNum):
      usableDataArray[k][j] = (usableDataArray[k][j] - minNum)/(maxNum - minNum)

#build the three dementional array
last = -1
for i in range(len(usableDataArray)):
  #print(i)
  if(last != int(mainArray[i][1])):
    last = int(mainArray[i][1])
    totalSet.append([])
  totalSet[int(mainArray[i][1])].append(usableDataArray[i])

#Sum the rows together
for i in range(len(totalSet)):
  theAverages.append(list(map(sum , zip(*totalSet[i]))))

  
answer = -1
averages = []
correct = []
total = []
change = -1
#calulate the average for each data point
for i in range(len(usableDataArray)):
  smallest = -1
  #sum the rest of the data points up and find which group is closest to the data set
  for j in range(len(theAverages)):
    c = [a - b for a, b in zip(theAverages[j], usableDataArray[i])]
    c = [x / (len(totalSet[j])-1) for x in c]
    sumTotal = 0
    for x in range(len(c)):
      sumTotal += (c[x] - usableDataArray[i][x]) * (c[x] - usableDataArray[i][x])
    if sumTotal < smallest or smallest == -1:
      smallest = sumTotal
      answer = j
  #Switch to a new correct and total if the number changed
  if(int(mainArray[i][1]) != change):
    change = int(mainArray[i][1])
    correct.append(0)
    total.append(0)
  #record wheather it was correct and display the numbers
  if(int(mainArray[i][1]) == answer):
    correct[int(mainArray[i][1])] += 1
  total[int(mainArray[i][1])] += 1
  if (int(mainArray[i][1]) != answer):
    print(mainArray[i][0] + ',' + mainArray[i][1] + ',' + str(answer) + ',*')
  else:
    print(mainArray[i][0] + ',' + mainArray[i][1] + ',' + str(answer))
  

for i in range(len(total)):
  print(str(i) + ',' + str(total[i]) + ',' + str(100.0 * correct[i] / total[i]) + "\n")

sys.stdout.flush()
