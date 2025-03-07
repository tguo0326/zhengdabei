import matplotlib.pyplot as plt
import matplotlib

# 设置中文字体支持
matplotlib.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'Microsoft YaHei']  # 用于显示中文标签
matplotlib.rcParams['axes.unicode_minus'] = False   # 正常显示负号

# 数据
total_products = 100
branded = 12
non_branded = total_products - branded

# 标签和比例
labels = ['品牌化 (12)', '非品牌化 (88)']
sizes = [branded, non_branded]
colors = ['#4CAF50', '#FFC107']  # 使用绿色和黄色的配色
explode = (0.1, 0)  # 突出显示品牌化部分

# 创建饼图
fig, ax = plt.subplots(figsize=(10, 6))
wedges, texts, autotexts = ax.pie(
    sizes,
    explode=explode,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    shadow=True,
    startangle=90,
    textprops={'fontsize': 12}
)

# 设置标题
ax.set_title('云南地区农产品品牌化与非品牌化分布', fontsize=16, weight='bold')

# 添加图例
ax.legend(wedges, labels, title="类别", loc="center left", bbox_to_anchor=(1, 0.5))

# 调整布局并显示图表
plt.tight_layout()
plt.show()
