from Tkinter import *
import ttk
import tkFileDialog

root = Tk()
root.title("Usb Test")

mainframe = ttk.Frame(root, padding="8 8 8 8")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

def openFile():
	global isoDirectory
	isoDirectory = tkFileDialog.askopenfile(mode ='r', filetypes = [('.ISO Files', '*.iso')])
	fileDirectory = isoDirectory.name
	isoPathEntry.delete(0,END)
	isoPathEntry.insert(0,fileDirectory)

def usbDirWindow():
	usbDir1 = tkFileDialog.askdirectory(initialdir="/Volumes/")
	usbDirectory = usbDir1
	usbDirEntry.delete(0,END)
	usbDirEntry.insert(0,usbDirectory)	

def runShit():
	print ("%s %s" % (usbDirectory,isoDirectory.name))
	
def UsbSelect():
	isoChooseLabel.grid_forget()
	isoBrowseButton.grid_forget()
	isoPathEntry.grid_forget()
	isoNextButton.grid_forget()
	global usbDirectory
	usbDirectory = StringVar()
	#global usbDirectory
	usbDirLabel = ttk.Label(mainframe, text="Please choose your USB Stick/Device")
	usbDirEntry = ttk.Entry(mainframe, textvariable=usbDirectory)
	usbDirButton = ttk.Button(mainframe, text="Browse", command=usbDirWindow)
	usbNextButton = ttk.Button(mainframe, text="Next", command=runShit)
	usbDirLabel.grid(column=2, row=1, sticky=(E, W))
	usbDirEntry.grid(column=1, row=2, sticky=E)
	usbDirButton.grid(column=2, row=2, sticky=W)
	usbNextButton.grid(column=3, row=3, sticky=(N, E, W, S))
	
	usbDirectory = tkFileDialog.askdirectory(initialdir="/Volumes")
	

#def setText(text):
#    e.delete(0,END)
#    e.insert(0,text)
#    return
fileDirectory = StringVar()
isoChooseLabel = ttk.Label(mainframe, text="Choose your ISO file")
#isoPathEntry = ttk.Label(mainframe, textvariable=fileDirectory)
isoBrowseButton = ttk.Button(mainframe, text="Browse", command=openFile)
isoPathEntry = ttk.Entry(mainframe, textvariable=fileDirectory)
isoNextButton = ttk.Button(mainframe, text="Next", command=UsbSelect)
print("%s" % (fileDirectory.get()))

isoChooseLabel.grid(row=1, column=1, sticky=(E, W))
isoPathEntry.grid(row=3, column=1, sticky=E)
isoBrowseButton.grid(row=3, column=2, sticky=W)
isoNextButton.grid(row=4, column=3, sticky=E)



root.mainloop()