import pandas as pd
import multiprocessing as mp
import sys
import subprocess
import time


a = sys.argv[1]
b = sys.argv[2]

l = [a, b]

# Store subprocess handles (Popen objects).
subprocesses = []

# Launch subprocesses in the background.
for filename in l:
    f_in = filename
    f_out = filename + "out.tsv"
    proc = subprocess.Popen(['python', 'read_file.py', f_in, f_out])
    subprocesses.append(proc)

# Wait for each subprocess to finish.
for proc in subprocesses:
    if proc.wait() != 0:
        # Error occurred, handle it however you want
        raise RuntimeError('Subprocess failed with nonzero exit code')

df1 = pd.read_csv(a + "out.tsv")
df2 = pd.read_csv(b + "out.tsv")

df = pd.merge(df1, df2, on="Name").to_csv("test.tsv", sep="\t", header=0)
