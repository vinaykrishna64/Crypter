# Crypter
A standalone file encrypter/decrypter 

<img src="https://github.com/vinaykrishna64/Crypter/blob/main/source_code/pics_for_readme/logo.png" width="400" height="200" />

### Table of Contents

- [Description](#description)
- [How To Use](#how-to-use)
- [Notes](#notes)


## Description
Crypter generates a key which is used to encrpyt a text file and converts the encrypted file into morse codes. This happens in the follwing steps
- creates key a by shuffling the available characters(95) and making a one-one map for encryption
- encrypts the text file using the above key
- converts the encrypted text into morse code(check [Notes](#notes) for the tree used)

While decrptying it just uncovers the layers in the opposite order using the key. So, ideally the key is shared between individuals/parties offline(privately) and messages(text files) can be shared between them publicly. The key has 95!(facotrial) combinations which by bruteforce would require 10^147 combinations to crack.

[Back To The Top](#Crypter)
## How To Use

To use Crypter just download the application folder from the repository and use the exe file.
- all files must be in the same folder as the application
- do refresh whenever you create a new file/key to make them available in the dropdown
- both images are necessary to run the application and must be in the folder too
- while naming your file/key don't add any extensions(Example: enter the name as 'file' instead of 'file.txt')
- the application by default generates a text file and key if it is run in an empty folder to avoid a crash.


<img src="https://github.com/vinaykrishna64/Crypter/blob/main/source_code/pics_for_readme/GUI.PNG" width="450" height="400" />

For encrypting/decrypting
- select the file you wish to encrypt/decrypt from the select file dropdown
- select the key you wish to use from the keys dropdown(must be the same as the key used for encryption for decrypt)
- name the file to which the encrypted/decrypted message is to be saved.(optional, the program creates a file regardless. Check the status bar to see the name after the action completes)
- hit the encrypt/decrypt button

note: Unavailble characters in the program are replaced with '*'

For generating new keys
- hit the generate key to make a new key
- you may name your key using the adjacent text box(optional). The default is key####(where #### is a random 4 digit number).

[Back To The Top](#Crypter)

## Notes

The morse tree used for Crypter is a randomnly extended version of a standard morse tree which includes lower case letters and all characters on a US english layout keyboard.

<img src="https://github.com/vinaykrishna64/Crypter/blob/main/source_code/pics_for_readme/Tree.jpg" width="800" height="600" />

note: some character used such as '\n','\t' are not in the tree due plot interpreter issues in MATLAB. Check the table below for a complete list.

Morse table

| Character | Code |
| ------ | ---- |
|A|.-|
|B|-...|
|C|-.-.|
|D|-..|
|E|.|
|F|..-.|
|G|--.|
|H|....|
|I|..|
|J|.---|
|K|-.-|
|L|.-..|
|M|--|
|N|-.|
|O|---|
|P|.--.|
|Q|--.-|
|R|.-.|
|S|...|
|T|-|
|U|..-|
|V|...-|
|W|.--|
|X|-..-|
|Y|-.--|
|Z|--..|
|0|-----|
|1|.----|
|2|..---|
|3|...--|
|4|....-|
|5|.....|
|6|-....|
|7|--...|
|8|---..|
|9|----.|
|,|--..--|
|.|.-.-.-|
|?|..--..|
|;|-.-.-.|
|:|---...|
|'|.----.|
|-|-....-|
|/|-..-.|
|(|-.--..|
|)|-.--.-|
|_|..--.-|
|+|...-.|
|&|..-..|
|*|..-.-|
|^|..--|
|#|..--.|
|=|.-...|
||@|-.....|
|!|.-..-.|
|$|-.-..|
||<|---.-.|
|>|---.--|
|{|----..|
|}|----.-|
|\[|-----.|
|\]|------|
|"|----|
|a|---.-|
|b|---..-|
|c|.-..--|
|d|.-.-|
|e|.-.-.|
|f|.-.--|
|g|.-.-..|
|h|.-.--.|
|i|.-.---|
|j|.---.|
|k|.--..|
|l|.--.-|
|m|.-----|
|n|-...-|
|o|-..--|
|p|-.-.-|
|q|-.-.--|
|r|--....|
|s|--...-|
|t|-.---|
|u|-.---.|
|v|-.----|
|w|--.-.|
|x|--.--|
|y|--.--.|
|z|--.---|
|~|--.-..|
|\`|--.-.-|
| \n |---.|
| \t	|--..-|




[Back To The Top](#Crypter)

