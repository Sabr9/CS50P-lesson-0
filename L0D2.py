""""
name = input("What's your name? ")
print("hello,")
print(name)
"""
#The above code print the side effect line by line, this below code will stop it, then iut started to print in a string format
#overriding the default value
"""
name = input("What's your name? ")
print("hello,")
print(name)
"""
# I don't like the way the side effect gives me a 2 lines prompt, 
#authomatically print function create a new line, so how do i stop that?
"""
name = input("What's your name? ")
print("hello, ",end="")#This end argument made it string
print(name)
"""
#using sep="" parameters to override(remove) blank
name = input("What's your name? ")
print("hello,",name,sep="")
