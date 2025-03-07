import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # macOS 系统预装的支持中文的字体
plt.rcParams['axes.unicode_minus'] = False   # 正常显示负号

def plot_progress_chart():
    # 数据
    categories = ['缺乏专业运营人员', '拥有专职电商团队']
    values = [76, 24]
    colors = ['#E6BCB0', '#A8D8B9']  # 更柔和的配色

    # 创建画布
    plt.figure(figsize=(10, 6))
    
    # 绘制水平条形图
    bars = plt.barh(categories, values, color=colors, height=0.5)
    
    # 添加数据标签
    for bar in bars:
        width = bar.get_width()
        plt.text(width + 1, bar.get_y() + bar.get_height()/2, 
                f'{width}%', va='center', ha='left', fontsize=11)
    
    # 设置图表样式
    plt.xlim(0, 100)
    plt.xlabel('占比（%）', fontsize=12)
    plt.title('云南某县农产品电商店铺专业运营人员情况', fontsize=14, pad=15)
    
    # 添加网格线
    plt.grid(axis='x', linestyle='--', alpha=0.3)
    
    # 移除上边框和右边框
    sns.despine(right=True, top=True)
    
    # 设置y轴标签字体大小
    plt.tick_params(axis='y', labelsize=11)
    
    # 调整布局
    plt.tight_layout()
    
    # 显示图表
    plt.show()

if __name__ == '__main__':
    plot_progress_chart()
