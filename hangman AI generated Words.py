import random

from ollama import chat
from ollama import ChatResponse
import re

#ADD HINT OPTION 
'''
would work by randomly selectinga  letter from the work then checks if its in letters[](chceking if its already a guess letter).
if not then ittl add the letter to letters[] which would refect the added letter on the screen'''

letters = []
trys = 7
word = ''
definition = ''

def getWord():
    global definition, word
    pattern = r"^[A-Z][a-z]+: .+$" #pattern 'word:sentence' eg book: used to keep notes
    
    #prompts llm to get a response 
    def getAIresponse() -> str:
        response: ChatResponse = chat(model='llama3', messages=[
            {
                'role': 'user',
                'content': "for a hangman game, Respond only in the following format: 'noun:description'. "
                            "Do not include any other text, explanations, or context. For example:\n"
                            "Cat: A small domesticated carnivorous mammal.\n"
                            "Computer: An electronic device for storing and processing data.\n"
                            "Provide a response strictly in the format 'noun: description'.",
            },
        ])
        
        return response.message.content
    
    
    
    while True:
        response = getAIresponse()
        
        #checks if the response that was givem by the ai was given in the correct format (refer to pattern variable)
        if re.search(pattern, response):
            word, definition = response.split(":")
            word = word.lower() #need a to be lower in oerder to properly compare when validating entries made
            definition = definition.strip()# removes space before definition
            return
            

def outputWord():
    global word
    
    print(definition)
    
    if not letters: #if no correct letters were entered
        [print("_", end=" ")for i in word]
        print()
        return
        
    #prints the spaces and letters entered
    for i in range(len(word)):
        if word[i] in letters:
            print(word[i], end=" ")
        else:
            print("_", end=" ") 
        
    print()
 
def validate(guess):
    global trys
    
    if len(guess) != 1 or not guess.isalpha():
            print("\nPLEASE ENTER A VALID LETTER.")
                
    if guess in word and guess not in letters:
        letters.append(guess)
    else: trys -= 1
    
    if all(letter in letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word.upper()}\n")
            reset()
            return
        
def reset():
    global word, letters, trys
    getWord()
    letters = []
    trys = 7

def start():
    reset()
    
    while(True):
        if trys <= 0:
            print("GAME OVER! The word was:", word)
            reset()
        
        print(f"trys left: {trys}")    
        outputWord()
        
        guess = input("\n[CNTRL + C to end Program] Enter a letter: ").strip().lower()
           
        validate(guess)
        
        
start()   
    

    