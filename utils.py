import requests
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline

def get_data(ticker, function):

    url = 'https://www.alphavantage.co/query'
    params = {'function': function,
          'symbol': ticker,
          'apikey':'9Q6MRAOS3OPYVK3R'
    }

    return requests.get(url,params = params).json()

def merge_data (ticker):

    df = pd.DataFrame()

    r = get_data(ticker,'INCOME_STATEMENT')
    response = pd.DataFrame(r['quarterlyReports'])
    response.drop(columns = 'reportedCurrency',inplace = True)
    df = pd.concat([df,response], axis= 1)

    r = get_data(ticker,'BALANCE_SHEET')
    response = pd.DataFrame(r['quarterlyReports'])
    response.drop(columns = 'reportedCurrency',inplace = True)
    df = df.merge(response, on = 'fiscalDateEnding')

    r = get_data(ticker,'CASH_FLOW')
    response = pd.DataFrame(r['quarterlyReports'])
    response.drop(columns = 'reportedCurrency',inplace = True)
    df = df.merge(response, on = 'fiscalDateEnding')

    r = get_data(ticker,'EARNINGS')
    response = pd.DataFrame(r['quarterlyEarnings'])
    df = df.merge(response, on = 'fiscalDateEnding')

    return df.head(1)


def  clean_data(df):
    cols_to_drop = ['proceedsFromSaleOfTreasuryStock','paymentsForRepurchaseOfPreferredStock','dividendPayoutPreferredStock',
                'proceedsFromOperatingActivities','proceedsFromIssuanceOfPreferredStock','changeInExchangeRate','investmentIncomeNet',
                'deferredRevenue','depreciation','capitalLeaseObligations','treasuryStock','proceedsFromIssuanceOfCommonStock',
                'longTermDebtNoncurrent','researchAndDevelopment','paymentsForRepurchaseOfCommonStock','investments',
                'accumulatedDepreciationAmortizationPPE','proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet',
                'proceedsFromRepaymentsOfShortTermDebt','changeInInventory','paymentsForRepurchaseOfEquity','currentDebt',
                'interestIncome','shortTermInvestments','dividendPayoutCommonStock','longTermInvestments','dividendPayout',
                'currentAccountsPayable','currentNetReceivables','inventory','paymentsForOperatingActivities',
                'otherNonOperatingIncome','goodwill','interestAndDebtExpense','changeInReceivables','currentLongTermDebt',
                'nonInterestIncome','changeInOperatingLiabilities','intangibleAssetsExcludingGoodwill','shortTermDebt',
                'changeInOperatingAssets','otherNonCurrentLiabilities','intangibleAssets','longTermDebt','netInterestIncome',
                'fiscalDateEnding','reportedDate']

    preproc_data = pd.read_csv('data/preproc_data.csv')

    df.drop(columns = cols_to_drop,inplace = True)
    pipeline = make_pipeline(SimpleImputer(strategy='median'))
    pipeline.fit(preproc_data)
    df  = pipeline.transform(df)

    return df
