""" crypto.py
    Implements a simple substitution cypher
"""
import random

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

key =   "XPMGTDHLYONZBWEARKJUFSCIQV"
new_key = list(key)
random.shuffle(new_key)
alpha = ''.join(new_key)

def main():
  keepGoing = True
  while keepGoing:
    response = menu()
    if response == "1":
      plain = input("text to be encoded: ").upper()
      print (encrypt(plain))
    elif response == "2":
      coded = input("code to be decyphered: ").upper()
      print (decrypt(coded))
    elif response == "0":
      print ("Thanks for doing secret spy stuff with me.")
      keepGoing = False
    else:
      print ("I don't know what you want to do... You entered: " + str(response))
  

#Create menu function
def menu():
  print("SECRET DECODER MENU: \n")
  print("0) Quit")
  print("1) Encode")
  print("2) Decode")
  action = input("What do you want to do? ")
  return action

#Create Encrypt function
def encrypt(message):
 encrypted = ""
 letter_loc = 0
 
 for letter in (message):
   letter_loc = alpha.find(letter)
   encrypted += key[letter_loc: letter_loc + 1]
 return encrypted
 
#Create Decrypt function
def decrypt(message):
    decrypted = ""
    letter_loc = 0
    
    for letter in (message):
        letter_loc = key.find(letter)
        decrypted += alpha[letter_loc: letter_loc + 1]
    

#Decrypt password: coder___________________________
    keepGoing = True
    tries = 2
    while (keepGoing):
      password = input("What is the password to decrypt this message? ")

      if password.upper() == "CODER":
        return decrypted
        keepGoing = False
      elif tries == 0:
        print("You've guessed incorrectly to many times. You can't decrypt this.")
        keepGoing = False
      elif password.upper() != "CODER":
        print("Wrong")
        tries -= 1
      
        
#-------------------------------------------------------------------------------
main()
