from pizza import Pizza

f = open("example.in","r")

x = f.readline()
values = x.split(" ")

arr  = []
line = f.readline()
while  line != "":
    ingreds = line.split()
    arr.append(ingreds)
    line = f.readline()


p = Pizza(values[0],values[1],values[2],values[3],arr)
p.print_pizza()
