# Q1/

x = "Hello world!"
print(x.replace("w",""))

# Q2/

Number_1 = int(input("first number: "))
Number_2 = int(input("second number: "))

for num in range(Number_1, Number_2):
      if num > 1:
               for i in range(2,num):  
                    if (num % i) == 0:
                         break
               else:
                   print(num)

#Q3/
def counting():
      string = input("Enter any string: ")
      character = input("Enter the character: ")
      count = 0
      for i in string:
           if i == character:
                 count+= 1
      return print("The count is :",count)   

counting()