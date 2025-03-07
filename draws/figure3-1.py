import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib

# 设置中文字体支持
matplotlib.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'Microsoft YaHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# Data for the pie chart
labels = ['快速增长', '直播间高效转化', '其他']
sizes = [64, 18, 100 - 64 - 18]  # Percentages
colors = ['#ff9999', '#66b3ff', '#99ff99']
explode = (0.1, 0.1, 0)  # Explode the first two slices

# Create a figure and axis for the pie chart
fig, ax = plt.subplots(figsize=(8, 6))

# Create the pie chart
wedges, texts, autotexts = ax.pie(
    sizes,
    explode=explode,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.85,
    wedgeprops={'edgecolor': 'w'}
)

# Add a circle at the center to give a "3D-like" effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Customize text properties
for text in texts + autotexts:
    text.set_color('black')
    text.set_fontsize(10)  # 设置字体大小

# Set title
ax.set_title('云南特色农产品推广案例销售数据', pad=20, fontsize=12)

# 如果在支持图形界面的环境中，也可以显示图表
try:
    plt.show()
except Exception as e:
    print(f"无法显示图表: {e}")
