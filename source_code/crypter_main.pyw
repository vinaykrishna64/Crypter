import crypter_lib as crypt
import pickle
import os
import random
from tkinter import *
from PIL import ImageTk, Image
path = os.getcwd()
#get files in the directory
#generates lists of .p and .txt files in the current directory
global txt_files, key_files
txt_files = []
key_files = []

def get_files():

	files = os.listdir()

	for x in files:
	    if x.endswith(".txt"):
	    	txt_files.append(x)
	if txt_files == [] :
		with open('null.txt', 'w') as f:
			f.write('This file is created to prevent a program crash.')
	


	for x in files:
	    if x.endswith(".p"):
	    	key_files.append(x)

	if key_files == [] :
		key = crypt.generate_key() 
		with open('KEY0000.p', 'wb') as fp:
			pickle.dump(key, fp)
			get_files()


get_files()


	

#encryption

def encrpty_button():
	filename = clicked.get()
	key_file = open(clicked_key.get(),'rb')
	print_status('Encrypting...'+ filename + '..with key...'+ clicked_key.get())
	key = pickle.load(key_file)
	with open(filename) as f:
	    lines = f.readlines()
	if f_entry.get() == "Encrypt/Decrypt to ..":
		f_split = filename.split('.txt')
		f_name = f_split[0] + 'encrypted' + '.txt'
	else:
		f_name = f_entry.get() + '.txt'
	with open(f_name, 'w') as f:
		for line in lines:
			encrypted_line = crypt.encode(crypt.encrypt(line, key))
			
			f.write(encrypted_line)
			f.write('\n')
	print_status(filename + '...is encrypted to...' + f_name)
#decryption

def decrpty_button():
	filename = clicked.get()
	key_file = open(clicked_key.get(),'rb')
	key = pickle.load(key_file)
	print_status('Decrypting...'+ filename + '..with key...'+ clicked_key.get())
	if f_entry.get() == "Encrypt/Decrypt to ..":
		f_split = filename.split('.txt')
		f_name = f_split[0] + 'decrypted' + '.txt'
	else:
		f_name = f_entry.get() + '.txt'
	if os.path.exists(f_name):
		os.remove(f_name)
	with open(filename, 'r') as f:
		lines = f.readlines()

		for line in lines:

			decrypted_line = crypt.decrypt(crypt.decode(line), key)
			with open(f_name, 'a') as w:
				w.write(decrypted_line)

	print_status(filename + '...is decrypted to...' + f_name)
	








#    GUI


root = Tk()
root.title('Crypter')
root.iconbitmap(default=os.path.join(path, 'logo.ico'))

root.geometry("450x400")
# set minimum window size value
root.minsize(450, 400)
 
# set maximum window size value
root.maxsize(600, 800)

root.config(bg = 'azure')


def make_dropdowns():
	global clicked, clicked_key, sel_file_entry, sel_key_entry
	sel_file = Label(root, width=15, bg = 'LemonChiffon3', fg =  'dark blue' ,text = " <-- Select your file")
	sel_file.grid(row = 4, column = 2)
	clicked = StringVar()
	clicked.set('choose file')
	sel_file_entry = OptionMenu(root, clicked,*txt_files)
	sel_file_entry.grid(row = 4, column =0)
	sel_file_entry.config(width=30)
	sel_file_entry.config(bg='light blue')

	sel_key= Label(root, width=15, bg = 'LemonChiffon3', fg =  'dark blue',text = " <-- Select your key")
	sel_key.grid(row = 5, column = 2)
	clicked_key = StringVar()
	clicked_key.set('choose key')
	sel_key_entry = OptionMenu(root, clicked_key, *key_files)
	sel_key_entry.grid(row = 5, column =0)
	sel_key_entry.config(width=30)
	sel_key_entry.config(bg='light blue')

make_dropdowns()


encrpty_button = Button(root,width=20, text = 'Encrypt' ,command=encrpty_button,bg =  'snow2', fg =  'DarkOliveGreen4',padx=10, pady=10, font=('Helvetica',12))
encrpty_button.grid(row = 6, column =0,columnspan = 2)



decrpty_button = Button(root,width=20, text = 'Decrypt' ,command=decrpty_button,bg =  'snow2', fg = 'tomato', padx=10, pady=10, font=('Helvetica',12))
decrpty_button.grid(row = 6, column =2 ,columnspan = 2)

f_entry = Entry(root, width=20, font=('Helvetica',12),bg = 'snow2')
f_entry.grid(row = 7, column = 0,columnspan = 2)
f_entry.insert(0, "Name your file")

sel_f= Label(root, width=30, bg = 'LemonChiffon3', fg =  'dark blue',text = " <-- name a file for results (no extension)")
sel_f.grid(row = 7, column = 2)

key_entry = Entry(root, width=20, font=('Helvetica',12),bg = 'snow2')
key_entry.grid(row = 8, column =0,columnspan = 2)
key_entry.insert(0, "Name your key ")


def generate_key_button():
	key_name = key_entry.get()

	file = 'KEY' + str(random.randint(0, 10000))+'.p'
	if key_name != "Name your key ":
		file = key_name + '.p'
	
	key = crypt.generate_key() 
	with open(file, 'wb') as fp:
		pickle.dump(key, fp)

	key_entry.delete(0, END)
	key_entry.insert(0, "Name your key ")

	print_status('New key generated......' + file)


generate_key_button = Button(root,width=20, text = 'Generate_key' ,command=generate_key_button,bg =  'snow2', fg = 'dark goldenrod' ,padx=10, pady=10, font=('Helvetica',12))
generate_key_button.grid(row = 8, column = 2)




def refresh():
	print_status('Refreshing.....')
	#get all files
	txt_files.clear() 
	key_files.clear() 

	get_files()

	#refesh key dropdown
	
	sel_key_entry.destroy()

	
	#refresh file dropdown
	
	sel_file_entry.destroy()

	make_dropdowns()

	print_status('Refreshed!')

Refresh_button = Button(root,width=20, text = 'Refresh' ,command=refresh,bg =  'snow2', fg = 'SlateBlue1' ,padx=10, pady=10)
Refresh_button.grid(row = 9, column =0)
refresh_label = Label(root, width=20, bg = 'LemonChiffon3', fg =  'dark blue',text = " <-- Refresh files and keys")
refresh_label.grid(row = 9, column = 2)

main_label = Label(root, font=('Helvetica',10), width=50, bg = 'seashell3', fg =  'dark blue' ,text = "Make sure you use the correct key to decrypt.\n If you don't provide a name for  the key/file it is named automatically")
main_label.grid(row = 0, column = 0, columnspan = 3)

logo = Image.open(os.path.join(path, 'logo.png'))
logo = logo.resize((400, 100))
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image = logo)
logo_label.grid(row = 10, column = 0,columnspan = 4)

def print_status(status_str):
	status = Label(root, font=('Helvetica',10), bg = 'blanched almond', fg =  'dark green' ,text = status_str ,bd=1, relief=SUNKEN, anchor=E)
	status.grid(row = 11, column = 0, sticky = W+E, columnspan = 3)
print_status('Hello! welcome to Crypter!')
root.mainloop()