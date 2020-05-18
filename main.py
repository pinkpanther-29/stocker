import yfinance as yf
import matplotlib.pyplot as plt
import seaborn

msft = yf.Ticker("MSFT")
print(msft.info)

hist = msft.history(period="5d")
print(hist)
print(type(hist))
