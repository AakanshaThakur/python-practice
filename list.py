list1=[]; # Empty List
list2=[11, 'ASN', True, 11.9, "ART", 11]
print(list2[1:4]); #Slicing
print(list2[1]); #Indexing
print(list2.count(11)); #count
print(list2.index(11)); #IndexPosition
print(list2.index(11,1)); #means leave 1st time and tell me the whenever you got it next time

list2.insert(2, "AAKANSHA"); #insert method to add item
print(list2)

list2.pop(2); # Pop deletes the item in the list
print(list2);

list3= list(); #list function

list4=["Aaku", "Govu"];
list2.extend(list4) #extend this can extend your list further
print(list2);

list4=list2.copy(); # copy this copys the content of list to other list
list4=list2[:]; # another way to copy
print(list4);

list22=[25,11,59,78,32,10];
list22.sort(reverse=True); # to sort in desending order
print(list22);

list22.reverse() #reverse method to reverse the list
print(list22);

list5 = [25,11,59,78,32,10,["ASN",["Shree"]]]; # This is nested list 
print(list5);

list6=["Hello", "Askk","Rohit","Ankit","World"];
f=[word for word in list6 if word.startswith("Ank")] #Comprehensive 
print(f);

list7=["Amkush", "Ankit"];
n1,n2=list7; #List unpacking
print(n2);