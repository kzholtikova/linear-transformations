import numpy as np
import matplotlib.pyplot as plt

DIMENSIONS = ['x', 'y', 'z']


class Object:
    def __init__(self, data: np.ndarray, title: str):
        self.data = data
        self.title = title
        self.suptitle = None

    def plot(self, color: str = 'black'):
        ax = plt.figure(figsize=(7, 5))
        if self.data.shape[1] == 3:
            ax = ax.add_subplot(projection='3d')
            ax.set_zlabel('Z')
        else:
            ax = ax.add_subplot()

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.axis('equal')
        ax.plot(*self.data.T, color=color, marker='o')
        plt.title(self.title)
        plt.suptitle(self.suptitle) if self.suptitle else None
        plt.show()

    def rotate(self, angle: int, axis: str = 'x'):
        theta = np.radians(angle)
        rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
        if self.data.shape[1] == 3:
            rotation_pivot = [1 if x == DIMENSIONS.index(axis) else 0 for x in range(self.data.shape[1])]
            rotation_matrix = np.insert(rotation_matrix, DIMENSIONS.index(axis), rotation_pivot[:2], axis=0)
            rotation_matrix = np.insert(rotation_matrix, DIMENSIONS.index(axis), rotation_pivot, axis=1)

        return self.transform(rotation_matrix, f'rotation by {angle}')

    def scale(self, factor: int):
        return Object(self.data * factor, self.title)

    def mirror(self, axis: str):
        mirroring_matrix = np.eye(self.data.shape[1])
        for i in range(self.data.shape[1]):
            if i != DIMENSIONS.index(axis):
                mirroring_matrix[i, i] = -1

        return self.transform(mirroring_matrix, f'mirroring over {axis}')

    def shear(self, factor: int, axis: str):
        shearing_matrix = np.eye(self.data.shape[1])
        shearing_matrix[DIMENSIONS.index(axis)] = [1 if x == DIMENSIONS.index(axis) else factor for x in range(self.data.shape[1])]
        return self.transform(shearing_matrix, f'shearing over {axis} by {factor}')

    def project(self, axis: str):
        projection_matrix = np.eye(self.data.shape[1])
        projection_matrix[DIMENSIONS.index(axis), DIMENSIONS.index(axis)] = 0
        return self.transform(projection_matrix, f'projection over {axis}')

    def transform(self, transformation_matrix: np.ndarray, transformation=''):
        # A * T and not T * A due to the structure of the input data (rows of vectors)
        return Object(np.dot(self.data, transformation_matrix), f"{self.title} | {transformation}")
