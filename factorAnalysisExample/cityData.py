'''
class cityData:
    storage city, time indicator
'''
import pandas as pd, numpy as np
from sklearn.datasets import  load_iris
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity, calculate_kmo
import matplotlib.pyplot as plt

class Indicator(object):
    def __init__(self, name, subIndicators):
        self.indicatorName = name
        self.subIndicators = {}
        for si in subIndicators:
            self.subIndicators[si] = 1
    def getIndicators(self):
        return self.subIndicators.keys()
    def setData(self, timeData):
        self.timeData = timeData
        self.rawdf = self.timeData.fillna(method='ffill', axis=0).fillna(method='bfill', axis=0)
        self.mean = self.rawdf.mean()
        self.sigma = self.rawdf.std()
        self.df = (self.rawdf-self.mean)/self.sigma
    def FA(self):
        print(self.df.columns)
        print(self.mean)
        print(self.sigma)
        '''
        print(self.df)
        chi_square_value,p_value=calculate_bartlett_sphericity(self.df)
        print(chi_square_value, p_value)
        # Bartlett ’s test, the p-value is 0. The test was statistically significant, indicating that the observed correlation matrix is not an identity matrix.
        kmo_all,kmo_model=calculate_kmo(self.df)
        print(kmo_model)
        # Kaiser-Meyer-Olkin (KMO) Test measures the suitability of data for factor analysis.
        fa = FactorAnalyzer(n_factors=self.df.shape[1], rotation=None)
        fa.fit(self.df)
        # Check Eigenvalues
        ev, v = fa.get_eigenvalues()
        print(ev)
        '''
        fa = FactorAnalyzer(n_factors=1, method="principal", rotation="varimax")
        fa.fit(self.df)
        # Print eigenvalues
        ev, v = fa.get_eigenvalues()
        print(ev)

        # Print loadings
        print(fa.loadings_)
        #print(fa.transform(self.df))
        '''
        plt.scatter(range(1,self.df.shape[1]+1),ev)
        plt.plot(range(1,self.df.shape[1]+1) ,ev)
        plt.title('Scree Plot')
        plt.xlabel('Factors')
        plt.ylabel('Eigenvalue')
        plt.grid()
        plt.savefig('{}.png'.format(self.indicatorName))
        plt.close()
        '''
        return 0
    def PCA(self):
        return 0
class CityData(object):
    def __init__(self):
        self.EnglishName = ''
        self.ChineseName = ''
        self.cityOid = ''
        self.economy = Indicator('economy', ['consumeLevel','CPI','GDP'])
        self.finance = Indicator('finance', ['socialFinancing','revenue','balanceDeposit'])#'listedCompany',
        self.education = Indicator('education', ['undergraduateStudent','primarySchoolStudent','juniorHighSchoolStudent','seniorHighSchoolStudent','elementarySchool','secondarySchools','higherEducationSchools'])#'postgraduate',
        #self.science = Indicator('science', ['institute','institudePeople','instituteFundamentalResearch','institudePaper','institudePatent'])
        self.health = Indicator('health', ['medicalInstitution','medicalPeople','medicalBed'])#,'medicalCost'
        self.people = Indicator('people', ['totalPopulation','bornRate','populationIncrease'])#,'populationAverageLife'
    def readxlsx(self, filename, sheetname=0):
        selectData = pd.read_excel(filename, sheetname, header=0, skiprows=[1], index_col=None, na_values=['NA'])
        
        self.economy.setData(selectData.loc[:, self.economy.getIndicators()])
        self.finance.setData(selectData.loc[:, self.finance.getIndicators()])
        self.education.setData(selectData.loc[:, self.education.getIndicators()])
        #self.science.setData(selectData.loc[:, self.science.getIndicators()])
        self.health.setData(selectData.loc[:, self.health.getIndicators()])
        self.people.setData(selectData.loc[:, self.people.getIndicators()])
    def calculateFA(self):
        self.economy.FA()
        self.finance.FA()
        self.education.FA()
        #self.science.FA()
        self.health.FA()
        self.people.FA()
class Cities(object):
    def __init__(self, cityes):
        self.cityes = cityes