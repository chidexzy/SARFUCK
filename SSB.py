#coding=utf-8
import os, sys, platform, time
from time import sleep

def brand():
	os.system('clear')
	print("""
██████╗ ██████╗ ███████╗██╗  ██╗
██╔══██╗██╔══██╗██╔════╝╚██╗██╔╝
██║  ██║██████╔╝█████╗   ╚███╔╝ 
██║  ██║██╔══██╗██╔══╝   ██╔██╗ 
██████╔╝██║  ██║███████╗██╔╝ ██╗
╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                """)
	time.sleep(1)
	os.system('clear')
	print("""
██╗███████╗
██║██╔════╝
██║███████╗
██║╚════██║
██║███████║
╚═╝╚══════╝
           """)
	time.sleep(1)
	os.system('clear')
	print("""
██╗  ██╗██╗███╗   ██╗ ██████╗ 
██║ ██╔╝██║████╗  ██║██╔════╝ 
█████╔╝ ██║██╔██╗ ██║██║  ███╗
██╔═██╗ ██║██║╚██╗██║██║   ██║
██║  ██╗██║██║ ╚████║╚██████╔╝
╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                              """)
	time.sleep(1)
	os.system('clear')
try:
    if sys.argv[1]=='update':
        os.system('rm -rf Sarfraz.so Sarfraz32.so')
except:
    pass
os.system('rm -rf Sarfraz.so Sarfraz32.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Sarfraz.so'):
        os.system('curl -L https://github.com/Sarfraz-XD/executables/blob/main/Sarfraz.cpython-311.so?raw=true -o Sarfraz.so') 
        brand()
        import Sarfraz
    else:
        brand()
        import Sarfraz

elif bit == '32bit':
    if not os.path.isfile('Sarfraz32.so'):
        os.system('curl -L https://github.com/Sarfraz-XD/executables/blob/main/Sarfraz32.cpython-311.so?raw=true -o Sarfraz32.so') 
        brand()
        import Sarfraz32
    else:
        brand()
        import Sarfraz32
