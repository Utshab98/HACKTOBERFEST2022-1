from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from PyPDF2 import PdfFileWriter, PdfFileReader

img_list = []
page = Image.open("images/Taking a break.png")
root = Tk()
root.title('Opening files')


def open_file():
	global page
	root.filename = filedialog.askopenfilenames(initialdir="images/",
												title="Select a file",
												filetypes=(
												("PNG Files", "*.png"),
												("All files", "*.*")))

	file_list = list(root.filename)

	for name in file_list:
		page = Image.open(name)
		page = page.convert("RGB")
		img_list.append(page)
		my_label = Label(text=name).pack()


def generate_pdf():
	global page
	global img_list
	page.save(r"Gone with the Blastwave.pdf", save_all=True,
			  append_images=img_list)

	print(img_list)


my_button = Button(root, text="Add file", command=open_file).pack()
my_button2 = Button(root, text="Generate PDF", command=generate_pdf).pack()
root.mainloop()


pages_to_delete = [0]  # page numbering starts from 0
infile = PdfFileReader('Gone with the Blastwave.pdf', 'rb')
output = PdfFileWriter()

for i in range(infile.getNumPages()):
	if i not in pages_to_delete:
		p = infile.getPage(i)
		output.addPage(p)

with open('Gone with the Blastwave.pdf', 'wb') as f:
	output.write(f)
