import random

letters = []
trys = 7
word = ""

mylist = {
    "mouse":"A computer input device",
    "violin":" A musical stringed instrument",
    "storm":"A type of weather phenomenon characterized by heavy rain and strong winds",
    "nitros":"A type of chemical compound that contains nitrogen and oxygen atoms and can be directly injected into the air intake to make more POWER",
    "eclipse":"A type of astronomical event where the moon passes between the Earth and the sun",
    "arthritis":"A type of medical condition characterized by inflammation and pain in the joints",
    "nostalgia":"A sentimental longing or wistful affection for the past, typically for a period of time when one was happy",
    "promiscuous":"Engaging in sexual relations with many people; having no strong emotional attachment to any one person; willing to have sex with anyone",
    "pen":"A writing instrument used to apply ink to paper or other surfaces.",
    "chair":"A piece of furniture with a flat surface and four legs, typically used for sitting.",
    "Sunflower":"A tall plant that produces large yellow flowers and is often grown for its edible seeds.",
    "martin":"A person who's never cooked in the house"
}

def getWord():
    return random.choice(list(mylist))

def outputWord():
    print(mylist[word]) #prints definition
    
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
 
def validate(letter):
    global trys
    
    if len(guess) != 1 or not guess.isalpha():
            print("\nPLEASE ENTER A VALID LETTER.")
                
    if letter in word and letter not in letters:
        letters.append(letter)
    else: trys -= 1
    
    if all(letter in letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word.upper()}")
            reset()
            return
        
def reset():
    global word, letters, trys
    word = getWord()
    letters = []
    trys = 7

def start():
    global word, trys, guess
    word = getWord()
    
    while(True):
        if trys <= 0:
            print("GAME OVER! The word was:", word)
            reset()
        
        print(f"trys left: {trys}")    
        outputWord()
        
        guess = input("\n[CNTRL + C to end Program] Enter a letter: ").strip().lower()
           
        validate(guess)
        
start()
    