my_list = [7, 6, 5, 4, 3, 2, 1]
my_list.pop(2)
my_list.sort() # this puts the elements in increasing order
my_list.remove(4)
print(my_list)

def test() : # do not change this line!
  values = [4, 7, 8, 9, -5] # do not change this line!
  
  # write your code here so that it modifies values
  if values[-1]<0:
    values.pop(-1)
  values.insert(1,(values[0]+values[1])/2)

  values.insert(len(values),values[0])
  values.pop(0)

  values.insert(0,values[-2])
  values.pop(-2)



  
  # be sure to indent your code!

  print(values)
  return values # do not change this line!
# do not write any code below here  

test()  # do not change this line!
# do not remove this line!
