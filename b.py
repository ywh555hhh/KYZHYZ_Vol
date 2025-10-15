import json
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

with open('netem_full_list.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
words = data["5530考研词汇词频排序表"]

# 统计每个词频对应的单词数量
freq_counter = Counter()
for item in words:
    freq = item.get("词频")
    if freq is not None:
        freq_counter[freq] += 1

# 只显示词频在1~50的区间，便于观察主流分布
x = [freq for freq in range(1, 400)]
y = [freq_counter.get(freq, 0) for freq in x]

plt.figure(figsize=(14, 6))
plt.bar(x, y, width=0.8, color='#4A90E2')
plt.xlabel('词频', fontsize=14)
plt.ylabel('单词数', fontsize=14)
plt.title('词频1~50区间的单词数量分布', fontsize=16)
plt.xticks(x)
plt.tight_layout()
plt.show()

# 如果想看全区间分布（对数坐标，适合长尾），可取消注释
# x_all = sorted(freq_counter.keys())
# y_all = [freq_counter[f] for f in x_all]
# plt.figure(figsize=(14, 6))
# plt.bar(x_all, y_all, width=0.8, color='#E94E77')
# plt.xlabel('词频', fontsize=14)
# plt.ylabel('单词数', fontsize=14)
# plt.title('所有词频的单词数量分布（对数Y轴）', fontsize=16)
# plt.yscale('log')
# plt.tight_layout()
# plt.show()
