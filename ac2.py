a={10,11,12,13,14}
b={"a","b","c","d","e"}
r=list(zip(a,b))
print(r)


a=[10,11,12,13,14]
b=["a","b","c","d","e"]
for x,y in zip(a,b[::-1]):
    print(x,y)