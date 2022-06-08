from tkinter import *
 
def ouvrir_popup():
	popup = Toplevel()
	popup.title("Pop Up")
	popup.grab_set()
	popup.transient(popup.master)
	popup.resizable(width=False, height=False)
	popup.configure(bd=10)
	Label(popup, text="Bonjour !\n").pack()
	Button(popup, text="Fermer", command=popup.destroy).pack()
 
 
root = Tk()
root.configure(bd=10)
 
Button(root, text="Ouvrir un popup !", command=ouvrir_popup).pack()
 
root.mainloop()