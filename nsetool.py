from wallstreet import Stock, Call, Put
class nsetool:
    s = Stock('INFY')
    print(s.price)
    print(s.cp)
    print(s.change)
    print(s.last_trade)
    print(s.volume)
    df = s.historical(days_back=30, frequency='d')
    print(df)