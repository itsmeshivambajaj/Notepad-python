import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Notepad:

    #variables
    root = Tk()

    #default window width and height
    width = 300
    _height_ = 300
    Text_Area = Text(root)
    menu_bar = Menu(root)
    file_menu = Menu(menu_bar,tearoff=0)
    edit_menu = Menu(menu_bar,tearoff=0)
    help_menu = Menu(menu_bar,tearoff=0)
    scroll_bar = Scrollbar(Text_Area)
    _file_ = None

    def __init__(self,**scrn):
        #initialization

        #set icon
        try:
        		self.root.wm_iconbitmap("Notepad.ico") #GOT TO FIX THIS ERROR (ICON)
        except:
        		pass

        #set window size (the default is 300x300)

        try:
            self.width = scrn['width']
        except KeyError:
            pass

        try:
            self._height_ = scrn['height']
        except KeyError:
            pass

        #set the window text
        self.root.title("Untitled - Notepad")

        #center the window
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        left = (screenWidth / 2) - (self.width / 2)
        top = (screenHeight / 2) - (self._height_ /2)

        self.root.geometry('%dx%d+%d+%d' % (self.width, self._height_, left, top))

        #to make the textarea auto resizable
        self.root.grid_rowconfigure(0,weight=1)
        self.root.grid_columnconfigure(0,weight=1)

        #add controls (widget)

        self.Text_Area.grid(sticky=N+E+S+W)

        self.file_menu.add_command(label="New",command=self.__newFile)
        self.file_menu.add_command(label="Open",command=self.__openFile)
        self.file_menu.add_command(label="Save",command=self.__saveFile)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit",command=self.__quitApplication)
        self.menu_bar.add_cascade(label="File",menu=self.file_menu)

        self.edit_menu.add_command(label="Cut",command=self.__cut)
        self.edit_menu.add_command(label="Copy",command=self.__copy)
        self.edit_menu.add_command(label="Paste",command=self.__paste)
        self.menu_bar.add_cascade(label="Edit",menu=self.edit_menu)

        self.help_menu.add_command(label="About Notepad",command=self.__showAbout)
        self.menu_bar.add_cascade(label="Help",menu=self.help_menu)

        self.root.config(menu=self.menu_bar)

        self.scroll_bar.pack(side=RIGHT,fill=Y)
        self.scroll_bar.config(command=self.Text_Area.yview)
        self.Text_Area.config(yscrollcommand=self.scroll_bar.set)
    
        
    def __quitApplication(self):
        self.root.destroy()
        #exit()

    def __showAbout(self):
        showinfo("Notepad","Created by: Shivam")

    def __openFile(self):
        
        self._file_ = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

        if self._file_ == "":
            #no file to open
            self._file_ = None
        else:
            #try to open the file
            #set the window title
            self.root.title(os.path.basename(self._file_) + " - Notepad")
            self.Text_Area.delete(1.0,END)

            file = open(self._file_,"r")

            self.Text_Area.insert(1.0,file.read())

            file.close()

        
    def __newFile(self):
        self.root.title("Untitled - Notepad")
        self._file_ = None
        self.Text_Area.delete(1.0,END)

    def __saveFile(self):

        if self._file_ == None:
            #save as new file
            self._file_ = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

            if self._file_ == "":
                self._file_ = None
            else:
                #try to save the file
                file = open(self._file_,"w")
                file.write(self.Text_Area.get(1.0,END))
                file.close()
                #change the window title
                self.root.title(os.path.basename(self._file_) + " - Notepad")
                
            
        else:
            file = open(self._file_,"w")
            file.write(self.Text_Area.get(1.0,END))
            file.close()

    def __cut(self):
        self.Text_Area.event_generate("<<Cut>>")

    def __copy(self):
        self.Text_Area.event_generate("<<Copy>>")

    def __paste(self):
        self.Text_Area.event_generate("<<Paste>>")

    def run(self):

        #run main application
        self.root.mainloop()




#run main application
notepad = Notepad(width=600,height=400)
notepad.run()


