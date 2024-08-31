import math

points = [
    (1, 2),
    (4, 6),
    (7, 1),
    (3, 5)
]

def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

distances = []
num_points = len(points)
for i in range(num_points):
    for j in range(i + 1, num_points):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)


if distances:
    min_distance = min(distances)
    print("Minimum mesafe:", min_distance)
else:
    print("Mesafe hesaplanacak nokta çiftleri bulunmuyor.")