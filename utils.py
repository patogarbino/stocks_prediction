import requests
import pandas as pd

ticker = 'AAPL'
def get_data(ticker):

    df = pd.DataFrame()

    for function in ['INCOME_STATEMENT','BALANCE_SHEET','CASH_FLOW','EARNINGS']:
        try:
            url = 'https://www.alphavantage.co/query'
            params = {'function': function,
                  'symbol': ticker,
                  'apikey':'C2FFBBIRN1B0SD6Z'
            }

            r = requests.get(url,params = params).json()


            if function in ['INCOME_STATEMENT','BALANCE_SHEET','CASH_FLOW']:

                response = pd.DataFrame(r['quarterlyReports'])
                response.drop(columns = 'reportedCurrency',inplace = True)
                df = pd.concat([df,response], axis= 1)


            else:
                print('Earnings')

                response = pd.DataFrame(r['quarterlyEarnings'])
                df = df.merge(response, on = 'fiscalDateEnding')
                print('Earnings_2')
            return df

        except:
            break
    return 'No se pudo obtener la información necesaria'
