#Assigment  of calculator
#we define function
#we pass parametter in parenthasis

#value return
#pass argument
#last we call the function

def calculator(num1,num2,operater):
   if operater == "+":
      return num1 + num2
   elif operater == "-":
      return num1 - num2
   elif operater == "*":
      return num1 * num2
   elif operater == "/":
      if num2 ==  0:
       return "division by zero is not allowed"
      return num1/num2
   else:
      return "invalid syntex"
num1 = float (input('Enter your first number; '))  
num2 = float (input('Enter your Second number; '))
operator=input("Enter your operator; ")
result = calculator(num1, num2, operator)
print(result) 