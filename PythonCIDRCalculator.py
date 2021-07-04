# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI SCRIPT FOR USER-ENTERED IPv4 CIDR CALCULATOR USING ipaddress MODULE

# ipaddress provides the capabilities to create, manipulate and operate on IPv4 and IPv6 addresses and networks.
# Python’s ipaddress module is an underappreciated gem from the Python standard library. The functions and classes
# in this module make it straightforward to handle various tasks related to IP addresses, including checking
# whether or not two hosts are on the same subnet, iterating over all hosts in a particular subnet, checking
# whether or not a string represents a valid IP address or network definition, and so on.

# Importing necessary packages
import ipaddress
import tkinter as tk
from tkinter import *

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    ipLabel = Label(root, text="ENTER IPv4 ADDRESS : ", bg="deepskyblue4")
    ipLabel.grid(row=0, column=0, padx=10, pady=5)
    root.ipEntry = Entry(root, width=20, textvariable=ipAddress)
    root.ipEntry.grid(row=0, column=1, padx=10, pady=5)

    calculateButton = Button(root, text="CALCULATE", command=calculateCIDR)
    calculateButton.grid(row=1, column=0, padx=5, pady=5, columnspan=2)
    clearButton = Button(root, text="CLEAR", command=clearEntries)
    clearButton.grid(row=1, column=1, padx=5, pady=5, columnspan = 2)

    networkAddress = Label(root, text="NETWORK ADDRESS : ", bg="deepskyblue4")
    networkAddress.grid(row=2, column=0, padx=10, pady=5)
    root.networkAddressEntry = Entry(root, width=20)
    root.networkAddressEntry.grid(row=2, column=1, padx=10, pady=5)

    broadcastAddress = Label(root, text="BROADCAST ADDRESS : ", bg="deepskyblue4")
    broadcastAddress.grid(row=3, column=0, padx=10, pady=5)
    root.broadcastAddressEntry = Entry(root, width=20)
    root.broadcastAddressEntry.grid(row=3, column=1, padx=10, pady=5)

    firstIPL = Label(root, text="FIRST HOST IP ADDRESS : ", bg="deepskyblue4")
    firstIPL.grid(row=4, column=0, padx=10, pady=5)
    root.firstIP = Entry(root, width=20)
    root.firstIP.grid(row=4, column=1, padx=10, pady=5)

    lastIPL = Label(root, text="LAST HOST IP ADDRESS : ", bg="deepskyblue4")
    lastIPL.grid(row=5, column=0, padx=10, pady=5)
    root.lastIP = Entry(root, width=20)
    root.lastIP.grid(row=5, column=1, padx=10, pady=5)

    numberOfIPs = Label(root, text="NUMBER OF USABLE IPs : ", bg="deepskyblue4")
    numberOfIPs.grid(row=6, column=0, padx=10, pady=5)
    root.numberOfIPsEntry = Entry(root, width=20)
    root.numberOfIPsEntry.grid(row=6, column=1, padx=10, pady=5)

    subnetRange = Label(root, text="SUBNET MASK : ", bg="deepskyblue4")
    subnetRange.grid(row=7, column=0, padx=10, pady=5)
    root.subnetRangeEntry = Entry(root, width=20)
    root.subnetRangeEntry.grid(row=7, column=1, padx=10, pady=5)

    wildcardLabel = Label(root, text="WILDCARD : ", bg="deepskyblue4")
    wildcardLabel.grid(row=8, column=0, padx=10, pady=5)
    root.wildcardEntry = Entry(root, width=20)
    root.wildcardEntry.grid(row=8, column=1, padx=10, pady=5)

# Defining calculateCIDR() function to find the calucate the CIDR RANGE of the IP Address
def calculateCIDR():
    # Retrieving and storing user-entered IPv4 Address in the variable
    userinput_ip_address = ipAddress.get()
    # Converting the String IP Address into IPv4 Interface object using ip_interface()
    ip_address = ipaddress.ip_interface(userinput_ip_address)
    # Obtaining the network to which user-entered IPv4 Interface belongs using network
    network_address = ip_address.network
    # Obtaining the usable hosts in the network using hosts() and converting to list().
    # Fetching the first ip address and last ip address from the list using indices
    first_ip_address = list(network_address.hosts())[0]
    last_ip_address = list(network_address.hosts())[-1]
    # Storing the length of the list of hosts as the number of the usable ips
    number_of_usable_ips = len(list(network_address.hosts()))
    # Storing the broadcast_address which can retrieved from network_address
    broadcast_address = network_address.broadcast_address
    # Storing the wildcard mask from the ip_address using hostmask
    wildcard = ip_address.hostmask
    # Storing the subnet_mask from the ip_address
    subnet_mask = ip_address.with_netmask.split('/')[1]

    # Clearing previous CIDR entries if there's any
    root.networkAddressEntry.delete(0, END)
    root.firstIP.delete(0, END)
    root.lastIP.delete(0, END)
    root.numberOfIPsEntry.delete(0, END)
    root.broadcastAddressEntry.delete(0, END)
    root.subnetRangeEntry.delete(0, END)
    root.wildcardEntry.delete(0, END)

    # Showing the new results in the tkinter window
    root.networkAddressEntry.insert('0', str(network_address).split('/')[0])
    root.firstIP.insert('0', str(first_ip_address))
    root.lastIP.insert('0', str(last_ip_address))
    root.numberOfIPsEntry.insert('0', str(number_of_usable_ips))
    root.broadcastAddressEntry.insert('0', str(broadcast_address))
    root.subnetRangeEntry.insert('0', str(subnet_mask))
    root.wildcardEntry.insert('0', str(wildcard))

# Defining clearEntries() to clear the values from the text entries of tkinter window
def clearEntries():
    ipAddress.set('')
    root.networkAddressEntry.delete(0, END)
    root.firstIP.delete(0, END)
    root.lastIP.delete(0, END)
    root.numberOfIPsEntry.delete(0, END)
    root.broadcastAddressEntry.delete(0, END)
    root.subnetRangeEntry.delete(0, END)
    root.wildcardEntry.delete(0, END)

# Creating object of tk class
root = tk.Tk()
# Setting the title, background color, windowsize & disabling the resizing property
root.title("PythonCIDRCalculator")
root.config(background="deepskyblue4")
root.geometry("420x350")
root.resizable(False, False)
# Creating tkinter variable
ipAddress = StringVar()
# Calling the CreateWidgets() function
CreateWidgets()
# Defining infinite loop to run application
root.mainloop()
