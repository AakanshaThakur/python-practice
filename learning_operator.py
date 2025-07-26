a =11 # arithmatic operations
b=14
print(a+b) # add
print(a-b) #subract
print(a*b) #multiply
print(a/b) #division
print(a//b) # modular
print(a**b) #power

a=9 # relational operator
b=28
print(a<b) # less than       #ture
print(a>b) #greater than     #false
print(a<=b) #less than =     #true
print(a>=b) #greater than =  #false
print(a==b) # ==             #false
print(a!=b) #not eqaul to    #true

# Logical operator
a = 13
b=2
print(a<b and a>b) # false
print(a>b or a<b)  #true
print(not(a<b and a>b)) #true

#Bitwise Operator
print(5 & 6) # bitwise & # op: 4
print(5 | 6) # bitwise | #op:7
print(5^6)   #bitwise ^XOR #op: 3
print(~6) # bitwise complement op:-7
print(15>>1) # bitwise right shift # op:7
print(15<<1) # bitwise left shift # op:30

# Assignment operator
a=5
print(a)

''' Special operator :> 1) identity operator : it checks if 2 id values are same or not
(is, is not)
2) membership operator (in , not in)
'''

a =5
b= 8
print(a is b) #false
print(a is not b) #true
print("id of a: ", id(a))
print("id of b: ", id(b))

var = "India is great"
print("great" in var) # true
print("hello" not in var) # true