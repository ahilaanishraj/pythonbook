
num = int(input("Enter the total number of tuple:"))
val = ()
for i in range(num):
    a=int(input("Enter the value:"))
    val+=(a,)

print("original tuple:",val)       
Po = ( )
for i in val:
	if i > 0:
		Po += (i, )
		
print("Positive Numbers: ", Po)
