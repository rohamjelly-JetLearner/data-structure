howlongdidittakeforgta6tocomeout=[1,22,34,35,56,72,72,86,94,101,131,142,153]
gta6yearsguess=int(input(str(howlongdidittakeforgta6tocomeout) + '\n which number do you want to choose\n'))
endpos=len(howlongdidittakeforgta6tocomeout)-1
startpos=0
while startpos<=endpos:
    mid=(startpos+endpos)//2
    midval=howlongdidittakeforgta6tocomeout[mid]
    if midval==gta6yearsguess:
        print('Your number is in the list at position', mid+1) 
        break
    elif midval>gta6yearsguess:
        endpos=mid-1
    elif midval<gta6yearsguess:
        startpos=mid+1
if startpos>endpos:
    print('Your number is not in the list')
    