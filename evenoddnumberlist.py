
def check_even_odd(data):
    even_numbers=[]
    odd_numbers=[]

    for num in data:
        if num%2==0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    return even_numbers,odd_numbers




numbers=[1,2,3,4,5,6,7,8,9,10]
even,odd=check_even_odd(numbers)
print('Even numbers list',even)
print('Odd numbers list',odd)