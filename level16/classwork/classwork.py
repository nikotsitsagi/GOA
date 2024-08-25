#1)
def greeting():
    return "hello world!"
print(greeting())
#2)
def greeting_by_name():
    return f"hello {name}"
name = input("enter your name here: ")
print(greeting_by_name())
#3)
def two_numbers(x , y):
    return x * y
result = two_numbers(5,2)
print(result)
#4)
def three_numbers(a , b , c):
    return a + b + c
result = three_numbers(1,2,3)
print(result)
#5)
def person_age(age):
    if age >= 18:
        return "you are an adult"
    else:
        return "you are a child"
    age = input("enter your age here: ")
    print()
    

