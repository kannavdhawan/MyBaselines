def numDuplicates(name, price, weight):
    q=[]
    counter=0
    for a,b,c in zip(name,price,weight):
        x=(a,b,c)
        q.append(x)
    l=len(q)
    w=set(q)
    e=len(w)
    return (l-e)
print(numDuplicates(['ball','bat','glove','glove','glove'],[2,3,1,2,1],[2,5,1,1,1]))