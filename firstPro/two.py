"""
name:
date:
author:
function:
"""

import pandas as pd
import matplotlib.pyplot as plt

catering_sale = r'F:\resource\data-analysis\data_exploratory\data\catering_dish_profit.xls'
data = pd.read_excel(catering_sale, index_col=u'日期')
data = data[(data[u'销量']>400) & (data[u'销量']<5000)]
statistics = data.describe()
statistics.loc['range'] = statistics.loc['max'] - statistics.loc['min']
statistics.loc['var'] = statistics.loc['std'] / statistics.loc['mean']
statistics.loc['dis'] = statistics.loc['75%'] - statistics.loc['25%']
print(statistics)








