from tkinter import *
from tkinter import filedialog
import PyPDF2

def open_pdf():
    textbox.delete(1.0,END)

    filename=filedialog.askopenfilename(title="Choose a PDF file",filetypes=(("pdf files","*.pdf"),))

    if filename:
        pdf_file=PyPDF2.PdfFileReader(filename)

        #get no of pages
        n=pdf_file.getNumPages()
        
        for i in range(n):
        
            #get page

            page=pdf_file.getPage(i)

            #extract the contents of page
            page=page.extractText()

            #display it in textbox
            textbox.insert(END,page)
def clear():
    textbox.delete(1.0,END)




root=Tk()
root.title("PDF Reader")
root.geometry("700x700")

my_frame=Frame(root)
my_frame.pack()
scrollbar = Scrollbar(my_frame, orient=VERTICAL)
scrollbar.pack(fill=Y, side=RIGHT)

textbox=Text(my_frame,height=30,width=80)
textbox.pack(pady=20)



textbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=textbox.yview)


#menu
my_menu=Menu(root)
root.config(menu=my_menu)

file_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)

file_menu.add_command(label="Open",command=open_pdf)
file_menu.add_command(label="Clear Text",command=clear)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)








root.mainloop()
