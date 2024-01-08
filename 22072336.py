import pandas as pan
import numpy as num


from matplotlib import pyplot as mpyp

import warnings
warnings.filterwarnings('ignore')
dts = pan.read_csv('WHO-COVID-19-global-table-data-31-08-21.csv')
dtst=dts[['Name','Cases - cumulative total', 'Cases - newly reported in last 7 days', 'Deaths - cumulative total', 'Deaths - newly reported in last 7 days','Cases - newly reported in last 7 days per 100000 population','Deaths - cumulative total per 100000 population']]
dtst[1:5].plot.bar(x='Name', y='Cases - cumulative total', xlabel = "Country Name", ylabel = "Total cumulative cases",rot=0, title="No. of total cumulative covid cases in different Countries");
dtst[1:5].plot.pie(y='Deaths - cumulative total', figsize = (5, 5), labels=dtst[1:5].Name, autopct='%1.1f%%', title="No. of Total Cumulative Deaths in different countries")
# Create a Figure with one Axis on it
fig, ax = mpyp.subplots()
# The x-values of the bars.
Country = dtst[1:5]['Name']
x = num.arange(len(Country))

# The width of the bars (1 = the whole width of the 'year group')
width = 0.15

# Create the bar charts!
ax.bar(x - 3*width/2, dtst[1:5]['Cases - newly reported in last 7 days'], width, label="Covid Cases - newly reported in last 7 days", color="Red")
ax.bar(x - width/2, dtst[1:5]['Deaths - newly reported in last 7 days'], width, label="Deaths - newly reported in last 7 days", color="Green")

# Notice that features like labels and titles are added in separate steps
ax.set_ylabel("No. of Newly reported covid cases and deaths in last 7 days")
ax.set_title("No. of Newly reported covid cases and deaths in last 7 days in different countries")

ax.set_xticks(x)    # This ensures we have one tick per year, otherwise we get fewer
ax.set_xticklabels(Country.astype(str).values, rotation='vertical')

ax.legend()
explode = (0.05, 0.05, 0.05, 0.05, 0.05)
dtst[1:5].plot.pie(y='Cases - newly reported in last 7 days per 100000 population', ylabel = "newly reported cases", figsize = (5, 5), labels=dtst[1:5].Name, autopct='%1.1f%%', title="No. of newly reported covid cases in last 7 days per 100000 population in different countries")
centre_circle = mpyp.Circle((0, 0), 0.70, fc='white')
fig = mpyp.gcf()
fig.gca().add_artist(centre_circle)
# building layers (without data)
figure = mpyp.figure(figsize=(10, 8))
gs_master = mpyp.gridspec.GridSpec(4, 2, height_ratios=[1, 2, 8, 2])

## ----------------------------- ## -----------------------------

dtst[1:5].plot.bar(x='Name', y='Cases - cumulative total', xlabel = "Country Name", ylabel = "Total cumulative cases",rot=0, title="No. of total cumulative covid cases in different Countries");
dtst[1:5].plot.pie(y='Deaths - cumulative total', figsize = (5, 5), labels=dtst[1:5].Name, autopct='%1.1f%%', title="No. of Total Cumulative Deaths in different countries")
## ----------------------------- ## -----------------------------

# Create a Figure with one Axis on it
fig, ax = mpyp.subplots()
# The x-values of the bars.
Country = dtst[1:5]['Name']
x = num.arange(len(Country))

# The width of the bars (1 = the whole width of the 'year group')
width = 0.15

# Create the bar charts!
ax.bar(x - 3*width/2, dtst[1:5]['Cases - newly reported in last 7 days'], width, label="Covid Cases - newly reported in last 7 days", color="Red")
ax.bar(x - width/2, dtst[1:5]['Deaths - newly reported in last 7 days'], width, label="Deaths - newly reported in last 7 days", color="Green")

# Notice that features like labels and titles are added in separate steps
ax.set_ylabel("No. of Newly reported covid cases and deaths in last 7 days")
ax.set_title("No. of Newly reported covid cases and deaths in last 7 days in different countries")

ax.set_xticks(x)    # This ensures we have one tick per year, otherwise we get fewer
ax.set_xticklabels(Country.astype(str).values, rotation='vertical')

ax.legend()

explode = (0.05, 0.05, 0.05, 0.05, 0.05)
dtst[1:5].plot.pie(y='Cases - newly reported in last 7 days per 100000 population', ylabel = "newly reported cases", figsize = (5, 5), labels=dtst[1:5].Name, autopct='%1.1f%%', title="No. of newly reported covid cases in last 7 days per 100000 population in different countries")
centre_circle = mpyp.Circle((0, 0), 0.70, fc='white')
fig = mpyp.gcf()
fig.gca().add_artist(centre_circle)

# joins layers still without data
gs_master.tight_layout(figure)
mpyp.show()
