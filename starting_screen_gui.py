# importing tkinter and tkinter.ttk 
# and all their functions and classes 
from tkinter import * 
from PIL import Image,ImageTk
  
# importing askopenfile function 
# from class filedialog 
from tkinter.filedialog import askopenfile 
  
root = Tk() 
root.geometry('626x417') 
root.title('CHAT ANALYZER')

image2 = Image.open("gui/images/holy.jpg")
background_image =ImageTk.PhotoImage(image2)

# This function will be used to open 
# file in read mode and only Python files 
# will be opened 
def open_file():
	global path_to_file
	file = askopenfile(mode ='r', filetypes =[('JSON Files', '*.json')]) 
	path_to_file=str(file.name)
	root.destroy()


label = Label(root,text=" MESSENGER\nCHAT ANALYZER",font=('Consolas', 30, 'bold'),fg="#FFD3B5",image=background_image,compound='center').place(x=0,y=0,relwidth=1, relheight=1)
btn = Button(label, text ='Choose the .JSON file to open...', background='green',activebackground='#83AF9B',command = lambda:open_file()) 
btn.pack(side=BOTTOM) 

mainloop() 