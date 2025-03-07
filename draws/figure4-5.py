import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import matplotlib

# 设置中文字体支持
matplotlib.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'Microsoft YaHei']  # 用于显示中文标签
matplotlib.rcParams['axes.unicode_minus'] = False   # 正常显示负号

def create_waffle_chart():
    # 数据
    data = {'能够独立完成': 26, '需要协助或不会操作': 74}
    total = sum(data.values())
    
    # 设置网格大小和颜色
    grid_size = 10  # 10x10 网格
    colors = ['#66c2a5', '#fc8d62']
    
    # 创建瓦片图数据
    waffle_data = []
    for key, value in data.items():
        waffle_data.extend([key] * int(value / total * grid_size**2))
    
    # 创建网格矩阵
    waffle_matrix = np.array(waffle_data).reshape(grid_size, grid_size)
    
    # 绘制图形
    fig, ax = plt.subplots(figsize=(6, 6))
    color_map = {key: color for key, color in zip(data.keys(), colors)}
    
    for row in range(grid_size):
        for col in range(grid_size):
            category = waffle_matrix[row, col]
            ax.add_patch(Rectangle((col, grid_size - 1 - row), 1, 1, color=color_map[category]))
    
    # 添加标题和图例
    ax.set_title('农民短视频操作能力调查结果', fontsize=16, fontweight='bold')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, grid_size)
    ax.set_ylim(0, grid_size)
    
    legend_labels = [f'{key} ({value}%)' for key, value in data.items()]
    handles = [Rectangle((0, 0), 1, 1, color=color) for color in colors]
    ax.legend(handles, legend_labels, loc='upper left', fontsize=12)
    
    # 显示图表
    plt.tight_layout()
    plt.show()

# 调用函数生成瓦片图
create_waffle_chart()
