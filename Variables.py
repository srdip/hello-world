#Variables are like container for the code. you can put certain type of code in certain named container. in Python, you can simply
# name anything as veriable except numbers in the begining and assign them by putting "=". However you can put number at the end of 
# the variables or in between.
#example of the variables:
    greetings = ("Hello World")
    print (greeting)

# You can add under_score in fron of variables. you can also input data from user by using simple function called "input". 
# let me show you how you can use both:
    _greeting = input ("How you greet people in your country?")
    print (_greeting)


# Inputing numbers from user and using numbers in your code:
# inputing numbers into your code is different than inputing string to your code. To input number, you need to add "int" for integer or
# full number such as 4, 8, etc. and "float" for decmal or fractional number such as 3.14, 7.9, etc.
# you can convert it while calculating.
# example of taking number input by converting into int from user:
    age = input("what is your age?")
    print = ("You are", int (age) * 365, "days old.") 
    
# you are getting error because in input you put string and trying to print it as number, which is Integers.
# to execute this code convert string into integers first.
# like this
# you can also input floating number by simply putting float instead of int. Let's see how:

work = input ("How long have you worked today: ")
rate = input ("How much you get per hour of work: ")
exchange = input ("What is today's exchange rate: ")
earning = float (work) * float (rate)
bdt = float (earning) * float (exchange)
print ("You earned", earning, "USD &", bdt, "Taka")


#this is s simple calculator for your daily income calculation.
