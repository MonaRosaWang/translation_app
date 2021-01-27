import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
    user = 'ardit700_student',
    password = 'ardit700_student',
    host = '108.167.140.122',
    database = 'ardit700_pm1database'
)
cursor = con.cursor()
word = input('Enter a word: ')
query = cursor.execute("SELECT * FROM Dictionary")#fetch all date on sql database
results = cursor.fetchall()
#print(type(results))

def Convert(tup, di): 
    for a, b in tup: 
        di.setdefault(a, []).append(b) 
    return di 
dictionary = {}      
results = Convert(results, dictionary)


if word in results:
    print(results[word])
elif len(get_close_matches(word, results.keys()))>0:
        yn=input('Did you mean %s instead? Enter Y if yes or N if no' %get_close_matches(word, results.keys())[0])
        if yn=='Y':
            print (results[get_close_matches(word, results.keys())[0]])
        elif yn=='N':
            print ('Please double check your input!')
        else:
            print ('We don\'t understand your input!')
else:
        print ('The word does not exist, Please input a valid one')