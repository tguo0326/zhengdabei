import matplotlib.pyplot as plt
import matplotlib

# 设置中文字体支持
matplotlib.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'Microsoft YaHei']  # 用于显示中文标签
matplotlib.rcParams['axes.unicode_minus'] = False   # 正常显示负号

# 数据
categories = ['全国平均', '云南某市']
values = [20, 35]

# 创建折线图
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(categories, values, marker='o', color='#FF7F50', linewidth=2.5, label='物流成本占比')

# 添加数据标签
for i, value in enumerate(values):
    ax.text(i, value + 1, f'{value}%', ha='center', fontsize=12)

# 设置标题和轴标签
ax.set_title('新鲜果蔬类物流成本占销售额比重对比', fontsize=14, weight='bold')
ax.set_ylabel('百分比 (%)', fontsize=12)
ax.set_ylim(0, 40)

# 美化图表
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.legend()

# 显示图表
plt.tight_layout()
plt.show()
