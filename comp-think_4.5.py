def test1() : # do not change this line!
  list = [4, 5, 1, 9, -2, 0, 3, -5] # do not change this line!
  min1 = list[0]
  min2 = list[1]

  # write your code here so that it sets
  # min1 and min2 to the two smallest numbers
  # be sure to indent your code!
  for item in list:
    if item < min1:
        if min1 < min2:
            min2 = item
        else:
            min1 = item
    elif item < min2:
        min2 = item



  print(min1, min2)
  return (min1, min2) # do not change this line!
# do not write any code below here  

test1() # do not change this line!
# do not remove this line!


def test() : # do not change this or the next line!
  numbers = [11.5, 28.3, 23.5, -4.8, 15.9, -63.1, 79.4, 80.0, 0, 67.4, -11.9, 32.6]
  average = 0

  # write your code here so that it sets average
  # to the average of the non-negative numbers
  # be sure to indent your code!
  sum, count = 0, 0
  for number in numbers:
    if number >=0:
        sum=sum+number
        count=count+1
  average=sum / count



  print(average)
  return average # do not change this line!
  # do not write any code below here  

test()  # do not change this line!
# do not remove this line!