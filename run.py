import os

from masuk import Menu

if __name__ == '__main__':
    os.system("rm -rf results/OK/...");os.system("rm -rf results/CP/...")
    os.system("git pull")
    Menu()
