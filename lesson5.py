#bubble sort
#list=[1,3,2,4,6,5,8,7,10,9]
list=[5,10,2,7,12,1] 
t=0
for x in range(len(list)):
    for i in range(len(list)-1):
        if list[i]>list[i+1]:
            t=list[i+1]
            list[i+1]=list[i]
            list[i]=t
print(list)