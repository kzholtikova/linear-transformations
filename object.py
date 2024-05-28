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

    def rotate(self, angle: int, axis: str):
        theta = np.radians(angle)
        rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
        if self.data.shape[1] == 3:
            rotation_pivot = [1 if x == DIMENSIONS.index(axis) else 0 for x in range(self.data.shape[1])]
            rotation_matrix = np.insert(rotation_matrix, DIMENSIONS.index(axis), rotation_pivot[:2], axis=0)
            rotation_matrix = np.insert(rotation_matrix, DIMENSIONS.index(axis), rotation_pivot, axis=1)

        self.data = np.dot(self.data, rotation_matrix)

    def scale(self, factor: int):
        self.data *= factor

    def mirror(self, axis: str):
        mirroring_matrix = np.eye(self.data.shape[1])
        for i in range(self.data.shape[1]):
            if i != DIMENSIONS.index(axis):
                mirroring_matrix[i, i] = -1

        self.data = np.dot(self.data, mirroring_matrix)
        