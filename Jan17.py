

import numpy as np
from scipy.stats import f_oneway

#data for the groups
group_a = np.array([20,22,19,24,20])
group_b = np.array([18,17,20,21,19])
group_c = np.array([25,27,26,24,28])

#perform one way ANOVA
f_stat,p_value = f_oneway(group_a,group_b,group_c)

#print results
print(f"F-statistics:{f_stat:.4f}")
print(f"P_value:{p_value:.4f}")

#Significance level
alpha = 0.05

if p_value<alpha:
    print("Result:At least one group mean is significantly differenet")
else:
    print("Result:No significantly difference between group means")