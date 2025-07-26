var={10,'nhn',45,True,'nhn', 56.7}
print(type(var))
var.add("Learn") #add method
var.update(["Learn", "coding"]) #update method is used when we need to insert more than one value

print(var.pop()) #pop method deletes the item
var.remove("nhn"); #remove deletes the particular item
var.clear()
print(var)



var1={10,95,True,'nhn', 56.7}
var2={10,'nhnmjm',95,False,'jjh', 56.79}

print(var1.union(var2)) # union method gives you unique value
print(var1.intersection(var2)) # intersection method gives you common values
print(var1 & var2) #operator using & intersection
print(var1 | var2 ) # operator using | union
print(var1.difference(var2)) # difference gives you only new values from both var1,2
print(var1-var2) #operator using - difference
print(var1.symmetric_difference(var2)) # symmetric_difference gives you unique valuse from both the var1,2
