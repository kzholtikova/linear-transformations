import numpy as np
import matplotlib.pyplot as plt

DIMENSIONS = ['x', 'y', 'z']

class Object:
    def __init__(self, data: np.ndarray, title: str, color: str):
        self.data = data
        self.title = title
        self.color = color

    def plot(self):
        ax = plt.figure(figsize=(7, 5))
        if self.data.shape[1] == 3:
            ax = ax.add_subplot(projection='3d')
            ax.set_zlabel('Z')
        else:
            ax = ax.add_subplot()

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.axis('equal')
        ax.plot(*self.data.T, color=self.color, marker='o')
        plt.title(self.title)
        plt.show()
