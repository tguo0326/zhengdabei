import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # macOS 系统预装的支持中文的字体
plt.rcParams['axes.unicode_minus'] = False   # 正常显示负号

# 创建字体对象
font = FontProperties(family='Arial Unicode MS')

# 数据准备
years = ['2023', '2024', '2025']
total_retail = [6100, None, 7200]  # 2024年的数据暂未提供
fresh_retail_ratio = [None, None, 35]  # 生鲜农产品网络零售额占比
prepared_retail = [1200, 1500, None]  # 预制菜类农产品网络零售额

# 插值计算2024年的总零售额
total_retail[1] = total_retail[0] * (1 + 0.15) * (1 + 0.18) ** 0.5

# 计算2024年的生鲜农产品网络零售额占比（假设逐渐增加）
fresh_retail_ratio[0] = 30  # 假设2023年的占比
fresh_retail_ratio[1] = (fresh_retail_ratio[0] + fresh_retail_ratio[2]) / 2

# 计算2025年的预制菜类农产品网络零售额（假设继续增长）
prepared_retail[2] = prepared_retail[1] * (1 + 0.25)

# 创建图表
fig, axs = plt.subplots(2, figsize=(8, 6))

# 第一个子图：全国农产品网络零售额
axs[0].plot(years, total_retail, marker='o')
axs[0].set_title('全国农产品网络零售额（亿元）', fontproperties=font, fontsize=12)
axs[0].set_xlabel('年份', fontproperties=font, fontsize=10)
axs[0].set_ylabel('零售额（亿元）', fontproperties=font, fontsize=10)

# 第二个子图：预制菜类农产品网络零售额
axs[1].plot(years, prepared_retail, marker='o')
axs[1].set_title('预制菜类农产品网络零售额（亿元）', fontproperties=font, fontsize=12)
axs[1].set_xlabel('年份', fontproperties=font, fontsize=10)
axs[1].set_ylabel('零售额（亿元）', fontproperties=font, fontsize=10)

# 添加生鲜农产品网络零售额占比信息
ax2 = axs[0].twinx()
ax2.plot(years, fresh_retail_ratio, color='r', linestyle='--', marker='s')
ax2.set_ylabel('生鲜农产品占比（%）', color='r', fontproperties=font, fontsize=10)
ax2.tick_params(axis='y', labelcolor='r')

# 布局调整
plt.tight_layout()

plt.show()
