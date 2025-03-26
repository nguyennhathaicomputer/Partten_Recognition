from ucimlrepo import fetch_ucirepo 
  

def load_data():
    # fetch dataset 
    adult = fetch_ucirepo(id=2) 
    # data (as pandas dataframes) 
    X = adult.data.features 
    y = adult.data.targets 
    return X, y
  
