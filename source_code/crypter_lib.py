

#dictionary for encoding and tree for decoding
global morse_tree, morse_dict

# making a list of morse code with respect to characater 
morse_codes = [('A', '.-'),
    ('B', '-...'),
    ('C', '-.-.'),
    ('D', '-..'),
    ('E', '.'),
    ('F', '..-.'),
    ('G', '--.'),
    ('H', '....'),
    ('I', '..'),
    ('J', '.---'),
    ('K', '-.-'),
    ('L', '.-..'),
    ('M', '--'),
    ('N', '-.'),
    ('O', '---'),
    ('P', '.--.'),
    ('Q', '--.-'),
    ('R', '.-.'),
    ('S', '...'),
    ('T', '-'),
    ('U', '..-'),
    ('V', '...-'),
    ('W', '.--'),
    ('X', '-..-'),
    ('Y', '-.--'),
    ('Z', '--..'),
    ('0', '-----'),
    ('1', '.----'),
    ('2', '..---'),
    ('3', '...--'),
    ('4', '....-'),
    ('5', '.....'),
    ('6', '-....'),
    ('7', '--...'),
    ('8', '---..'),
    ('9', '----.'),
    (',', '--..--'),
    ('.', '.-.-.-'),
    ('?', '..--..'),
    (';', '-.-.-.'),
    (':', '---...'),
    ('\'', '.----.'),
    ('-', '-....-'),
    ('/', '-..-.'), 
    ('(', '-.--..'),
    (')', '-.--.-'),
    ('_', '..--.-'),
    ('+', '...-.'),
    ('&', '..-..'),
    ('*', '..-.-'),
    ('^','..--'),
    ('#','..--.'),
    ('=','.-...'),
    ('%', '.-..-'),
    ('@','-.....'),
    ('!','.-..-.'),
    ('$','-.-..'),
    ('\\', '-.--.'),
    ('<', '---.-.'),
    ('>', '---.--'),
    ('{', '----..'),
    ('}', '----.-'),
    ('[', '-----.'),
    (']', '------'),
    ('\"', '----'),
    ('a', '---.-'),
    ('b', '---..-'),
    ('c', '.-..--'),
    ('d', '.-.-'),
    ('e', '.-.-.'),
    ('f', '.-.--'),
    ('g', '.-.-..'),
    ('h', '.-.--.'),
    ('i', '.-.---'),
    ('j', '.---.'),
    ('k', '.--..'),
    ('l', '.--.-'),
    ('m', '.-----'),
    ('n', '-...-'),
    ('o', '-..--'),
    ('p', '-.-.-'),
    ('q', '-.-.--'),
    ('r', '--....'),
    ('s', '--...-'),
    ('t', '-.---'),
    ('u', '-.---.'),
    ('v', '-.----'),
    ('w', '--.-.'),
    ('x', '--.--'),
    ('y', '--.--.'),
    ('z', '--.---'),
    ('~', '--.-..'),
    ('`', '--.-.-'),
    ('\n','---.'),
    ('\t', '--..-')]

morse_dict = dict(morse_codes)  

# Defining and making the morse_tree from the above dictionary

class Tree:
  def __init__(self, char='', left=None, right=None):
    self.char = char
    self.left = left
    self.right = right



