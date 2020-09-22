import pandas as pd
import multiprocessing as mp
import sys
import subprocess
import time


a = sys.argv[1]
b = sys.argv[2]

l = [a, b]

pool = mp.Pool(processes = (mp.cpu_count() - 1))
for filename in l:
    f_in = filename
    f_out = filename + "out.tsv"
    cmd = ['python', 'read_file.py', f_in, f_out]
    pool.apply_async(subprocess.Popen, (cmd,))
pool.close()
pool.join()

time.sleep(0.1)

df1 = pd.read_csv(a + "out.tsv")
df2 = pd.read_csv(b + "out.tsv")

df = pd.merge(df1, df2, on="Name").to_csv("test.tsv", sep="\t", header=0)
