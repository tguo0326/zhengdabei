import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

# 设置中文字体和全局参数
rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'Microsoft YaHei']  # 用于显示中文标签
rcParams['axes.unicode_minus'] = False   # 正常显示负号

# 数据
products = ['茶叶', '咖啡', '水果', '蔬菜', '肉类']
sales_before = np.array([100, 120, 150, 180, 200])  # 推广前销量
sales_after = np.array([150, 180, 220, 250, 280])   # 推广后销量

# 创建条形图
plt.figure(figsize=(10, 6))
bar_width = 0.4
x = np.arange(len(products))

# 绘制双柱图
plt.bar(x - bar_width / 2, sales_before, width=bar_width, label='推广前', color='skyblue', alpha=0.8)
plt.bar(x + bar_width / 2, sales_after, width=bar_width, label='推广后', color='orange', alpha=0.8)

# 设置标题和标签
plt.xticks(x, products, fontsize=12)
plt.xlabel('农产品', fontsize=14)
plt.ylabel('销量', fontsize=14)
plt.title('抖音平台对云南农产品销路的促进', fontsize=16)
plt.legend(fontsize=12)

# 添加网格线和美化布局
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# 显示图表
plt.show()
