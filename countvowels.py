
def count_vowels(word):
    vowels=set('AEIOUaeiou')
    vowel_count=0

    for letter in word:
        if letter in vowels:
            vowel_count+=1
    return vowel_count


text="Welcome"
result=count_vowels(text)
print('Numers of vowels in',text,'is',result)