import pandas as pd
import numpy as np

# 读取CSV文件
df = pd.read_csv('正大杯-小组课题-S2-数据处理-600-1.csv')

# 删除前两列和最后两列
df = df.iloc[:, 2:-2]

# 将ABCD答案转换为1234
answer_mapping = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
for col in df.columns:
    if df[col].dtype == 'object':
        # 提取答案字母（A、B、C、D）
        df[col] = df[col].str.extract(r'^([A-D])')
        # 只对包含A-D的列进行转换
        if df[col].str.contains('^[A-D]$', na=False).any():
            df[col] = df[col].map(answer_mapping)

# 处理多选列
multi_choice_col = '您最关注云南农产品的哪些方面'
if multi_choice_col in df.columns:
    # 创建新的列来存储每个选项
    options = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    for option in options:
        new_col_name = f'{multi_choice_col}_{option}'
        df[new_col_name] = df[multi_choice_col].apply(lambda x: 1 if option in str(x) else 0)
    
    # 删除原始多选列
    df = df.drop(columns=[multi_choice_col])

# 保存处理后的结果
df.to_csv('result.csv', index=False)
print("数据处理完成，结果已保存到 result.csv") 