import pandas as pd


df = pd.read_csv("C:/Users/andri/Documents/Andri Martin/Trisakti/Python/Praktikum Algo/Praktikum 12 Latihan 1 Andri Martin/Negara.csv")
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

print("Berikut Data Frame:")
print(df, "\n")

print("Berikut Data Mean:")
print(mean, "\n")

print("Berikut Data Standard Deviation:")
print(std, "\n")

mean.to_csv('NegaraMean.csv')
std.to_csv('NegaraStandardDeviation.csv')
print("Data Berhasil Dibuat, Terimakasih")