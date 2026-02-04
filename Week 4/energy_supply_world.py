import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from pyfonts import load_font
import pandas as pd
from pypalettes import load_cmap

# - Data Files -
url = "https://raw.githubusercontent.com/thatakin/52Chartsfor52Weeks/refs/heads/main/Week%204/Total%20Energy%20Supply%20by%20Source.csv"
df = pd.read_csv(url)

# -- Colors --
# Using Pypalettes to handle the colours
cmap = load_cmap("Superfishel_Stone")
specific_colors = {
    'Coal and coal products': "#5e5652",
    'Natural gas': cmap.colors[3],
    'Hydropower': cmap.colors[6],
    'Nuclear': cmap.colors[1],
    'Solar, wind and other renewables': cmap.colors[4],
    'Biofuels and waste': cmap.colors[2],
    'Oil and oil products': '#32373a'
}
data_columns = [col for col in df.columns if col != 'Year' and col != "Units"]
colors = [specific_colors[col] for col in data_columns]

# -- Fonts --
# Using Pyfonts to handle the fonts
bold = load_font("https://github.com/google/fonts/blob/main/ofl/mukta/Mukta-Bold.ttf?raw=true")
regular = load_font("https://github.com/google/fonts/blob/main/ofl/mukta/Mukta-Regular.ttf?raw=true")
thin = load_font("https://github.com/google/fonts/blob/main/ofl/mukta/Mukta-Light.ttf?raw=true")

# -- Plot --
cm = 1 / 2.54
fig, ax = plt.subplots(figsize=(22 * cm, 23 * cm), facecolor='none')
# Adjusting the plot size to accommodate the title
fig.subplots_adjust(top=0.8)
x = df['Year']
ax.stackplot(x, df['Coal and coal products'], df['Natural gas'], df['Hydropower'], df['Nuclear'], df['Solar, wind and other renewables'], df['Biofuels and waste'], df['Oil and oil products'], colors=colors)

# -- Cosmetics --
ax.grid(visible=False)
ax.spines[:].set_visible(False)
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False) #Do not use scientific notation
plt.yticks([200000000,400000000,600000000,800000000], ['200M', '400M', '600M', '800M'])

y_max = ax.get_ylim()[1]
x_min = ax.get_xlim()[0]
ax.text(x_min, y_max * 1.02, "Terajoules (TJ)",
        va='bottom', ha='right', fontproperties=regular, size=17)

# Data Labels
cumulative = df[data_columns].iloc[-1].cumsum() # Get the cumulative sum of the last year's values
for i, column in enumerate(data_columns):
    if i == 0: #Put the label of the first one at the bottom
        y_position = cumulative[column] / 2  # Put the labels in the middle of the stacked area
    else:
        y_position = (cumulative[column] + cumulative[data_columns[i-1]]) / 2  # Middle of each stacked area
    
    x_position = df['Year'].iloc[-1] + 0.3
    
    ax.text(x_position, y_position, column, 
            va='center', ha='left', fontsize=20,
            fontproperties=regular, color=colors[i])
# Add title and subtitle  
ax.text(x_min, y_max * 1.15, size=25, font=bold, s="The Evolution of World Energy Production")
ax.text(x_min, y_max * 1.09, size=20, font=thin, s="Total energy supply by source, World, 1990-2023")
# Handle the tick fonts and size
font_ticks = regular.copy()
font_ticks.set_size(17)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(font_ticks) 

# Add data source
ax.text(0, -0.08, "Data: International Energy Agency (IEA) | Viz by Akin Orhan", 
           size=12, font=thin, color='gray', va='top', transform=ax.transAxes)

plt.savefig('week4-energyproduction.svg', transparent=True, dpi=300)
plt.show()