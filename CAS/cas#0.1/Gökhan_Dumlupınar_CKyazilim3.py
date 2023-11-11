import numpy as np
import itertools

poolMap = np.zeros((20, 20), dtype=int)
coordinates = np.zeros((5, 2), dtype=int)

poolMap[5][5] = 1  # Başlangıç
poolMap[12][7] = 2  # 1.HEDEF
poolMap[8][13] = 2  # 2.HEDEF
poolMap[10][15] = 2  # 3.HEDEF
poolMap[15][11] = 2  # 4.HEDEF

coordinates[0] = [5, 5]  # Başlangıç
coordinates[1] = [12, 7]  # 1.HEDEF
coordinates[2] = [8, 13]  # 2.HEDEF
coordinates[3] = [10, 15]  # 3.HEDEF
coordinates[4] = [15, 11]  # 4.HEDEF

#hedefler tek bir dizide toplanır
targets = coordinates[1:]
print(poolMap)
#en iyi skor ilerde karşılaştırılmak için -sonsuz olarak işaretlenir
best_score = float("-inf")
best_path = []

def calculate_score(path):
    car_position = coordinates[0]
    total_points = 0


    for target_index in path:
        target = coordinates[target_index]
        distance = abs(target[0] - car_position[0]) + abs(target[1] - car_position[1])
        total_points -= distance
        total_points += 15
        car_position = target

    return total_points
#tüm olasılılıklar çıkarılır karşılaştırılır
for path in itertools.permutations(range(1, 5), 4):
    path = list(path)
    score = calculate_score(path)
    if score > best_score:
        best_score = score
        # en iyi yol 
        best_path = [0] + path
    print(path)
print("Best Path:", best_path)
poolMapWithMovements = np.zeros((20, 20), dtype=int)
#aracın yollara uğrama sırası yazdırılır
for position in (coordinates[path]):
        poolMapWithMovements[position[0], position[1]] = 1
        
        print(poolMapWithMovements,"\n")
print("score",best_score)