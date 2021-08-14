

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.axes as ax
import matplotlib

pd.set_option('display.max_columns', None)

df = pd.read_csv(
    'mining_report.csv',
    usecols = [
        'Local date time',
        'Purpose',
        'Amount (BTC)',
        '* Exchange rate',
        'Amount (USD)'],
    index_col=0, 
    parse_dates=True
    )



df = df.rename(columns={
    'Amount (BTC)': 'Amount', 
    '* Exchange rate': 'Exchange rate', 
    'Amount (USD)': 'USD Equivalent'})

df.drop(df.tail(3).index,
        inplace = True)

df.index.name = 'Date'
df.index = df.index.str[:11]
df.index = pd.to_datetime(df.index)



df['Amount'] = 1000000 * df['Amount']
df['Exchange rate'] = 1000000 * df['Exchange rate']

income_plot = df.groupby(pd.Grouper(level='Date',freq='W')).sum()



fig, axs = plt.subplots(2)
fig.suptitle('USD and μBTC Generated Per Week')

axs[0].plot(income_plot['USD Equivalent'])
axs[0].set_title('USD Generated Per Week')
axs[1].plot(income_plot['Amount'])
axs[1].set_title('μBTC Generated Per Week')

fig.tight_layout()
plt.show()