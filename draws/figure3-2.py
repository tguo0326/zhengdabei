import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib

# 设置中文字体支持
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams['font.size'] = 12  # 设置全局字体大小

# 数据准备
years = np.array([2018, 2019, 2020, 2021, 2022])
product_1_sales = np.array([100, 110, 120, 130, 150])  # 产品1的销量
product_2_sales = np.array([80, 90, 110, 120, 140])  # 产品2的销量

# 设置柱子的位置
x = np.arange(len(years))  # x轴位置
y1 = -0.15  # 产品1的偏移位置
y2 = 0.15   # 产品2的偏移位置

# 图形初始化
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# 设置视角和图表范围
ax.view_init(elev=25, azim=45)
ax.set_box_aspect([2, 1, 1])  # 设置图表的长宽高比例

# 绘制柱状图，统一设置柱子的宽度、深度和颜色
width = 0.25  # 增加柱子宽度
depth = 0.4  # 增加柱子深度

# 为柱子添加3D效果
for i, (height1, height2) in enumerate(zip(product_1_sales, product_2_sales)):
    # 产品1的柱子（蓝色）
    xx = [x[i] + y1 - width/2, x[i] + y1 + width/2, x[i] + y1 + width/2, x[i] + y1 - width/2]
    yy = [0, 0, depth, depth]
    zz = [0, 0, 0, 0]
    verts = [list(zip(xx, yy, zz))]
    ax.add_collection3d(Poly3DCollection(verts, facecolors='royalblue', alpha=0.9))
    
    xx = [x[i] + y1 - width/2, x[i] + y1 - width/2, x[i] + y1 - width/2, x[i] + y1 - width/2]
    yy = [0, 0, depth, depth]
    zz = [0, height1, height1, 0]
    verts = [list(zip(xx, yy, zz))]
    ax.add_collection3d(Poly3DCollection(verts, facecolors='royalblue', alpha=0.7))
    
    ax.bar3d(x[i] + y1 - width/2, 0, 0, width, depth, height1, color='royalblue', alpha=0.9, label='产品1' if i == 0 else "")
    
    # 产品2的柱子（红色）
    xx = [x[i] + y2 - width/2, x[i] + y2 + width/2, x[i] + y2 + width/2, x[i] + y2 - width/2]
    yy = [0, 0, depth, depth]
    zz = [0, 0, 0, 0]
    verts = [list(zip(xx, yy, zz))]
    ax.add_collection3d(Poly3DCollection(verts, facecolors='crimson', alpha=0.9))
    
    xx = [x[i] + y2 - width/2, x[i] + y2 - width/2, x[i] + y2 - width/2, x[i] + y2 - width/2]
    yy = [0, 0, depth, depth]
    zz = [0, height2, height2, 0]
    verts = [list(zip(xx, yy, zz))]
    ax.add_collection3d(Poly3DCollection(verts, facecolors='crimson', alpha=0.7))
    
    ax.bar3d(x[i] + y2 - width/2, 0, 0, width, depth, height2, color='crimson', alpha=0.9, label='产品2' if i == 0 else "")

# 添加网格线增强3D效果
ax.grid(True, linestyle='--', alpha=0.4)

# 设置坐标轴范围和刻度
ax.set_xlim(-0.5, len(years) - 0.5)
ax.set_ylim(-0.5, 0.5)
ax.set_zlim(0, 200)

# 设置轴标签和标题
ax.set_xlabel('年份', fontsize=12)
ax.set_ylabel('产品', fontsize=12)
ax.set_zlabel('销量', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=10)
ax.set_yticks([-0.15, 0.15])
ax.set_yticklabels(['产品1', '产品2'], fontsize=10)
ax.set_zticks(np.arange(0, 201, 25))  # 设置Z轴刻度间隔为25
ax.set_title('云南特色农产品销量增长', fontsize=14, pad=20)  # 增加标题的字体大小和上边距

# 添加图例
ax.legend()

# 调整布局
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

# 显示图形
plt.show()
