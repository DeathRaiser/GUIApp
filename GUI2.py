from tkinter import *

#create root element
root=Tk()
root.title('GUI2')
root.configure(background='#D35400')
root.geometry('1100x975')

#create canvas
canvas=Canvas(root, height=950, width=1100, bg='#D35400')
canvas.pack()

caption=canvas.create_text(550, 25, text='Display1', font=('ComicSansMS', 40), fill='white')

#clicked() is a function which draws again and again so it appears that the window is being refreshed.
def clicked():
	Text=[]

	rect1 = canvas.create_rectangle(50, 50, 350, 450, fill='white')
	rect2 = canvas.create_rectangle(400, 50, 700, 450, fill='white')
	rect3 = canvas.create_rectangle(750, 50, 1050, 450, fill='white')
	rect4 = canvas.create_rectangle(50, 500, 350, 900, fill='white')
	rect5 = canvas.create_rectangle(400, 500, 700, 900, fill='white')
	rect6 = canvas.create_rectangle(750, 500, 1050, 900, fill='white')

	file1=open('text1', 'r')
	Text.append(file1.read())
	file2=open('text2', 'r')
	Text.append(file2.read())
	file3=open('text3', 'r')
	Text.append(file3.read())
	file4=open('text4', 'r')
	Text.append(file4.read())
	file5=open('text5', 'r')
	Text.append(file5.read())
	file6=open('text6', 'r')
	Text.append(file6.read())

	txt1=canvas.create_text(200, 250, text=Text[0], font=('Times', 30))
	txt2=canvas.create_text(550, 250, text=Text[1], font=('Times', 30))
	txt3=canvas.create_text(900, 250, text=Text[2], font=('Times', 30))
	txt4=canvas.create_text(200, 700, text=Text[3], font=('Times', 30))
	txt5=canvas.create_text(550, 700, text=Text[4], font=('Times', 30))
	txt6=canvas.create_text(900, 700, text=Text[5], font=('Times', 30))

	file1.close()
	file2.close()
	file3.close()
	file4.close()
	file5.close()
	file6.close()

	
clicked()

#If there are any changes in the text file, refresh button will refresh the values
refreshButton=Button(root, text='Refresh', command=clicked)
refreshButton.pack()

root.mainloop()