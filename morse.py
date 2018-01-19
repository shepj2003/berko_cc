CODE = {' ': '_', 
	"'": '.----.', 
	'(': '-.--.-', 
	')': '-.--.-', 
	',': '--..--', 
	'-': '-....-', 
	'.': '.-.-.-', 
	'/': '-..-.', 
	'0': '-----', 
	'1': '.----', 
	'2': '..---', 
	'3': '...--', 
	'4': '....-', 
	'5': '.....', 
	'6': '-....', 
	'7': '--...', 
	'8': '---..', 
	'9': '----.', 
	':': '---...', 
	';': '-.-.-.', 
	'?': '..--..', 
	'A': '.-', 
	'B': '-...', 
	'C': '-.-.', 
	'D': '-..', 
	'E': '.', 
	'F': '..-.', 
	'G': '--.', 
	'H': '....', 
	'I': '..', 
	'J': '.---', 
	'K': '-.-', 
	'L': '.-..', 
	'M': '--', 
	'N': '-.', 
	'O': '---', 
	'P': '.--.', 
	'Q': '--.-', 
	'R': '.-.', 
	'S': '...', 
	'T': '-', 
	'U': '..-', 
	'V': '...-', 
	'W': '.--', 
	'X': '-..-', 
	'Y': '-.--', 
	'Z': '--..', 
	'_': '..--.-'}

def encode(sentence):
    sentence = sentence.upper()
    encodedSentence = ""
    for character in sentence:
        encodedSentence += CODE[character] + " " 
    return encodedSentence

#sentence = input("Enter sentence: ")
#encodedSentence = convertToMorseCode(sentence)
#print(encodedSentence)

def encode_to_words(sentence):
    encodedSentence = encode(sentence)
    for character in encodedSentence:
        if character == '-':
            print("Dash")
        elif character == '.':
            print("Dot")
        elif character == ' ':
            print('.')
        elif character == '_':
            print("Space")
            
def decode( morse) :
    DECODE = {v:k for k,v in CODE.items()}
    morse_words = morse.split('_')
    sentence = ''
    for word in morse_words :
        letters = word.split(' ')
        sentence += ''.join([DECODE[l] for l in letters if l != ''])
        sentence += ' '
    return sentence

#sentence = input("Enter sentence: ")
#encodeToWords(sentence)
