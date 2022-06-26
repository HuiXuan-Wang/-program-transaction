# -*- coding: utf-8 -*-
import mplfinance as fplt
import pandas as pd

def get_data(amount):
    data = pd.read_csv('0050.csv')
    df = data.head(int(amount))
    df.rename(
        columns = {
            'date': 'Date', 'open': 'Open', 
            'high': 'High', 'low': 'Low', 
            'close': 'Close', 'volume': 'Volume'}, 
            inplace = True)#不創建新的對象，直接對原始對象進行修改

    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index(['Date'], inplace=True)        
    return df
    
def draw_candle_chart(df):
    
    mc = fplt.make_marketcolors(
                                up='tab:red',down='tab:green',
                                wick={'up':'red','down':'green'},
                                volume='tab:green',
                               )
    
    s  = fplt.make_mpf_style(marketcolors = mc)
    
    fplt.plot(
                df,
                type = 'candle',
                style = s,
                title = '0050',
                ylabel = 'Price ($)', 
                volume = True,
                savefig='stock_Kbar.png',
                
            )

    #plt.savefig("")
    
if __name__ == "__main__":
    draw_candle_chart(2330)