import matplotlib.pyplot as plt
import matplotlib

# 设置中文字体支持
matplotlib.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'Microsoft YaHei']  # 用于显示中文标签
matplotlib.rcParams['axes.unicode_minus'] = False   # 正常显示负号

# 数据
labels = ['文化认同 (26%)', '本地特色农产品购买倾向 (74%)']
sizes = [26, 74]
colors = ['#ff9999', '#66b3ff']  # 配色
explode = (0.1, 0)  # 突出显示第一部分

# 绘制饼图
plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', 
        startangle=140, shadow=True)
plt.title('云南文化认同与本地特色农产品购买倾向', fontsize=16, fontweight='bold')

# 显示图表
plt.show()
