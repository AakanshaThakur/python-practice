var={"Name" : "Aakansha", "age" :23, "Password":"Aakansha1234"}
print(var.keys()) # this gives you all the keys present there
print(var.values()) # this gives you all the keys present there
print(var.items()) # item method gives you both key and value pairs
for key, values in var.items():
    print(key,values, sep= ":") # using for loop

var["age"]=50; # we can update values like this also
print(var)
var.clear() # Clear method clears all the values
print(var.get("Password")) # get method gives you the value
print(var)
var.pop("Name"); # pop deletes the key
print(type(var))
print(var["age"]) # we can access the value through this



