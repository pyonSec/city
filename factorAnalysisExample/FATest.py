#References:
#https://www.datacamp.com/community/tutorials/introduction-factor-analysis
#https://pypi.org/project/factor-analyzer/#:~:text=This%20is%20a%20Python%20module%20to%20perform%20exploratory,perform%20confirmatory%20factoranalysis%20%28CFA%29%2C%20with%20certain%20pre-defined%20constraints.
#https://factor-analyzer.readthedocs.io/en/latest/index.html
#https://vincentarelbundock.github.io/Rdatasets/datasets.html

from factor_analyzer import FactorAnalyzer
import matplotlib.pyplot as plt
import pandas as pd

df= pd.read_csv("bfi.csv")

print(df.columns)

df.drop(['gender', 'education', 'age', 'Unnamed: 0'],axis=1,inplace=True)

df.dropna(inplace=True)

from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
chi_square_value,p_value=calculate_bartlett_sphericity(df)
print(chi_square_value, p_value)

from factor_analyzer.factor_analyzer import calculate_kmo
kmo_all,kmo_model=calculate_kmo(df)
print(kmo_model)

# Create factor analysis object and perform factor analysis
fa = FactorAnalyzer(n_factors=6, method="principal", rotation="varimax")
fa.fit(df)

# Print eigenvalues
ev, v = fa.get_eigenvalues()
print(ev)

# Print loadings
print(fa.loadings_)
