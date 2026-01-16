import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from pyfonts import load_font
import pandas as pd
from highlight_text import ax_text
import matplotlib.dates as mdates


# - Data Files -
url = "https://raw.githubusercontent.com/thatakin/52Chartsfor52Weeks/refs/heads/main/Week%202/Consumer%20Confidence%20Index%20Jan%2015%202026.csv"
df = pd.read_csv(url)


df_adjusted = pd.melt(df, id_vars=['Date'],
                      value_vars=["Australia", "Denmark", "China", "Germany", 
                                  "South Africa", "Türkiye", "India", 
                                  "Costa Rica", "OECD"],
                      var_name="Country", value_name="CCI")



# -- Fonts --
# Using Pyfonts to handle the fonts
bold = load_font("https://github.com/google/fonts/blob/main/ofl/mukta/Mukta-Bold.ttf?raw=true")
regular = load_font("https://github.com/google/fonts/blob/main/ofl/mukta/Mukta-Regular.ttf?raw=true")
thin = load_font("https://github.com/google/fonts/blob/main/ofl/mukta/Mukta-Light.ttf?raw=true")

# -- Plot --
cm = 1 / 2.54
fig, axs = plt.subplots(figsize=(22 * cm, 23 * cm), facecolor='none', ncols=3, nrows=3)
fig.text(0,1, "Costumer Confidence Index", font=bold, size=25)
fig.text(0.01,0.95, "CCI standardised confidence indicator providing an indication of\nfuture developments of households’ consumption and saving.", font=thin, size=15)
fig.subplots_adjust(top=0.8)
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

selected_countries = ["Australia", "Denmark", "China", "Germany", "South Africa", "Türkiye", "India", "Costa Rica", "OECD"]


for country, ax in zip(df_adjusted["Country"].unique(), axs.flat):
    x = df_adjusted.loc[df_adjusted["Country"] == country, "Date"]
    y = df_adjusted.loc[df_adjusted["Country"] == country, "CCI"]
    
    x = pd.to_datetime(x).reset_index(drop=True) #Convert dates to datetime format
    y = y.reset_index(drop=True) #Clean index
    
    ax.plot(x, y)
    ax.xaxis.set_major_locator(mdates.YearLocator()) #Put tick marks on each year
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y')) #Adjust the dates so it only shows years
    ax.set_xlim(pd.Timestamp("2020-01-01"), pd.Timestamp("2025-12-31")) #Limit the x axis between 2020 and 2025
    ax.set_ylim(90, 105) #Limit the y axis between 90 and 105
    ax.spines[:].set_visible(False) #Remove the frame
    ax.grid(axis="y") #Show grid lines from y axis
    ax.text(pd.Timestamp("2024-01-01"), 105, country) # Add country names to the corner

plt.savefig('week2-OECD_CCI.svg', transparent=True, dpi=300)
plt.show()



