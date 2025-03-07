import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# 设置中文字体支持
matplotlib.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'Microsoft YaHei']  # 用于显示中文标签
matplotlib.rcParams['axes.unicode_minus'] = False   # 正常显示负号

# 数据
data = {
    '年份': [2023, 2024, 2025],
    '农村快递包裹量（亿件）': [370, 400, 450],
    '增长率（%）': [11, 12, None],
    '农村覆盖率（%）': [None, None, 90],
    '主要快递企业覆盖率（%）': [None, None, 98],
    '物流时效缩短（小时）': [None, 48, None],
    '物流成本降低（%）': [None, 15, None],
    '农产品与工业品流通规模（万亿元）': [None, None, 2.3]
}

# 可视化农村快递包裹量和增长率
fig, ax1 = plt.subplots(figsize=(12, 8))

# 绘制柱状图：农村快递包裹量
ax1.bar(data['年份'], data['农村快递包裹量（亿件）'], color='#7CB9E8', label='农村快递包裹量（亿件）')
ax1.set_xlabel('年份', fontsize=14)
ax1.set_ylabel('农村快递包裹量（亿件）', fontsize=14, color='#4682B4')
ax1.tick_params(axis='y', labelcolor='#4682B4')

# 添加第二个y轴：增长率
ax2 = ax1.twinx()
ax2.plot(data['年份'], data['增长率（%）'], color='#DEB887', marker='o', label='增长率（%）')
ax2.set_ylabel('增长率（%）', fontsize=14, color='#8B4513')
ax2.tick_params(axis='y', labelcolor='#8B4513')

# 添加数据标签
for i, value in enumerate(data['农村快递包裹量（亿件）']):
    ax1.text(data['年份'][i], value + 5, f'{value}亿件', ha='center', fontsize=12, color='#4682B4')

for i, value in enumerate(data['增长率（%）']):
    if value is not None:
        ax2.text(data['年份'][i], value + 0.5, f'{value}%', ha='center', fontsize=12, color='#8B4513')

# 添加标题和图例
plt.title('农村物流趋势（2023-2025年）', fontsize=16)
fig.tight_layout()
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# 显示图表
plt.show()

# 创建一个新的图表，包含覆盖率和物流效率改善
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# 覆盖率图表
bar_width = 0.35
x = np.array([0])
ax1.bar(x - bar_width/2, [data['农村覆盖率（%）'][2]], bar_width, color='#A8D8B9', label='农村覆盖率')
ax1.bar(x + bar_width/2, [data['主要快递企业覆盖率（%）'][2]], bar_width, color='#E6BCB0', label='主要快递企业覆盖率')
ax1.set_title('2025年覆盖率情况', fontsize=14)
ax1.set_xticks([])
ax1.set_ylabel('百分比（%）')
ax1.legend()

# 在柱状图上添加数值标签
ax1.text(x - bar_width/2, data['农村覆盖率（%）'][2], f"{data['农村覆盖率（%）'][2]}%", 
         ha='center', va='bottom')
ax1.text(x + bar_width/2, data['主要快递企业覆盖率（%）'][2], f"{data['主要快递企业覆盖率（%）'][2]}%", 
         ha='center', va='bottom')

# 物流效率改善图表
bar_width = 0.35
x = np.array([0])
ax2.bar(x - bar_width/2, [data['物流时效缩短（小时）'][1]], bar_width, color='#B4C7E7', label='时效缩短（小时）')
ax2.bar(x + bar_width/2, [data['物流成本降低（%）'][1]], bar_width, color='#C3B1E1', label='成本降低（%）')
ax2.set_title('2024年物流效率改善情况', fontsize=14)
ax2.set_xticks([])
ax2.set_ylabel('数值')
ax2.legend()

# 在柱状图上添加数值标签
ax2.text(x - bar_width/2, data['物流时效缩短（小时）'][1], f"{data['物流时效缩短（小时）'][1]}小时", 
         ha='center', va='bottom')
ax2.text(x + bar_width/2, data['物流成本降低（%）'][1], f"{data['物流成本降低（%）'][1]}%", 
         ha='center', va='bottom')

plt.tight_layout()
plt.show()
