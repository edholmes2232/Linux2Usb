#!/usr/bin/env python

from os import system

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    WHITE = '\033[47m'
    GREY = '\033[90m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''
        self.WHITE = ''
	self.GREY = ''

print bcolors.FAIL + "By continuing, you agree to holding full responsibility to f*cking up your computer."
print bcolors.OKBLUE
raw_input("Plug in your USB stick and press Enter" + bcolors.GREY)
system("diskutil list" )
print bcolors.OKBLUE
usbno = raw_input("\n\nPlease enter the number of your USB stick \n(e.g. '/dev/disk1' == '1'): " + bcolors.ENDC)
print bcolors.FAIL
yn = raw_input("Okay this will wipe your USB stick and all of it's data. Continue?[Y/n] " + bcolors.ENDC)

if yn == "n":
	quit()

print bcolors.GREY
system("diskutil eraseDisk FAT32 USB disk%s > /dev/null && diskutil unmountDisk /dev/disk%s > /dev/null" % (usbno,usbno))
print bcolors.OKBLUE + "Please type the path of the ISO or Drag + Drop on this terminal window "
path = raw_input(""+ bcolors.ENDC)
print bcolors.GREY
system("hdiutil convert %s -format UDRW -o /tmp/convert.img && mv /tmp/convert.img.dmg /tmp/convert.img" % (path))
print bcolors.OKBLUE + "This part may take a while. Please give it up to 5 minutes" + bcolors.ENDC
system("sudo echo 'hello' > /dev/null ")
print bcolors.GREY
system("sudo dd if=/tmp/convert.img of=/dev/rdisk%s bs=1m && diskutil eject /dev/disk%s" % (usbno,usbno)) 
print bcolors.OKGREEN + "Done! The Linux USB was created successfully!"
print
print bcolors.HEADER + "Press any key to exit"
raw_input()
print bcolors.OKBLUE + "~ Created by Ed Holmes" + bcolors.ENDC

