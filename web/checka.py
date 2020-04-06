import pandas
import glob

        
def main():

  cols=['age','workclass','fnlwgt','education','marital-status','occupation','relationship','race','sex','income','capital-loss','hours-per-week','native-country',]
  file = open("census.csv")
  census_data = pandas.read_csv("./census.csv",sep=',',names=cols)
  mean = census_data.income.mean()
  median = census_data.income.median()
  max1 = census_data.income.max()
  print(f"mean: {mean}\n Median: {median}\n Max: {max1}")

if __name__ == "__main__":
  main()