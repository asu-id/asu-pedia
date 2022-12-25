import os

from masuk import masuk as yacek

if __name__ == '__main__':
    os.system('git pull');os.remove("results/OK/...");os.remove("results/CP/...")
    yacek()
