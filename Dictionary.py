import mysql.connector
import enchant
from textblob import TextBlob

search = True

d = enchant.Dict("en_US")

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

def definition(word):
    cursor = con.cursor()

    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word )
    results = cursor.fetchall()

    word = word.lower()
    if results:
        for word in results:
            print(word[1])

while True:
    user_input = input('Insert a word: ')
    d = enchant.Dict("en_US")

    if d.check(user_input) == True:
        word = user_input
        definition(word)

    if d.check(user_input) == False:
        checked = TextBlob(user_input)
        yn = input(f"did you mean: {checked.correct()}? Enter Y if yes or N if no: ").upper()
        if yn == 'Y':
            word = checked.correct()
            definition(word)
        elif yn == 'N':
            print('word doesnt exist. Please double check it.')

    new_search = input("Would you like to search another word? Enter 'Y' or 'N' ").upper()

    if new_search == 'Y':
        search=True
        continue
    else:
        print("Thanks for using our Dictionary!")
        break
