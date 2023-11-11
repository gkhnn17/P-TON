import numpy as np
import itertools

# 20x20'lik matris oluşturma ve tüm elemanları sıfırlama
poolMap = np.zeros((20,20),dtype=int)

# Aracın konumunu rastgele seçme ve matriste 1 olarak işaretleme
car_position = np.random.randint(0, 20, size=2)
poolMap[car_position[0], car_position[1]] = 1

# 4 adet hedef belirleme ve matriste 2 olarak işaretleme
x = 0 
targets =[]
while x <4:
    target = np.random.randint(0, 20, size=(2))
    x +=1
    targets.append(target)
    poolMap[target[0],target[1]] =2 

# Matrisi ekrana yazdırma
print(poolMap)

score = 0 
max_score =0

best_combination = None

# Tüm hedef kombinasyonlarını bulma
for r in range(5):
    target_permutations = itertools.permutations(range(4), r)


    # Her bir kombinasyon için puan hesaplama
    for target_permutations in target_permutations:
        score = 0
        current_position = car_position

        # Her hedefi ziyaret etme durumunu kontrol etme
        for target_index in range(4):
            if target_index in target_permutations:
                target = targets[target_index]
                dx = abs(target[0] - current_position[0])
                dy = abs(target[1] - current_position[1])
                score += dx + dy
                current_position = target

        # En yüksek puanı ve en iyi kombinasyonu güncelleme
if score > max_score:
    max_score = score
    best_combination = target_combination
    best_positions = [car_position]

    # Her hedefe giderken konumu güncelleme
    for target_index in range(4):
        if target_index in target_combination:
            target = targets[target_index]
            best_positions.append(target)

# Pool Map'i güncelleme
poolMapWithMovements = np.zeros((20, 20), dtype=int)
for i, position in enumerate(best_positions):
    if i == 0:
        poolMapWithMovements[position[0], position[1]] = 1
    else:
        poolMapWithMovements[position[0], position[1]] = i + 1

print("En yüksek puan:", max_score)
print("En iyi kombinasyon:", best_combination)
print("Arabanın her hedefe gittiği konumları gösteren Pool Map:")
print(poolMapWithMovements)
'''
topperm = []
for r in range(1,5):
    perm =list(itertools.permutations(targets,r))
    print(len(perm))
    print(perm)
    for i in range(len(perm)):
        uzaklik = perm[i][0][0] +perm[i][0][i-2]
        print(uzaklik)
'''