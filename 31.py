import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

def upload_pokemon():
    return pd.read_csv("pokemon.csv")

pokemon=upload_pokemon()
print(pokemon)

df = pd.DataFrame(pokemon["Speed"])

df.plot(kind='hist')
plt.show()