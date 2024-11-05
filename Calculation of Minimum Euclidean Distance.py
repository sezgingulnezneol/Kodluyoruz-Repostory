'''
import math

# Noktaları tanımlıyoruz
points = [(1, 2), (4, 6), (5, 3), (2, 1), (7, 5)]

# İki nokta arasındaki Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Mesafeleri saklamak için liste
distances = []

# Her nokta çifti arasındaki mesafeyi hesaplama
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bulma
min_distance = min(distances)

print("Tüm noktalar arasındaki minimum mesafe:", min_distance)
'''