
def sum_of_even(data):
    # initialize  a variable to store values of sum of even numbers
    sum=0
    # iterate through the list of numbers
    for num in data:
        if num%2==0:
            sum+=num
    return sum




numbers=[1,2,3,4,5,6,7,8,9,10]
result=sum_of_even(numbers)
print('the sum of even number is',result)