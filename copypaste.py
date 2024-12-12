import file1


try:
    path = input("Which file you want to read: ")
    data = file1.read_data(path)
    print(data)
    
except FileNotFoundError as e:
    print("Check the path again")


try:
    path = input("Where you want to write: ")
    content = input("Which file you want to paste: ")
    file1.write_data(path,file1.read_data(content))
    print("successfully Written")

except FileNotFoundError as e:
    print("Check the path again")