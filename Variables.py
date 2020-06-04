#Variables are like container for the code. you can put certain type of code in certain named container
#example of the variables:
# you can also input data from user by using simple function called input. let me show you how.
# There are some variable naming rule. You can not put number in front of Variables. However you can put number at the end of the variables or in between.
    # You can add under_score in fron of variables.
    # An example could be:

# Inputing numbers from user and using numbers in your code:
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
