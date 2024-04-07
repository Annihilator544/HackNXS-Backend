from wallstreet import Stock, Call, Put
class nsetool:
    s = Stock('INFY')
    df = s.historical(days_back=30, frequency='d')
    print(df['Date'].tolist())