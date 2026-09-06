import matplotlib.pyplot as plt

file_path = 'sensor.txt'
z_adx_values = []

with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split(',')
        z_adx = float(parts[3].strip().split(':')[1])  
        z_adx_values.append(z_adx)


plt.figure(figsize=(10, 6))
plt.plot(z_adx_values, marker='o')
plt.xlabel('Zeilen Nummer')
plt.ylabel('Z_adx Wert')
plt.title('Z_adx Auswertung')
plt.tight_layout()
plt.show()







