# filter function returns an iterator yielding those items of iterable for which function(item) is true.Meaning you need to filter by a function that returns either True or False.

def check_even(num):
    return num%2==0


numbers=[1,2,3,4,5,6,7,8,9,10]
result=list(filter(check_even,numbers))
print(result)