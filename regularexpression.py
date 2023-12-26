# regex/regular expression : it is a sequence of characters that forms a serch pattern and it is also used to check if a string contains the specified pattern. for example : if ypu want to check the password pattern then there should be certain no of characters or capital letter or lowercase letter etc

import re

text= "Winter 2023 is starting in Nepal"
test=re.search("^Winter.*Nepal$",text)
if test:
    print('matched')
else:
    print('not match')

# regex functions 
#  findall -> return the list containing all matches
#  search ->  return the match object if there is a match 
#  split -> returns the list where the string has been split each time

# metacharacters
# []  A set of characters eg: [a-p]
test= re.findall("\d",text)
print(test)

# \  signals a special sequence  eg : \d then it will return the digits
# ^ starts with  '^test'
# $ ends with  'bye$'
# * zero or more occurances
# + one or more occurances
# ? zero or one occurance
# {} exactly the number of occurances  eg: 'he.{2}o'


 
