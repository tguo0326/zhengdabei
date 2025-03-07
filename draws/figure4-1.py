import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# 设置中文字体支持
matplotlib.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'Microsoft YaHei']  # 用于显示中文标签
matplotlib.rcParams['axes.unicode_minus'] = False   # 正常显示负号

# 数据
categories = ['高质量，剪辑流畅', '画质较差，内容冗长']
percentages = [64, 18]
colors = ['#4CAF50', '#FF5722']

# 创建图表
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制柱状图
bars = ax.bar(categories, percentages, color=colors, edgecolor='black', linewidth=1.2)

# 添加数据标签
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 2, f'{height}%', ha='center', fontsize=12, fontweight='bold')

# 添加标题和标签
ax.set_title('消费者对视频质量与长度的偏好', fontsize=16, fontweight='bold')
ax.set_ylabel('百分比 (%)', fontsize=14)
ax.set_ylim(0, 80)

# 添加网格线以提高可读性
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# 美化外观
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 显示图表
plt.tight_layout()
plt.show()
