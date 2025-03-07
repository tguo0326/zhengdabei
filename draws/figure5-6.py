import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # macOS 系统预装的支持中文的字体
plt.rcParams['axes.unicode_minus'] = False   # 正常显示负号

# 数据准备
years = ['2023', '2024', '2025']
station_counts = [180000, 185000, 200000]
coverage_rates = [85, 87.5, 92]

# 创建图表
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# 第一个子图：服务站点数量
ax1.plot(years, station_counts, marker='o', label='服务站点数量')
ax1.set_title('村级电商服务站点数量增长', fontsize=12)
ax1.set_xlabel('年份', fontsize=10)
ax1.set_ylabel('站点数量（个）', fontsize=10)
ax1.legend()

# 第二个子图：覆盖率
ax2.plot(years, coverage_rates, marker='o', label='覆盖率')
ax2.set_title('服务覆盖率提升', fontsize=12)
ax2.set_xlabel('年份', fontsize=10)
ax2.set_ylabel('覆盖率（%）', fontsize=10)
ax2.legend()

# 添加数据标签
for i, value in enumerate(station_counts):
    ax1.text(i, value, f'{value:,}', ha='center', va='bottom')
    
for i, value in enumerate(coverage_rates):
    ax2.text(i, value, f'{value}%', ha='center', va='bottom')

# 布局调整
plt.tight_layout()

# 显示图表
plt.show()
