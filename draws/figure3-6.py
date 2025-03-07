import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# 设置中文字体支持
matplotlib.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'Microsoft YaHei']  # 用于显示中文标签
matplotlib.rcParams['axes.unicode_minus'] = False   # 正常显示负号

# 数据
labels = ['抖音推广成功案例', '其他推广成功案例', '滞销案例']
data = [88, 12, 0]  # 对应描述中的数据

# 转换数据为闭合形式
data += data[:1]

# 设置角度
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
angles += angles[:1]

# 绘制雷达图
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, data, color='blue', alpha=0.25)
ax.plot(angles, data, color='blue', linewidth=2)

# 添加标签和标题
ax.set_yticks([20, 40, 60, 80])
ax.set_yticklabels(['20', '40', '60', '80'], color="grey", size=10)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=12)
plt.title('云南农产品销量增长案例分布', fontsize=14)

# 显示图表
plt.tight_layout()
plt.show()
