import matplotlib.pyplot as plt
import matplotlib

# 设置中文字体支持
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
matplotlib.rcParams['axes.unicode_minus'] = False

# 数据
categories = ['农产品销售快速增长', '本地农民转型为主播']
percentages = [76, 24]
colors = ['#66c2a5', '#fc8d62']  # 高对比度配色
explode = (0.1, 0)  # 突出第一个扇区

# 创建饼图
plt.figure(figsize=(8, 8))
wedges, texts, autotexts = plt.pie(
    percentages,
    labels=categories,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    wedgeprops={'edgecolor': 'white', 'linewidth': 1.5},  # 添加白色边界线
    textprops={'fontsize': 12}
)

# 调整标签和百分比位置
for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(12)

# 添加标题
plt.title('抖音直播带货经济拉动的数据分析', fontsize=16, fontweight='bold')

# 显示图表
plt.tight_layout()
plt.show()
