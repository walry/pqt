import tushare as ts 
d = ts.get_tick_data('601318','2017-06-26')
print(d)
e = ts.get_hist_data('601318',start='2017-06-23',end='2017-06-26')
print (e)