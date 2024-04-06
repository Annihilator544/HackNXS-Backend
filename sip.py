import requests



def get_data(amt: int, fund_id: int = 118666, months: int = 6):
    url = "https://api.mfapi.in/mf/" + str(fund_id)
    response = requests.get(url).json()
    data = list(response["data"])
    Bnav = float(data[months*30]["nav"])
    current_amt = 0
    for i in range(months*30, 0, -30):
        current_amt += amt
        profit = (float(data[i]["nav"]) - Bnav) / Bnav
        current_amt = current_amt * (1 + profit)
        print(f"Profit for {data[i]['date']} is {profit}")
        print(f"Current amount is {current_amt:.2f}")
        Bnav = float(data[i]["nav"])
    return (response["meta"],current_amt)


