from django.shortcuts import render
import requests
import json
from datetime import date, timedelta
import datetime
from decouple import config

# Create your views here.

def tracking_error(request):
    key =config('key')
        
    params = {
    'access_key': key
    }

    #API Call

    api_etf_latest = requests.get('https://api.marketstack.com/v1/tickers/SETFNN50.XNSE/eod/latest',params).json()
    api_etf_old = requests.get('https://api.marketstack.com/v1/tickers/SETFNN50.XNSE/eod/2021-03-10',params).json()
    api_niftyindex_latest = requests.get('https://api.marketstack.com/v1/tickers/NN50.INDX/eod/latest',params).json()
    api_niftyindex_old = requests.get('https://api.marketstack.com/v1/tickers/NN50.INDX/eod/2021-03-10',params).json()

    difference=((api_etf_latest['close']/api_etf_old['close'])-1)-((api_niftyindex_latest['close']/api_niftyindex_old['close'])-1)

    #tracking error calculation
    tracking_error=abs(difference)*100
   
    context={
        
        'tracking_error':round(tracking_error,3)
    }

    return render(request,'tracking_error.html',context)


