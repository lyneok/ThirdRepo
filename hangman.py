## ASCII pics for the noose.
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


#print(HANGMAN_PICS)
#[print(pic) for pic in HANGMAN_PICS]

assert len(HANGMAN_PICS) == 7, 'must have 7 noose pics'


WORDS = 'snake zombie sphinx vaporize unknown rhythm xylophone strength oxygen luxury jogging awkward subway equip buffalo jinx pajamas wristwatch zodiac queue wizard puppy kiwifruit fluffy jawbreaker'.split(',')
print(f"Words: {WORDS}")



