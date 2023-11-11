message = "hello whassup how is it going".split()
print(message[0]) #hello
message = "hello whassup how is it going"
print(message[0]) #h

my_list =["bir",2,3.1]
my_list[-2:]=["yeni,eklentiler"]
print(my_list)

numbers=[2,3,4,5,46,57,8,5]
numbers.append(49)#sona 49
numbers.insert(1,"yeni")#yeni 
numbers.insert(len(numbers),"yeni")
numbers = "yeni" in numbers #yeni varmı
str = "asf,sadf"
numbers = str.split(",")

print(numbers)
