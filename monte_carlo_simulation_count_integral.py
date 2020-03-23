import random
import math
import sys

# use monte carlo simulation method to count integral of 'y = x^2' on [0, 1]

sample_num = 10000
if len(sys.argv) == 2:
    sample_num = (int)(sys.argv[1])

sample = [(random.uniform(0, 1), random.uniform(0, 1)) for i in range(sample_num)]

count_under_curve = 0.0

for i in range(sample_num):
    x_square = math.pow(sample[i][0], 2)
    y = sample[i][1]
    if y < x_square:
        count_under_curve += 1

print("count_under_curve: %d" % count_under_curve)
print("sample_num: %d" % sample_num)

integral_simulated = (count_under_curve / sample_num)
print("integral_simulated: " + str(integral_simulated))
