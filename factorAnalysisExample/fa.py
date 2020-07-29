import cityData
filename = '../refer/total.xlsx'
df = cityData.CityData()
df.readxlsx(filename)
df.calculateFA()