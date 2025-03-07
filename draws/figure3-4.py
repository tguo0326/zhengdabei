import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# 设置中文字体支持
matplotlib.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'Microsoft YaHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 模拟云南直播带货就业与销量增长数据
x = np.arange(1, 51)  # 50个案例编号
employment_growth = np.random.uniform(5, 20, size=50)  # 模拟就业增长百分比
sales_growth = np.random.uniform(10, 50, size=50)  # 模拟销量增长百分比

# 创建折线图
plt.figure(figsize=(12, 6))
plt.plot(x, employment_growth, label='就业增长率 (%)', linewidth=2.5, color='#1f77b4', marker='o')
plt.plot(x, sales_growth, label='销量增长率 (%)', linewidth=2.5, color='#ff7f0e', marker='s')

# 添加标题和坐标轴标签
plt.title('云南直播电商：就业与销量增长趋势', fontsize=16, fontweight='bold')
plt.xlabel('案例编号', fontsize=14)
plt.ylabel('增长百分比 (%)', fontsize=14)

# 自定义网格和图例
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(fontsize=12, loc='upper left')

# 美化图表
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()

# 显示图表
plt.show()
