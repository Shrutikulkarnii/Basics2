import sys
import os

def seperate():
    check = []
    for a in sys.argv[:]:
        for part in a.split(","):
            if part.strip():
                check.append(part.strip())
    return check

def traverse(p):
    for roots,d_names,f_names in os.walk(p):
        print(roots,d_names,f_names)

def main():
    check=seperate()
    for i in range(1,len(check)):
        print("\n")
        print(f"Path name: {str(check[i])} ")
        if os.path.exists(check[i]):
            print("Path exists.")
        else:
            print("Given path does not exist. Enter a valid path!!!!")
            continue
        print(f"Is it a file?: {str(os.path.isfile(check[i]))} ")
        print(f"Is it a link?: {str(os.path.islink(check[i]))} ")

        if os.path.isdir(check[i]):
            print("It is a directory")
            p=check[i]
            l=traverse(p)
        else:
            print("It is not a directory. Enter a valid directory name!!")
        print("\n")


if __name__== "__main__":
    main()
    sys.exit(0)
