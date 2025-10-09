a=input("Ente text to write to the file: ")
with open("output.txt","w") as file:
    file.write(a+"\n")
print("Data successfully written to output.txt")
b=input("Enter additional text to append: ")
with open("output.txt","a") as file:    
    file.write(b+"\n")
print("Data successfully appended")
print("Final content of output.txt:")
for line in open("output.txt","r"):
    print(line.strip())