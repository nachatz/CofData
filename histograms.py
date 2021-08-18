import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import os

df = pd.read_csv('./properties.csv')

targets = df.columns[1:]
targets = [t for t in targets if not 'unit' in t] # remove units

os.mkdir('./histograms')

# now we have targets and target_cifs we can build plots. 
for target in targets: 
    x = list(df[target])
    plt.figure()
    plt.hist(x, bins=30)
    plt.ylabel('No of Cofs')
    plt.xlabel(target)
    plt.savefig('./histograms/' + target + '.png')
