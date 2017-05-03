from difflib import SequenceMatcher,get_close_matches

def similar(a,b):

    a= SequenceMatcher(None,a,b).ratio()
    return str(a*100)+"%"

def close_matching(a,b):
    return get_close_matches(a,b)
print(similar('my name is pankaj','my name is shubham jain')+"%")
print(close_matching('apple',['app','lok','appl','koi']))

lis=['my name is shubham','my name is deepka','shubham','shubham jain']

for a1 in range(0,len(lis)):
    if(a1==(len(lis)-1)):
        break
    firstElement=lis[0]

    secondelemant=lis[a1+1]
    print('diffrence between '+firstElement+' and '+secondelemant+' is ='+similar(firstElement,secondelemant))