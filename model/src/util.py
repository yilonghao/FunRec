# encoding: utf-8

"""
@author: yilonghao
@file: util.py
"""

def cal_auc(data):
    """
    计算 AUC 值。
    
    Args:
        data (dict): 包含多个键值对的字典，键为分数，值为一个包含两个元素的元组，分别表示正样本和负样本的数量。
    
    Returns:
        float: AUC 值，保留 5 位小数。
    
    """
    """"""
    data_sort = sorted(data.items(), key=lambda x: x[0], reverse=True)
    ack = [x[1][1] for x in data_sort]
    clk = [x[1][2] for x in data_sort]
    sample_num = sum(ack)
    pos = sum(clk)
    neg = sample_num - pos
    if pos < 1 or neg < 1:
        return 0
    roc_arr = []
    tp = fp = 0
    for i, j in zip(ack, clk):
        tp += j
        fp += (i - j)
        roc_arr.append((float(fp) / neg, float(tp) / pos))
    auc = 0
    prev_x = 0
    for x, y in roc_arr:
        auc += (x - prev_x) * y
        prev_x = x
    return round(auc, 5)


if __name__ == "__main__":
    data = {
    "0.95": [0, 1, 1],
    "0.90": [0, 1, 1],
    "0.80": [0, 1, 1],
    "0.70": [0, 1, 0],
    "0.60": [0, 1, 0],
    "0.50": [0, 1, 0],
    "0.40": [0, 1, 1],
    "0.30": [0, 1, 0],
    "0.20": [0, 1, 0],
    "0.10": [0, 1, 0]
    }
    print(cal_auc(data))