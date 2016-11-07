from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.font import *

#keybindings

filename = None
clipboard = None

#######################################################################
#TextEditor WIP in Tkinter
#Version 1.0.0
#author James Du Plessis
#######################################################################

"""
Creates a new file to work on.

Version: 1.0.0
"""
def newFile():
	global filename
	filename = 'Untitled Project'
	text.delete(0.0, END)

"""
Saves a file.

Version: 1.0.0
"""
def saveFile():
	global filename
	t = text.get(0.0, END)
	with open(filename, 'w') as f:
		f.write(t)

"""
Save a file as something.

Version: 1.0.0
"""
def saveAsFile():
	f = asksaveasfile(mode='w', defaultextension='.txt')
	t = text.get(0.0, END)
	try:
		f.write(t.rstrip())
	except:
		showerror(title='Sorry', message='Cannot save file...')

"""
Opens a file.

Version: 1.0.0
"""
def openFile():
	f = askopenfile(mode='r')
	t = f.read()
	text.delete(0.0, END)
	text.insert(0.0, t)

"""
Makes a copy of content.

Version: 1.0.0
"""
def doCopy():
	global clipboard
	sel = text.selection_get()
	clipboard = sel

"""
Cut content for pasting.

Version: 1.0.0
"""
def doCut():
	global clipboard
	sel = text.selection_get()
	clipboard = sel
	text.delete(SEL_FIRST, SEL_LAST)

"""
Pastes content.

Version: 1.0.0
"""
def doPaste():
	global clipboard
	text.insert(INSERT, clipboard)

"""
Undo the last change to the file.

Version: 1.0.0
"""
def doUndo():
	t.edit_undo()

"""
Redo the last change to a file.

Version: 1.0.0
"""
def doRedo():
	t.edit_redo()

"""
Find by text.

Version: 1.0.0
"""
def doSearch():
	print('To be implemented')

"""
Development placeholder

Version: 1.0.0
"""
def doNothing():
	print('To be implemented')


root = Tk()

# **** Top Menu ****


#Initialising the menus
fileMenu = Menu(root)
root.config(menu=fileMenu)

filem = Menu(fileMenu, tearoff=False)
fileMenu.add_cascade(label='File', menu=filem)
filem.add_command(label='New File..', command=newFile)
filem.add_command(label='Open File..', command=openFile)
filem.add_command(label='Recent', command=doNothing)
filem.add_command(label='Save', command=doNothing)
filem.add_command(label='Save As..', command=saveAsFile)
filem.add_separator()
filem.add_command(label='Exit', command=quit)


edit = Menu(fileMenu, tearoff=False)
fileMenu.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Undo', command=doNothing)
edit.add_command(label='Redo', command=doNothing)
edit.add_separator()
edit.add_command(label='Cut', command=doCut)
edit.add_command(label='Copy', command=doCopy)
edit.add_command(label='Paste', command=doPaste)
edit.add_separator()
edit.add_command(label='Find...', command=doSearch)

view = Menu(fileMenu, tearoff=False)
fileMenu.add_cascade(label='View', menu=view)
view.add_command(label='Hide Status Bar', command=doNothing)
view.add_command(label='Hide Toolbar', command=doNothing)
view.add_separator()
view.add_command(label='Enter Fullscreen', command=doNothing)

help = Menu(fileMenu, tearoff=False)
fileMenu.add_cascade(label='Help', menu=help)
help.add_command(label='Documentation', command=doNothing)
help.add_separator()
help.add_command(label='About Text Editor', command=doNothing)

# **** ToolBar ****

#toolbar = Frame(root, bg='gray94')
#newbutton = Button(toolbar, text='New', command=newFile)
#newbutton.pack(side=LEFT, padx=2, pady=2)
#openbutton = Button(toolbar, text='Open', command=openFile)
#openbutton.pack(side=LEFT, padx=2, pady=2)
#savebutton = Button(toolbar, text='Save', command=saveFile)
#savebutton.pack(side=LEFT, padx=2, pady=2)

#toolbar.pack(side=TOP, fill=X)

# ****Status Bar****

status = Label(root, text='Status Bar', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

# ****Main Widget****

root.title('Text Editor')
root.minsize(width=400, height=400)


# ****Fonts****
defaultFont = Font(family='Helvetica', size=12)


text = Text(root, width=400, height=400, undo=True)
text.tag_config("default", font=defaultFont)
text.tag_add("default", 0.0, END)
text.configure(bg='gray10', fg='white')
text.pack()

root.mainloop()