import numpy as np
import matplotlib.pyplot as plt


class Object:
    def __init__(self, data: np.ndarray, title: str, color: str):
        self.data = data
        self.title = title
        self.color = color

    def plot(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.data[:, 0], self.data[:, 1], self.color, marker='o')
        plt.title(self.title)
        plt.axis('equal')
        plt.show()
    