import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd
import statsmodels.api as sm
import matplotlib
from pylab import rcParams
rcParams['figure.figsize'] = 18, 8
matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'



df = pd.read_excel("TOTALNSA.xls")

cars = df
cars = cars.set_index('observation_date')


y = cars

y.plot(figsize=(15,6))
#plt.show()

decomposition = sm.tsa.seasonal_decompose(y, model='additive')
fig = decomposition.plot()
#plt.show()

"""
p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
"""

mod = sm.tsa.statespace.SARIMAX(y,
                                order=(0, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
#print(results.summary().tables[1])

results.plot_diagnostics(figsize=(16, 8))
#plt.show()

pred = results.get_prediction(start=pd.to_datetime('2017-01-01'), dynamic=False)
pred_ci = pred.conf_int()
ax = y['2014':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('Car Sales')
#plt.legend()
#plt.show()

y_forecasted = pred.predicted_mean
y_forecasted = y_forecasted.tolist()
y_truth = y['2017-01-01':]
y_truth = y_truth['TOTALNSA'].tolist()
squared_error_list = []

truth_forecast_pairs = zip(y_forecasted, y_truth)
truth_forecast_pairs = list(truth_forecast_pairs)

for f, t in truth_forecast_pairs:
    squared_error_list.append((t-f)**2)

mse = sum(squared_error_list)/len(squared_error_list)

print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))
print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))


pred_uc = results.get_forecast(steps=13)
pred_ci = pred_uc.conf_int()
ax = y['2014':].plot(label='Observed', figsize=(14, 7))
pred_uc.predicted_mean.plot(ax=ax, label='Forecast')
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.25)
ax.set_xlabel('Date')
ax.set_ylabel('Car Sales')
plt.legend()
plt.show()