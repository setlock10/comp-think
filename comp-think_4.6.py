def verify(number) : # do not change this line!

  # write your code here so that it verifies the card number
  test3=0
  for x in number:
     if x!="-":
        test3=test3+int(x)
 
  test4 = (int(number[0])*10+int(number[1])) + (int(number[7])*10+int(number[8]))
  
  
  # be sure to indent your code!
  if number[0]!='4':
    return 1

  if int(number[3])!=int(number[5])+1:
    return 2

  if  test3%4!=0:
    return 3

  if test4!=100:  
    return 4 
  else:
    return True # modify this line as needed

input = "4094-3460-2754" # change this as you test your function
output = verify(input) # invoke the method using a test input
print(output) # prints the output of the function
# do not remove this line!
