## ASCII pics for the noose.
# Data
HANGMAN_PICS = [
	'''
  +---+
      |
      |
      |
     ===''',

  '''
  +---+
  0   |
      |
      |
     ===''',
        
  '''
  +---+
  0   |
  |   |
      |
     ===''',

  '''
  +---+
  0   |
 /|   |
      |
     ===''',
  '''
  +---+
  0   |
 /|\  |
      |
     ===''',
        
  '''
  +---+
  0   |
 /|\  |
 /    |
     ===''',
        
  '''
  +---+
  0   |
 /|\  |
 / \  |
     ===''']

WORDS = 'snake zombie sphinx vaporize unknown rhythm xylophone strength oxygen luxury jogging awkward subway equip buffalo jinx pajamas wristwatch zodiac queue wizard puppy kiwifruit fluffy jawbreaker'.split(' ')


# Functions

def getRandomWord():
    import random
    idx = random.randint(0, len(WORDS)-1)
    return WORDS[idx]

# Count the number of different letters in a word
def count_letters_in_(word):
    return len(set(word))

def test():
    assert len(HANGMAN_PICS) == 7, 'must have 7 noose pics'
    print(f"Random word: {getRandomWord()}")
    assert count_letters_in_("aassacdee") == 5, "this word has 5 letters!"
    print(f"Words: {WORDS}")


## Program 

print('HANGMAN')
print ('You are about to start playing...')