import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('penguins')
df = df.dropna()

print("FIRST 5 ROWS:")
print(df.head())
print()
print(df.info())
print()
print(df.describe)
print()
print("SPECIES :" , df['species'].unique())
print("ISLANDS:" , df['island'].unique())


sns.histplot(data=df , x='body_mass_g' , bins=20 , color = 'steelblue')
plt.title('DISTRIBUTION OF PENGUIN BODY MASS')
plt.xlabel('body mass(grams)')
plt.ylabel('count')
plt.show()


sns.kdeplot(data=df , x='flipper_length_mm' , hue='species' , fill=True)
plt.title('Flipper Length (KDE)')
plt.xlabel('Flipper Length (mm)')
plt.show()

sns.histplot(data=df , x='flipper_length_mm' , y='body_mass_g' , hue = 'species')
plt.title('Flipper Length VS Body Mass by Species')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (grams)')
plt.show()

corr = df.corr(numeric_only=True)
print("Correlation table :")
print(corr)
print()

sns.heatmap(corr , annot=True , cmap ='coolwarm')
plt.title('Correlation Heatmap -- Penguin Measurement')
plt.show()
