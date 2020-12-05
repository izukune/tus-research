import numpy as np
import matplotlib.pyplot as plt

input_data = np.arange(0, np.pi*2, 0.1)
correct_data = np.sin(input_data)
input_data = (input_data - np.pi) / np.pi
n_data = len(correct_data)

n_in = 1
n_mid = 3
n_out = 1

wb_width = 0.01
eta = 0.1
epoch = 2001
interval = 200

class MiddleLayer:
    def __init__(self, n_upper, n):
        self.w = wb_width * np.random.randn(n_upper, n)
        self.b = wb_width * np.random.randn(n)
    def forward(self, x):
        self.x = x
        u = np.dot(x, self.w) + self.b
        self.y = 