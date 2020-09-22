import pandas as pd
import sys

a = sys.argv[1]
b = sys.argv[2]

df = pd.read_csv(a, header=0, sep="\t").tail(200000).to_csv(b, header=True, index=False)
