
"""
Solutions to module 4
Review date:
"""

student = "Renata Piatkova"
reviewer = ""


import random as r
import matplotlib.pyplot as plt 
import math

r.seed(1234)
# 1. Print the number of points nc that are inside the circle.
# 2. Print the approximation of π≈4nc/n.
# 3. Print the builtin constant π (math.pi) of Python.
# 4. Produceapng filethatshowsallpointsinsidethecircleasreddotsandpointsoutside
# the circle as blue dots (like in Figure 2).

def approximate_pi(n):
    x = []
    y =[]
    circle = []
    for i in range(n):
        x_point = r.uniform(-1, 1)
        x.append(x_point)
        y_point = r.uniform(-1, 1)
        y.append(y_point)
        if x_point**2 + y_point**2 <= 1:
            circle.append((x_point, y_point))
    plt.scatter(x, y, color='blue', s=1, label='All Points')
    
    circle_x, circle_y = zip(*circle)  
    # The zip(*circle) expression "unzips" the list of tuples into two separate sequences.
    # The asterisk (*) operator is used to unpack the list of tuples into individual elements.
    # The function zip groups the first elements of each tuple into one sequence (which will be circle_x),
    # and the second elements into another sequence (which will be circle_y).

    plt.scatter(circle_x, circle_y, color='red', s=1, label='Inside Circle')  # inside the circle
    plt.title(f'Monte Carlo Approximation with {n} points')
    plt.legend()
    plt.show()
    
         
    return 4*(len(circle)/n)
    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        pi= approximate_pi(n) #dots_in_circle
        print(# f'There are {dots_in_circle} points inside the circle.\n'
                f'The approximation of π is {pi}.\n'
                f'The actual value of π is {math.pi}.\n')
        


if __name__ == '__main__':
	main()
