import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('population.csv')

india = data[data.Country == 'India']
china = data[data.Country == 'China']

# Plot grapth between the India and the China to compare population in Millions
plt.plot(india.Year, india.Value / 10**6)
plt.plot(china.Year, china.Value / 10**6)
plt.legend(['India', 'China'])
plt.xlabel('Year')
plt.ylabel('Population')
plt.show()

# Plot grapth between the India and the China to compare population growth rate
india_percentage = india.Value / india.Value.iloc[0] * 100
china_percentage = china.Value / china.Value.iloc[0] * 100
plt.plot(india.Year, india_percentage)
plt.plot(china.Year, china_percentage)
plt.legend(['India', 'China'])
plt.xlabel('Year')
plt.ylabel('Population Growth')
plt.show()
