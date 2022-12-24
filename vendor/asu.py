import os, sys, datetime
from datetime import datetime

ct = datetime.now().month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if ct < 0 or ct > 12:
        exit()
    nTemp = ct - 1
except ValueError:
    exit()
current = datetime.now()
op = bulan[nTemp]
ta = current.year
ha = current.day

H = '\x1b[1;92m' # HIJAU
N = '\x1b[0m'    # WARNA MATI
M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA

class Logo:

    def __init__(self):
        if "win" in sys.platform:os.system("cls")
        else:os.system("clear")

    def kontl(self, nama, key, cok):
        print(f"""
                         \ \ | * {ha} {op} {ta}
    .-'''''-.    __       |/ |----------------------------
   /         \.'`  `',.--//  | * ASU PEDIA [MBF]
 -(    Asu  | Pedia  |  {M}@@{N}\  | * premium : {key}
   \             /'._.'\__|  | * expred  : {M}{cok}{N}
    '-.....-' __/ | \   ({O}`{N})  |----------------------------
 v3.11.0 dev /   /  /        | * {H}{nama}{N}
                 \  \\

  +------------------------------------------------------+""")

    def logos(self):
        print(f"""
                         \ \ | * {ha} {op} {ta}
    .-'''''-.    __       |/ |----------------------------
   /         \.'`  `',.--//  | * ASU PEDIA [MBF]
 -(    Asu  | Pedia  |  {M}@@{N}\  | * AUTHOR: rendra
   \             /'._.'\__|  | * GIT   : github.com/asu-id
    '-.....-' __/ | \   ({O}`{N})  |----------------------------
 v3.11.0 dev /   /  /        | * {H}Asu Pedia{N}
                 \  \\

  +------------------------------------------------------+""")