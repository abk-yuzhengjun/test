import pandas as pd
import matplotlib.pyplot as plt

catering_sale = r'F:\resource\data-analysis\data_exploratory\data\catering_sale.xls'
data = pd.read_excel(catering_sale, index_col=u'日期')
print(len(data))
print(data.describe())

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 建立图像
plt.figure()
p = data.boxplot(return_type='dict')
x = p['fliers'][0].get_xdata()
y = p['fliers'][0].get_ydata()

y.sort()

# 用annotate添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

plt.show()
