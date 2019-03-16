import pygal

from die import Die

#创建两个D6
die1 =Die()
die2 =Die()

#掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(2, die1.num_sides*2 +1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling two D6 1000 times."
hist.x_labels =[str(x_label_num) for x_label_num in range(1, die1.num_sides*2+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
