
import pandas as pd
import numpy as np

data = pd.read_csv("GlobalLandTemperaturesByCity.csv")
print(data["AverageTemperature"].std())
averageTemp=data['AverageTemperature']
meanOfAvgTemp=np.mean(averageTemp)
print(meanOfAvgTemp)
# Filter values greater than the mean
greaterThanMean = averageTemp[averageTemp > meanOfAvgTemp]
# Print the filtered values
print("greater than mean",greaterThanMean)

"""import numpy as np
from scipy.stats import ttest_ind, alpha

#data for two groups
group_a = np.array([120,115,123,117,125])
group_b = np.array([130,132,128,135,140])

#perform an independent t-test
t_stat,p_value = ttest_ind(group_a,group_b)

#set significant level
alpha = 0.05

#display results
print(f"T-statistics:{t_stat:.4f}")
print(f"P_value:{p_value:.4f}")

if p_value<alpha:
    print("Result:Statistically significant(reject the null hypothesis)")
else:
    print("Result:Not statistically significant(fail to reject the null hypothesis)")"""

