import os
def traverse(p):
    for roots,d_names,f_names in os.walk(p):
        print(roots,d_names,f_names)
p=input("Enter the path: ")
l=traverse(p)
print(l)
