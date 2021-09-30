import operator
def most_frequent(str):
    n=dict()
    for key in str:
        if key not in n:
            n[key]=1
        else:
            n[key]=n[key]+1

    return n
string=input("Please enter a string: ")
res=most_frequent(string)
sort=dict(sorted(res.items(),key=operator.itemgetter(1),reverse=True))
print(sort) 
