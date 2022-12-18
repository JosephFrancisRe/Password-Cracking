import time
from hashlib import sha256

# Initialize starting timestamp to use in statistical analysis
starting_timestamp = time.time()

# Initialize and encode the salt in utf-8
salt = '000000000000000000000000000078d2'.encode('utf-8')

# Initialize a desired hash variable containing the sha256 encrypted password for the admin account
desiredHash = '18821d89de11ab18488fdc0a01f1ddf4d290e198b0f80cd4974fc031dc2615a3'

# Helper function to print the relevant statistics associated with the password cracking
def printStats(starting_timestamp, guesses):
    print(f'\n**********\n')
    print(f'Statistical Overview of Password Crack')
    print(f'--------------------------------------')
    print(f'Total number of Guesses: {guesses}')
    print(f'Total elapsed time: {time.time() - starting_timestamp} seconds')
    print(f'Guesses per second: {guesses / (time.time() - starting_timestamp)} guesses')
    print(f'\n**********\n')

# Open wordlist and consider it as a wordbank containing each potential crack option.
# For loop through the wordbank to locate potential cracks that match the desired hash when encrypted using SHA256.
# If a match is found print the statistics as well as the plain text version of the password.
with open('wordlist.txt', mode='r', encoding='ISO-8859-1') as wordbank:
    guessCount = 0
    for potentialcrack in wordbank:
        # Increment the guessCount for every word checked in the wordlist.
		# Also use list indexing to ignore the new line character at the end of every line of wordlist.
        guessCount += 1
        potentialcrack = potentialcrack[:-1]

        # Create hash object that will encode each potential crack in the wordbank using SHA256
        hashObject = sha256()
        hashObject.update(salt)
        hashObject.update(potentialcrack.encode('utf-8'))

        # Compare the hex value of the hash object to the desired hash to determine if a match exists.
		# If a match exists, ultimately print the decrypted plain text value of the password.
        if hashObject.hexdigest() == desiredHash:
            printStats(starting_timestamp, guessCount)
            correctHashObjectHexDigest = hashObject.hexdigest()
            print(f'The password has successfully been cracked!')
            print(f'The encrypted hash is: {correctHashObjectHexDigest}')
            print(f'The decrypted password is: {potentialcrack}')
            break