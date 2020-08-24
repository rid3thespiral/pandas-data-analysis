import pandas as pd
from pathlib import Path

p = str(Path(__file__).parents[2])+"/materials/titanic.csv"
titanic = pd.read_csv(p)
titanic.head(10)
print(titanic.info())

#1. Display passengers in the first class
mask = titanic["Pclass"] == 1
print(titanic[mask])
#alternative method that servers also Nan values
print(titanic.where(titanic["Pclass"] == 1))
#alternative method that substitutes Nan with Falso string
print(titanic.where(titanic["Pclass"] == 1, other = 'Falso'))
#query needs a string to be evaluated, dropping Nan rows (same output as first point)
print(titanic.query("Pclass == 1"))