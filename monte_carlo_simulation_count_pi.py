import random
import math
import sys

sample_num = 10000
if len(sys.argv) == 2:
    sample_num = (int)(sys.argv[1])

sample = [(random.uniform(-2, 2), random.uniform(-2, 2)) for i in range(sample_num)]
count_in_circle = 0.0

for i in range(sample_num):
    x_square = math.pow(sample[i][0], 2)
    y_square = math.pow(sample[i][1], 2)
    distance = math.sqrt(x_square + y_square)
    if distance <= 2:
        count_in_circle += 1

print("count_in_circle: %d" % count_in_circle)
print("sample_num: %d" % sample_num)

pi_simulated = 4 * (count_in_circle / sample_num)
print("pi_simulated: " + str(pi_simulated))
