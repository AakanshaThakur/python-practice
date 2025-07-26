print("This is a print function");
print(len("something"))

a=11;
b=9;

def calculator(a,b):
    print("addition : ",a+b);
    print("subraction : ",a-b);
    print("multiplication : ",a*b);
    print("division : ",a/b);

calculator(5,8);
calculator(9,7)
# Keyword Arguments
# def greet(firstName, lastName):
    # print("Good morning", firstName, lastName);

# greet(lastName="Thakur",firstName="Akansha"); # Keyword argunm



#default arguments
# def greet(firstName="Guest"):
#     print("Good morning", firstName);

# greet("Aditya");

#variable length arguments
def test(*args): #Keyword args= **args
    print(args);
    print(len(args))
    print(type(args))

test("India", "America", "Sri Lanka");

def function_name(parameter1, parameter2):
    "body"
    "body"
    return value;
