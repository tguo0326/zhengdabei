import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib
from matplotlib.font_manager import FontProperties

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # macOS 系统预装的支持中文的字体
plt.rcParams['axes.unicode_minus'] = False   # 正常显示负号

# 创建字体对象
font = FontProperties(family='Arial Unicode MS')

# 数据准备
labels = ['冷链覆盖', '非冷链覆盖']
sizes = [40, 60]  # 假设全国冷链覆盖率为40%
colors = ['#4CAF50', '#FF9800']

# 创建饼图
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
wedges, texts, autotexts = plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', 
                                  shadow=True, startangle=90)

# 设置饼图标签的字体
for text in texts:
    text.set_fontproperties(font)
    
plt.title('全国农产品冷链覆盖率', fontproperties=font, fontsize=12)

# 条形图数据
years = ['2023', '2024', '2025']
market_sizes = [4700, 5200, 6000]  # 假设2024年市场规模为5200亿元

# 创建条形图
plt.subplot(1, 2, 2)
sns.set_style('whitegrid')
plt.bar(years, market_sizes, color='#03A9F4')
plt.title('冷链物流市场规模（亿元）', fontproperties=font, fontsize=12)
plt.xlabel('年份', fontproperties=font, fontsize=10)
plt.ylabel('市场规模（亿元）', fontproperties=font, fontsize=10)

# 为饼图的图例设置中文字体
ax1 = plt.gcf().axes[0]
legend = ax1.get_legend()
if legend:
    for text in legend.get_texts():
        text.set_fontproperties(font)

plt.tight_layout()
plt.show()
