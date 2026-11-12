import pandas as pd 
import matplotlib.pyplot as plt 



def read_csv(path):
    df = pd.read_csv(path)
    return df

def data_price(price_path):
    df_price = read_csv(price_path)
    df_price['date']= pd.to_datetime(df_price['date'], format='mixed', dayfirst=True,utc=True)
    df_price = df_price.set_index('date')
    return df_price

def main():
    price_path = "./iris_electricity_price.csv"
    df_price = data_price(price_path)
    print(df_price.head(3))
    plt.plot(df_price['elec_price'])
    plt.show()

if __name__ == '__main__':
    main()
