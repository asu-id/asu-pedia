import os

from masuk import masuk as yacek

try:os.remove("results/OK/...");os.remove("results/CP/...")
except:pass

if __name__ == '__main__':
    os.system('git pull') #;os.remove("results/OK/...");os.remove("results/CP/...")
    yacek()
