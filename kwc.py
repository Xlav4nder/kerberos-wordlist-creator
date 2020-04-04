#!/usr/bin/env python
import sys


def CreateWordlist():
	f = open(sys.argv[2],"w")
	for line in open(sys.argv[1]):
		fullname = ''.join([c for c in line if  c == " " or  c.isalpha()])

		parts = fullname.split()
		fname = parts[0]
		lname = parts[-1]

		f.write(fname.capitalize() + "\n")
		f.write(fname.lower() + "\n")
		f.write(lname.capitalize() + "\n")
		f.write(lname.lower() + "\n")
        
		#all combinations from pure firstname+lastname
		f.write(fname + lname+ "\n")
		f.write(fname.capitalize() + lname.capitalize() + "\n")
		f.write(fname.lower() + lname.lower() + "\n")
		f.write(fname.capitalize() + lname.lower() + "\n")
		f.write(fname.lower() + lname.capitalize() + "\n")

		#first letter + last name
		f.write(fname[0].capitalize() + "." + lname.capitalize() + "\n")
		f.write(fname[0].lower() + "." + lname.lower() + "\n") 
		f.write(fname[0].capitalize() + "." + lname.lower() + "\n") 
		f.write(fname[0].lower() + "." + lname.capitalize() + "\n") 

		#first name + first letter
		f.write(fname.capitalize() + "." + lname[0].capitalize() + "\n")
		f.write(fname.lower() + "." + lname[0].lower() + "\n")
		f.write(fname.capitalize() + "." + lname[0].lower() + "\n")
		f.write(fname.lower() + "." + lname[0].capitalize() + "\n")

		#first letter + last name (no dot)
		f.write(fname[0].capitalize() + lname.capitalize() + "\n")
		f.write(fname[0].lower() + lname.lower() + "\n") 
		f.write(fname[0].capitalize() + lname.lower() + "\n") 
		f.write(fname[0].lower() + lname.capitalize() + "\n")

		#first name + first letter (no dot)
		f.write(fname.capitalize() + lname[0].capitalize() + "\n")
		f.write(fname.lower() + lname[0].lower() + "\n")
		f.write(fname.capitalize() + lname[0].lower() + "\n")
		f.write(fname.lower() + lname[0].capitalize() + "\n")

		

        
        
        
if __name__ == "__main__": 
	if len(sys.argv) != 3:
		print "[INVALID INPUT] \nusage: kwc.py <input filelename> <output filename>"
		sys.exit(0)
	else:
		CreateWordlist()
