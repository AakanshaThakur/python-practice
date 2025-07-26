import os
if os.path.exists("C:\\Users\\UseR\\Python_Learnings\\C.txt"):
    os.remove("C:\\Users\\UseR\\Python_Learnings\\C.txt");
    print("File deleted ")
else:
    print("File Not available ")



# f = open(r"C:\Users\UseR\Python_Learnings\A.txt", "x") # this creats new file

# f = open(r"C:\Users\UseR\Python_Learnings\A.txt", "w") # w use for write in file 
# try:
#     with open(r"C:\Users\UseR\Python_Learnings\A.txt") as f2:  # r use for read in file 
#         with open(r"C:\Users\UseR\Python_Learnings\B.txt", "w") as f3:
#             for i in f2:
#                 f3.write(i)
# except:
#     print("file not available");
# else:
#     f2.close()
#     print("File Closed...!")
# f.write("Learning new data in python \nfile handling | exceptions") # write function
# print(f.read(5))
# print(f.readline())

