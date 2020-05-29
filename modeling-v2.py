from __future__ import print_function
import sys
sys.path.append('/Users/Manon/anaconda3/lib/python3.5/site-packages')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pprint import pprint as p
import sys
import seaborn as sns
from scipy.stats import norm

#seq = np.append([np.negative([np.ones((15,), dtype=int)])],[np.ones((35,), dtype=int)])
#np.random.shuffle(seq)

#Block 2 sequence
seq = [-1,-1,-1,-1,1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,1,1,1,1,1,-1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,-1,1,1,1,1,-1,-1,-1,1]

choice = np.append([np.negative([np.ones((10,), dtype=int)])],[np.ones((20,), dtype=int), np.zeros((20,), dtype=int)])
np.random.shuffle(choice)

trials = np.arange(0,50)

e = 0
bet = []
evidence = []
alpha = .15
epsilon = .8
d = 2
rand = []
choice = []
betleft = []
betright = []
pbet = []
obsblue = []
obsorange = []


for i in range(len(trials)):
    evidence.append(e)
    p_bet = norm.cdf((e-d)/epsilon) + norm.cdf((-e-d)/epsilon)
    random = np.random.uniform(low=0, high = 1)
    betTrue = random < p_bet
    if betTrue:
        if e > 0:
            choice.append(1)
            betleft.append(e)
            betright.append(None)
        else:
            choice.append(-1)
            betright.append(e)
            betleft.append(None)
        observed = 0
        obsorange.append(None)
        obsblue.append(None)
    else:
        observed = seq[i]
        if observed == 1:
            obsblue.append(e)
            obsorange.append(None)
        else:
            obsorange.append(e)
            obsblue.append(None)
        choice.append(0)
        betleft.append(None)
        betright.append(None)
    
    
    e = (1-alpha)*e+observed
    bet.append(betTrue)
    rand.append(random)
    pbet.append(p_bet)

df = pd.DataFrame({'evidence':evidence,
                  'bet': bet,
                  'choice': choice,
                  'random draw': rand,
                  'bet left': betleft,
                  'bet right': betright,
                  'pbet': pbet,
                  'orange':obsorange,
                  'blue':obsblue})

plt.plot(trials, df['evidence'], color = "black", linestyle = 'dashed')
plt.scatter(trials,obsorange,color='orange', edgecolors = 'black', s = 30)
plt.scatter(trials, obsblue, color = 'deepskyblue', edgecolors = 'black', s = 30)
plt.scatter(trials, betleft, color = 'grey', edgecolors = 'black', s = 30)
plt.scatter(trials, betright,color = 'grey', edgecolors = 'black', s = 30)
plt.show()
