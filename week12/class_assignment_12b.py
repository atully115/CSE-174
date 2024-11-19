# Author: Ashton Tully
# Dr. Goodman
# 11/13/2024
# CSE 174 J
"""Practicing maxing a pie chart and plotting a graph"""

import matplotlib.pyplot as plt

def main():
    x_axis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y_axis = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    plt.plot(x_axis, y_axis)
    label = 'Part 1 graph'
    plt.title(label)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()
    
    labels = ['A', 'B', 'C', 'D', 'E']
    sizes = [10, 20, 30, 40, 50]
    colors = ['red', 'blue', 'green', 'yellow', 'orange']
    plt.pie(sizes, labels=labels, colors=colors)
    plt.legend(title='Legend')
    plt.show()
    
    
    
    with open('week12/hist_data.txt', 'r') as file:
        data = [float(line.strip()) for line in file]
        plt.hist(data, bins=8, range=(0, 50), color='red', rwidth=0.5)
        plt.xlabel('Prices')
        plt.ylabel('Number of Sales')
        plt.title('Part 3 Histogram Title')
        plt.show()

if __name__ == "__main__":
    main()

