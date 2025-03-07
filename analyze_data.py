import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import os
warnings.filterwarnings('ignore')

print("开始数据分析...")

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # MacOS
plt.rcParams['axes.unicode_minus'] = False

try:
    # 读取数据
    print("正在读取数据...")
    df = pd.read_csv('result.csv')
    print(f"成功读取数据，共 {len(df)} 行")

    # 1. 相关性分析
    print("正在进行相关性分析...")
    correlation_matrix = df.corr()

    # 绘制相关性热力图
    print("正在生成相关性热力图...")
    plt.figure(figsize=(15, 12))
    plt.imshow(correlation_matrix, cmap='coolwarm', aspect='auto')
    plt.colorbar()
    plt.title('变量相关性热力图')
    plt.tight_layout()
    plt.savefig('correlation_heatmap.png')
    plt.close()
    print("相关性热力图已保存")

    # 分析强相关性
    print("\n分析强相关性关系...")
    strong_correlations = []
    for i in range(len(correlation_matrix.columns)):
        for j in range(i+1, len(correlation_matrix.columns)):
            corr_value = correlation_matrix.iloc[i, j]
            if abs(corr_value) > 0.3:  # 设置相关性阈值
                strong_correlations.append({
                    'var1': correlation_matrix.columns[i],
                    'var2': correlation_matrix.columns[j],
                    'correlation': corr_value
                })
    
    # 按相关性强度排序
    strong_correlations.sort(key=lambda x: abs(x['correlation']), reverse=True)

    # 2. 数据洞察分析
    print("正在生成基本统计信息...")
    basic_stats = df.describe()
    basic_stats.to_csv('basic_statistics.csv')
    print("基本统计信息已保存")

    # 2.2 各问题的回答分布
    print("正在生成各问题答案分布图...")
    for col in df.columns:
        if col not in ['来源', '来自IP']:  # 排除非问题列
            try:
                value_counts = df[col].value_counts()
                plt.figure(figsize=(10, 6))
                value_counts.plot(kind='bar')
                plt.title(f'{col}的答案分布')
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.savefig(f'distribution_{col}.png')
                plt.close()
            except Exception as e:
                print(f"处理列 {col} 时出错: {str(e)}")
    print("答案分布图已生成")

    # 3. 关键发现
    print("正在计算关键发现...")
    with open('analysis_report.txt', 'w', encoding='utf-8') as f:
        f.write("数据分析报告\n")
        f.write("=" * 50 + "\n\n")
        
        # 写入基本统计信息
        f.write("1. 基本统计信息\n")
        f.write("-" * 30 + "\n")
        f.write(f"总样本数：{len(df)}\n")
        f.write(f"问题数量：{len(df.columns) - 2}\n\n")
        
        # 写入关键发现
        f.write("2. 关键发现\n")
        f.write("-" * 30 + "\n")
        
        # 写入相关性分析结果
        f.write("\n2.1 变量相关性分析\n")
        f.write("-" * 30 + "\n")
        f.write("发现以下变量之间存在较强相关性（相关系数绝对值>0.3）：\n\n")
        
        for corr in strong_correlations:
            strength = "强" if abs(corr['correlation']) > 0.7 else "中等" if abs(corr['correlation']) > 0.5 else "弱"
            direction = "正" if corr['correlation'] > 0 else "负"
            f.write(f"{corr['var1']} 与 {corr['var2']} 之间存在{strength}的{direction}相关关系（相关系数：{corr['correlation']:.3f}）\n")
        
        # 分析政策了解程度与电商发展的关系
        if '1. 您是否了解云南的"三农"政策？' in df.columns and '7. 您认为云南的"三农"政策对电商发展的支持力度如何？' in df.columns:
            policy_correlation = df['1. 您是否了解云南的"三农"政策？'].corr(df['7. 您认为云南的"三农"政策对电商发展的支持力度如何？'])
            f.write(f"\n政策了解程度与电商发展支持力度的相关性：{policy_correlation:.3f}\n")
        
        # 分析抖音平台使用情况
        if '3. 您是否曾通过抖音平台购买过云南的农产品？' in df.columns:
            purchase_rate = (df['3. 您是否曾通过抖音平台购买过云南的农产品？'] == 1).mean() * 100
            f.write(f"通过抖音平台购买过云南农产品的比例：{purchase_rate:.2f}%\n")
        
        # 分析主要障碍
        if '9. 您认为云南乡村电商发展的主要障碍是什么？' in df.columns:
            f.write("\n电商发展主要障碍分布：\n")
            f.write(df['9. 您认为云南乡村电商发展的主要障碍是什么？'].value_counts().to_string())
        
        f.write("\n\n3. 建议\n")
        f.write("-" * 30 + "\n")
        f.write("基于数据分析结果，建议：\n")
        f.write("1. 加强政策宣传力度\n")
        f.write("2. 提升抖音平台运营质量\n")
        f.write("3. 解决物流和技术支持问题\n")
        f.write("4. 提供更多电商培训机会\n")
    print("分析报告已生成")

    print("\n分析完成！请查看生成的文件：")
    print("1. correlation_heatmap.png - 相关性热力图")
    print("2. basic_statistics.csv - 基本统计信息")
    print("3. distribution_*.png - 各问题答案分布图")
    print("4. analysis_report.txt - 详细分析报告")

except Exception as e:
    print(f"分析过程中出错: {str(e)}")
    raise 