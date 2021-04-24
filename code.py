read_data=[]
l=[]

#read the file and store it as a list
f = open("../demo/sample_input.txt", "r")
i=0
for x in f:
    if x=="\n":
        pass
    else:
        l.append(x[:].strip().split(": "))
        
#convert no. of employee to integer
n=int(l[0][1])

#sorting goodies by their price
for x in range(2,len(l)):
    l[x][1]=int(l[x][1])
for x in range(2,len(l)-1):
    for y in range(3,len(l)-(x-2)):
        if l[y][1]<l[y-1][1]:
            temp=l[y]
            l[y]=l[y-1]
            l[y-1]=temp

min_diff=229900
#max cost of the product is 229900 therefore it is the max diff
for x in range(2,len(l)-n):
    if min_diff>l[x+n-1][1]-l[x][1]:
        min_diff=l[x+n-1][1]-l[x][1]
        index=x

op=""

#printing the output
print("The goodies selected for distribution are:\n")
for x in range(index,index+n):
    op+="{0}: {1}\n".format(l[x][0],l[x][1])
    print(l[x][0],end="")
    print(":",l[x][1])
print("\nAnd the difference between the chosen goodie with highest price and the lowest price is",min_diff)

#open output file to write output
out_file = open("output.txt","w+")

out_file.write("The goodies selected for distribution:\n\n")
out_file.write(op)
out_file.write("\nAnd the difference between the chosen goodie with highest price and the lowest price is {}".format(min_diff))