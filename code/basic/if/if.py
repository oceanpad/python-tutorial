age = input('please input your age(int):')
try:
   age = int(age)
   if age > 18 :
       print("adult")
   elif age < 6 :
       print("children")
   else :
       print("teenage")
except ValueError:
   print("'" + age + "' is not an int!")
