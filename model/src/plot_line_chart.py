# encoding: utf-8

import matplotlib.pyplot as plt
import numpy as np


def plot_line_chart(x_values, y_values_list, labels, title, xlabel, ylabel):
    """
    创建折线图

    参数：
    - x_values: x轴数据
    - y_values_list: y轴数据列表，每个列表对应一个折线
    - labels: 折线的标签列表
    - title: 图表标题
    - xlabel: x轴标签
    - ylabel: y轴标签
    """
    plt.figure(figsize=(10, 6))

    for y_values, label in zip(y_values_list, labels):
        plt.plot(x_values, y_values, label=label)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # 示例数据
    x_values = np.linspace(0, 10, 100)
    y_values_list = [np.sin(x_values), np.cos(x_values), np.tan(x_values)]
    labels = ['sin(x)', 'cos(x)', 'tan(x)']
    title = 'Trigonometric Functions'
    xlabel = 'x'
    ylabel = 'Function Value'

    # 创建折线图
    plot_line_chart(x_values, y_values_list, labels, title, xlabel, ylabel)
