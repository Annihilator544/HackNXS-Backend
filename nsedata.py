from jugaad_data.nse import NSELive


def getLiveData(company_name):
    n = NSELive()
    q = n.stock_quote(company_name)
    return q['priceInfo']
