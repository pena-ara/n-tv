#!/usr/bin/env python
from os import system as s

ip_tv = open("iptv.list").readlines()
tv = []
a_tv =[]
for a in ip_tv:
    a_list = a.split(", ")
    tv.append(a_list[0])
    a_tv.append(a_list[1].replace("\n", ""))
jml_chl = (len(tv))

while True:
    s("clear")
    print(f"""
███╗   ██╗   ████████╗██╗   ██╗
████╗  ██║   ╚══██╔══╝██║   ██║
██╔██╗ ██║█████╗██║   ██║   ██║
██║╚██╗██║╚════╝██║   ╚██╗ ██╔╝
██║ ╚████║      ██║    ╚████╔╝ 
╚═╝  ╚═══╝      ╚═╝     ╚═══╝  By Nestero
Streaming TV, terdapat kurang lebih 21 Channel Lokal 
	""")
    print("List Channel :")

    for i, key in enumerate(tv):
    	if (i + 1) % 3:
        	print('{:20}'.format(key), end='\t')
    	else:
        	print(key, end='\n')    

    p_tv = int(input(f"\nPilih Channel 0 - {jml_chl-1} > "))
    
    if p_tv == 99:
        exit()
    else:
        c_tv = a_tv[p_tv]
        t_tv = tv[p_tv]
        s(f"mpv --fs --title='{t_tv}' {c_tv}")
