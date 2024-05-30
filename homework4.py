8.
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
import numpy as np


points = np.array([(7, 6), (8, 4), (3, -4), (-3, 0), (-2, 3), (2, 0), (-6, -4)])


hull = ConvexHull(points)


plt.plot(points[:, 0], points[:, 1], 'o')
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')


for i, txt in enumerate(['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7']):
    plt.annotate(txt, (points[i, 0], points[i, 1]))

plt.show()

9.
import matplotlib.pyplot as plt
import numpy as np


polygon_points = np.array([(0, 0), (3, -1), (7, 1), (10, -2), (10, -4), (12, -7)])
chords = [((10, -103), (10, -356))]


def is_convex_division(polygon, chord):
    # 这里应该是您的算法
    pass


plt.plot(polygon_points[:, 0], polygon_points[:, 1], 'o-')  
for chord in chords:
    plt.plot([chord[0][0], chord[1][0]], [chord[0][1], chord[1][1]], 'r--')  


labels = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A14', 'A16']
for i, txt in enumerate(labels):
    plt.annotate(txt, (polygon_points[i % len(polygon_points)][0], polygon_points[i % len(polygon_points)][1]))

plt.show()
