list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
question=int(input('which number do you want to check for?'))
found=False
for i in range (len(list)):
    if list[i]== question:
        print('your number is found in the list at position',(i+1))
        found=True
if found==False:
    print('your number is not found in the list')
    