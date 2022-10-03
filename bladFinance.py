import urllib
import csv
import pandas as pd
from datetime import datetime

class bladFinance:
    # monthYear must be in yyyymm format or yyyy to see entire year
    def getDailyTreasuryInterestRates(monthYear, toPresent):
        # toPresent is boolean true or false, monthYear will only return for 1 year or 1 month so need additional work to get data up to present, if doing to present only do yyyy format
        if len(str(monthYear)) == 4 and toPresent == True:
            df = pd.read_csv("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/{year}/all?type=daily_treasury_yield_curve&field_tdr_date_value={year}&page&_format=csv".format(year=monthYear))
            currentYear = datetime.now().year
            yy = int(currentYear)
            y = int(monthYear)
            while y<yy:
                df2 = pd.read_csv("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/{year}/all?type=daily_treasury_yield_curve&field_tdr_date_value={year}&page&_format=csv".format(year=y))
                df = pd.concat([df,df2])
                #df.append(df2)
                y = y + 1
        else:
            df = pd.read_csv("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/all/{year}?type=daily_treasury_yield_curve&field_tdr_date_value_month={year}&page&_format=csv".format(year=monthYear),skiprows=2)

        #file = urllib.urlopen("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/all/{year}?type=daily_treasury_yield_curve&field_tdr_date_value_month={year}&page&_format=csv".format(year=monthYear))
        #df = csv.reader(file)
        return df
    #def getFedYieldRates(monthYear):
        
