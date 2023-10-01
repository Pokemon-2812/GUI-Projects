from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfile
from PyPDF2 import PdfMerger
from tkinter.messagebox import showinfo
merger=PdfMerger()
root=Tk()
root.title("Pdf Merger")
root.geometry("300x200")
files=[]
def openfile():
	file_name=askopenfilename(defaultextension=".pdf",filetypes=[('PDF Files',"*.pdf")])
	if file_name!=None:
		files.append(file_name)
def save():
	global files
	to_file=asksaveasfile(defaultextension=".pdf" ,filetypes = [('PDF Files',"*.pdf")])
	if to_file!=None:
		if(len(files)>0):
			try:
				for file_name in files:
					merger.append(file_name)
			except Exception as e:
				showinfo("Error","Sorry,an error occured.")
			else:
				merger.write(to_file.name)
				merger.close()
				showinfo("File saved",f"File saved at {to_file.name}")
				files=[]
btn=Button(root,text="Add",font="arial 14 bold",bg="blue",fg="white",width=7,command=openfile)
btn.pack(expand=True,fill=BOTH)
btn2=Button(root,text="Save",font="arial 14 bold",bg="red",fg="white",width=7,command=save)
btn2.pack(expand=True,fill=BOTH)
menu=Menu(root)
fileMenu=Menu(menu,tearoff=0)
fileMenu.add_command(label="Add",command=openfile)
fileMenu.add_command(label="Save",command=save)
menu.add_cascade(label="File",menu=fileMenu)
root.config(menu=menu)
root.mainloop()