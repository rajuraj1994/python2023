import pandas as pd

d={
    'fruits':['apple','mango','cherry'],
    'calories':[100,50,70]
}
result=pd.DataFrame(d)
print(result)

# pandas version
print(pd.__version__)


# Series : means column in table
a=[1,2,3,4,5]
result=pd.Series(a)
print(result)

# labels in series 
result=pd.Series(a,index=['a','b','c','d','e'])
print(result)


# DataFrame
d={
    'fruits':['apple','mango','cherry'],
    'calories':[100,50,70]
}
test=pd.DataFrame(d)
print(test)
print(test.loc[1])
print(test.loc[[0,1]])

b=pd.DataFrame(d,index=['Sunday','Monday','Tuesday'])
print(b)
print(b.loc['Tuesday'])