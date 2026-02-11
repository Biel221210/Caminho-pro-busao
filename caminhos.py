import random
import subprocess

caminhos = random.choice([1, 2, 3, 4])

if caminhos == 1:
    subprocess.run(['cat', 'caminho1.txt'])
elif caminhos == 2:
    subprocess.run(['cat', 'caminho2.txt'])
elif caminhos == 3:
    subprocess.run(['cat', 'caminho3.txt'])
elif caminhos == 4:
    subprocess.run(['cat', 'caminho4.txt'])
