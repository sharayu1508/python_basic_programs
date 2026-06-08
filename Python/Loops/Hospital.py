# 15.Hospital Patient Temperature Monitor

normal = 0
fever = 0

for i in range(1, 21):

    temp = float(input(f"Enter temperature of Patient {i} : "))

    if temp > 100:
        fever += 1
    else:
        normal += 1

print("\nNormal Patients :", normal)
print("Fever Patients :", fever)
