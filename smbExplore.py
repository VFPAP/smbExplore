#!/usr/bin/python3

import os

ip = input("\n\nSMB IP:> ")

creds = input("Creds? (y/n)")

if creds == 'y':

	user = input("User:> ")
	passwd = input("Password:> ")
	domain = input("Domain:> ")

	#print("\nListing folders...\n")
	#os.system("smbclient -L " + ip + " -U "+user_passwd+" -W "+domain)

	os.system("smbmap -u " +user+ " -p " +passwd+ " -H " +ip)

	sn = input("\n\nSharename:> ")

	print("\n\nFolder >" + sn)
	os.system("smbclient //" + ip + "/" + sn + " -U "+user_passwd+" -W "+domain)

elif creds == 'n':

	#print("Listing folders...")
	#os.system("smbclient -L " + ip + " -N")

	os.system("smbmap -H " + ip)


	sn = input("\nSharename:> ")

	print("\nFolder >" + sn)
	os.system("smbclient //" + ip + "/" + sn +" -N")
