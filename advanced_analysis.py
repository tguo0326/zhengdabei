import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
import warnings
import os
from sklearn.preprocessing import StandardScaler
import plotly.express as px
import plotly.graph_objects as go
warnings.filterwarnings('ignore')

print("开始高级数据分析...")

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # MacOS
plt.rcParams['axes.unicode_minus'] = False

try:
    # 读取数据
    print("正在读取数据...")
    df = pd.read_csv('result.csv')
    print(f"成功读取数据，共 {len(df)} 行")
    print("数据列名：", df.columns.tolist())

    # 1. 高级数据洞察
    print("\n1. 生成高级数据洞察...")
    
    # 1.1 多维度分析
    # 选择数值型列
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    numeric_cols = [col for col in numeric_cols if col not in ['来源', '来自IP']]
    print("数值型列：", numeric_cols)
    
    # 计算每个问题的回答分布
    response_distributions = {}
    for col in numeric_cols:
        response_distributions[col] = df[col].value_counts(normalize=True).round(3) * 100
        print(f"\n{col}的分布：")
        print(response_distributions[col])
    
    # 1.2 生成交互式可视化
    print("\n正在生成交互式可视化...")
    
    # 创建目标变量（是否购买过农产品）
    target_col = '3. 您是否曾通过抖音平台购买过云南的农产品？ '
    if target_col not in df.columns:
        raise ValueError(f"目标变量 {target_col} 不存在")
    target = df[target_col]
    print(f"目标变量分布：\n{target.value_counts(normalize=True).round(3) * 100}")
    
    # 选择特征变量（排除目标变量和无关列）
    feature_cols = [col for col in numeric_cols if col != target_col]
    print("\n特征变量：", feature_cols)
    
    # 准备数据
    X = df[feature_cols]
    y = target
    
    # 处理缺失值
    print("\n正在处理缺失值...")
    X = X.fillna(X.mean())
    
    # 数据标准化
    print("正在进行数据标准化...")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # 2. 机器学习模型分析
    print("\n2. 训练随机森林模型...")
    
    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    print(f"训练集大小：{len(X_train)}, 测试集大小：{len(X_test)}")
    
    # 训练随机森林模型
    print("正在训练模型...")
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    
    # 预测和评估
    print("正在进行预测和评估...")
    y_pred = rf_model.predict(X_test)
    y_pred_proba = rf_model.predict_proba(X_test)[:, 1]
    
    # 生成特征重要性
    print("正在计算特征重要性...")
    feature_importance = pd.DataFrame({
        'feature': feature_cols,
        'importance': rf_model.feature_importances_
    }).sort_values('importance', ascending=False)
    print("\n特征重要性：")
    print(feature_importance)
    
    # 创建特征重要性可视化
    print("正在生成特征重要性可视化...")
    fig = px.bar(feature_importance, x='importance', y='feature',
                title='特征重要性分析',
                labels={'importance': '重要性得分', 'feature': '特征'})
    fig.write_html('feature_importance.html')
    print("特征重要性可视化已保存")
    
    # 创建混淆矩阵可视化
    print("正在生成混淆矩阵可视化...")
    cm = confusion_matrix(y_test, y_pred)
    fig_cm = go.Figure(data=go.Heatmap(
        z=cm,
        x=['否', '是'],
        y=['否', '是'],
        text=cm,
        texttemplate='%{text}',
        textfont={"size": 16},
        hoverongaps=False,
        colorscale='Reds',
        showscale=True,
        colorbar_title='数量'
    ))
    fig_cm.update_layout(
        title='随机森林模型混淆矩阵',
        xaxis_title='预测值',
        yaxis_title='真实值',
        width=800,
        height=600
    )
    fig_cm.write_html('confusion_matrix.html')
    print("混淆矩阵可视化已保存")
    
    # 创建ROC曲线可视化
    print("正在生成ROC曲线可视化...")
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    roc_auc = auc(fpr, tpr)
    
    fig_roc = go.Figure()
    fig_roc.add_trace(go.Scatter(
        x=fpr,
        y=tpr,
        mode='lines',
        name=f'ROC曲线 (AUC = {roc_auc:.2f})'
    ))
    fig_roc.add_trace(go.Scatter(
        x=[0, 1],
        y=[0, 1],
        mode='lines',
        name='随机猜测',
        line=dict(dash='dash')
    ))
    fig_roc.update_layout(
        title='随机森林模型ROC曲线',
        xaxis_title='假正率 (FPR)',
        yaxis_title='真正率 (TPR)',
        width=800,
        height=600
    )
    fig_roc.write_html('roc_curve.html')
    print("ROC曲线可视化已保存")
    
    # 3. 生成高级分析报告
    print("\n3. 生成高级分析报告...")
    with open('advanced_analysis_report.txt', 'w', encoding='utf-8') as f:
        f.write("高级数据分析报告\n")
        f.write("=" * 50 + "\n\n")
        
        # 写入模型评估结果
        f.write("1. 随机森林模型评估\n")
        f.write("-" * 30 + "\n")
        f.write(classification_report(y_test, y_pred))
        f.write(f"\nROC曲线下面积 (AUC): {roc_auc:.4f}\n")
        
        # 写入特征重要性
        f.write("\n2. 特征重要性分析\n")
        f.write("-" * 30 + "\n")
        for _, row in feature_importance.iterrows():
            f.write(f"{row['feature']}: {row['importance']:.4f}\n")
        
        # 写入关键洞察
        f.write("\n3. 关键数据洞察\n")
        f.write("-" * 30 + "\n")
        
        # 分析购买行为的影响因素
        f.write("\n3.1 购买行为影响因素分析\n")
        top_features = feature_importance.head(5)
        f.write("影响购买行为最重要的5个因素是：\n")
        for _, row in top_features.iterrows():
            f.write(f"- {row['feature']} (重要性：{row['importance']:.4f})\n")
        
        # 分析用户群体特征
        f.write("\n3.2 用户群体特征分析\n")
        for col in numeric_cols:
            if col != target_col:
                mean_value = df[col].mean()
                f.write(f"{col}的平均得分：{mean_value:.2f}\n")
        
        # 写入建议
        f.write("\n4. 基于机器学习的建议\n")
        f.write("-" * 30 + "\n")
        f.write("基于模型分析结果，建议：\n")
        f.write("1. 重点关注影响购买决策的关键因素\n")
        f.write("2. 针对不同用户群体制定差异化策略\n")
        f.write("3. 优化产品展示和营销方式\n")
        f.write("4. 加强用户教育和引导\n")
    
    print("高级分析报告已生成")

    print("\n高级分析完成！请查看生成的文件：")
    print("1. feature_importance.html - 特征重要性可视化")
    print("2. confusion_matrix.html - 混淆矩阵可视化")
    print("3. roc_curve.html - ROC曲线可视化")
    print("4. advanced_analysis_report.txt - 高级分析报告")

except Exception as e:
    print(f"分析过程中出错: {str(e)}")
    import traceback
    print(traceback.format_exc())
    raise 