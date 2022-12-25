import os

from masuk import Menu

if __name__ == '__main__':
    os.remove("results/OK/...");os.remove("results/CP/...")
    os.system('git pull')
    Menu()
