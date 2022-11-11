x, y, z = True, False, True
if x and y and z:
  print ("Apple")
elif x and z:
  print("Banana")
elif z:
  print ("Pear")
 
a, b = 25, 4
if a > 0 and  b > 0 :
    sum = a + b
    print(sum)
else: 
    prod = a * b
    print(prod)
print("done")

plan = 'M' # ‘M’ = monthly, ‘D’ = daily
hours = 35
student = True
senior = False
total = 0

# write the code to calculate the total below
if plan=='M':
    total = total +30
    total = (hours * 3) + total
else:
    total=hours*10

if student or senior:
    total = total*.9

print('total fee: ',total)

x, y, z = True, False, True
if x and y and z:
  print ("Apple")
elif x and z:
  print("Banana")
elif z:
  print ("Pear")
  