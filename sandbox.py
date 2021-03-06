import pandas as pd
import matplotlib.pyplot as plt

def get_price(symbol):
    df = pd.read_csv("data/{}.csv".format(symbol))
    #return df['Volume'].mean()
    return df['Close'].max()

def show_data(symbol, location="head", lines=20):
    df = pd.read_csv("data/{}.csv".format(symbol))
    if location == "head":
        return df.head(lines)
    return df.tail(lines)

def graph_data(symbol):
    df = pd.read_csv("data/{}.csv".format(symbol), parse_dates=True, usecols=["Date", "Close"])
    df['Close'].plot()
    plt.show()

if __name__ == "__main__":
    print(show_data("AMZN", "head", 25))
    print(get_price("AMZN"))
    graph_data("AMZN")