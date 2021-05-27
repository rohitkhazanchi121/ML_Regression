import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

IceCream = pd.read_csv('IceCreamData.csv')

## Prints the IceCream Dataframe created by reading IceCreamData CSV file
print(IceCream)


print(IceCream.describe())