morse_tree = Tree('',
                Tree('E',
                     Tree('I',
                          Tree('S',
                               Tree('H',
                                    Tree('5'),
                                    Tree('4')),
                               Tree('V',
                                    Tree('+'),
                                    Tree('3'))),
                          Tree('U',
                               Tree('F',
                                    Tree('&'),
                                    Tree('*')),
                               Tree('^',
                                    Tree('#',
                                    	Tree('?'),
                                        Tree('_')),
                                    Tree('2')))),
                     Tree('A',
                          Tree('R',
                               Tree('L',
                                    Tree('='),
                                    Tree('%',
                                    	Tree('!'),
                                        Tree('c'))),
                               Tree('d',
                                    Tree('e',
                                    	Tree('g'),
                                        Tree('.')),
                                    Tree('f',
                                        Tree('h'),
                                        Tree('i')))),
                          Tree('W',
                               Tree('P',
                                    Tree('k'),
                                    Tree('l')),
                               Tree('J',
                                    Tree('j'),
                                    Tree('1',
                                    	Tree('\''),
                                    	Tree('m')))))),
                Tree('T',
                     Tree('N',
                          Tree('D',
                               Tree('B',
                                    Tree('6',
                                    	Tree('@'),
                                    	Tree('-')),
                                    Tree('n')),
                               Tree('X',
                                    Tree('/'),
                                    Tree('o'))),
                          Tree('K',
                               Tree('C',
                                    Tree('$'),
                                    Tree('p',
                                    	Tree(';'),
                                    	Tree('q'))),
                               Tree('Y',
                                    Tree('\\',
                                    	Tree('('),
                                    	Tree(')')),
                                    Tree('t',
                                        Tree('u'),
                                        Tree('v'))))),
                     Tree('M',
                          Tree('G',
                               Tree('Z',
                                    Tree('7',
                                    	Tree('r'),
                                    	Tree('s')),
                                    Tree('\t',
                                    	Tree(''),
                                    	Tree(','))),
                               Tree('Q',
                                    Tree('w',
                                    	Tree('~'),
                                    	Tree('`')),
                                    Tree('x',
                                    	Tree('y'),
                                    	Tree('z')))),
                          Tree('O',
                               Tree('\n',
                                    Tree('8',
                                    	Tree(':'),
                                    	Tree('b')),
                                    Tree('a',
                                    	Tree('<'),
                                    	Tree('>'))),
                               Tree('\"',
                                    Tree('9',
                                    	Tree('{'),
                                    	Tree('}')),
                                    Tree('0',
                                    	Tree('['),
                                    	Tree(']')))))))



 




# enocder and decoder functions for messages

#get character from sequence using the tree for decoding

def get_char(sequence):
	char_tree = morse_tree
	for character in sequence:
		if character == '.':
			char_tree = char_tree.left								
		elif character == '-':
			char_tree = char_tree.right

	return char_tree.char


# message decoder

def decode(message):
	decoded_message = ''
	message = message.split(' ')
	for sequence in message:
		if sequence == '\\':
			decoded_message += ' '
		else:
			decoded_message += get_char(sequence)
	return decoded_message




# message endcoder
def encode(message):
     encoded_message = ''
     message = message
     message = message.split(' ')
     for sequence in message:
          for char in sequence:
               try:
                    encoded_message += morse_dict[char] + ' '
               except:
                    encoded_message += morse_dict['*'] + ' '
                    print( 'the symbol ---> \t '+ char + '\t <----' + 'is not avaibale in the current code.\n It will be replacaed with *' )
          encoded_message += ' \\ '

     return encoded_message



# encrpytion and decryption functions for messages
import random
def generate_key():
     crypt_key = list(range(0,len(morse_dict)))
     random.shuffle(crypt_key)
     return crypt_key



def encrypt_dict(crypt_key):
     base_dict = []
     encrypted_dict = {}
     for key in morse_dict:
          base_dict.append(key)
     for i in range(0,len(morse_dict)):
          encrypted_dict[base_dict[i]] = base_dict[crypt_key[i]]
     
     return encrypted_dict


#message encrypter

def encrypt(message,crypt_key):
     encrypted_dict = encrypt_dict(crypt_key)
     encrypted_message = ' '
     message = message
     message = message.split(' ')
     for sequence in message:
          for char in sequence:
               try:
                    if char != '\n':
                         encrypted_message += encrypted_dict[char]
                    else:
                         encrypted_message += encrypted_dict[char]
               except:
                    encrypted_message += encrypted_dict['*']
                    print( 'the symbol ---> \t '+ char + '\t <----' + 'is not avaibale in the current code.\n It will be replacaed with *')
          encrypted_message += ' '
     return encrypted_message

#message decrypter
def decrypt_dict(crypt_key):
     encrypted_dict = encrypt_dict(crypt_key)
     decrypted_dict = {}
     for key in encrypted_dict.keys():
          decrypted_dict[encrypted_dict[key]] = key

     return decrypted_dict

def decrypt(message,crypt_key):

   decrypted_dict = decrypt_dict(crypt_key)
   decrypted_message = ' '
   message = message.split(' ')
   for sequence in message:
          for char in sequence:
               if char != '\n':
                    decrypted_message += decrypted_dict[char]  
               elif char == '\n':
                    decrypted_message += '\n' 
          decrypted_message += ' '
   return decrypted_message



# #for exporting morse dict

# import pandas as pd



# df = pd.DataFrame(data=morse_dict, index=[0])

# df = (df.T)

# print(df)

# df.to_excel('dict1.xlsx')