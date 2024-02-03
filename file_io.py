#use Python open 

test_file = open(file="./test_file.txt",mode="r",buffering=-1,encoding="utf-8")
content = test_file.read()
print(content)

#open file must closed!
test_file.close()

#use with => much better 
with open("./test_file.txt","a+") as input_file:
    input_file.write("\nhello test file this is Python")
    
with open("./test_file.txt","r") as test_file:
    print(test_file.read())
    