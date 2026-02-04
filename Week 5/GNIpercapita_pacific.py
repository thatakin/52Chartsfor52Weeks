import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from pyfonts import load_font
import pandas as pd
from pypalettes import load_cmap


# - Data Files -
url = "https://raw.githubusercontent.com/thatakin/52Chartsfor52Weeks/refs/heads/main/Week%205/GNI_capita_pacific.csv"
df = pd.read_csv(url)

# -- Colors --
# Using Pypalettes to handle the colours
cmap = load_cmap("Classic_Green_Orange_12")

country_colours = {
    "Nauru" : cmap.colors[0],
    "Palau" : cmap.colors[1],
    'Tuvalu' : cmap.colors[2],
    "Marshall Islands": cmap.colors[3],
    "Tonga": cmap.colors[4],
    "Fiji": cmap.colors[5],
    "Samoa": cmap.colors[6],
    "Vanuatu": cmap.colors[7],
    "Kiribati": cmap.colors[8],
    "Papua New Guinea": cmap.colors[9],
    "Solomon Islands": cmap.colors[10]
}

# -- Fonts --
# Using Pyfonts to handle the fonts
bold = load_font("https://github.com/google/fonts/blob/main/ofl/mukta/Mukta-Bold.ttf?raw=true")
regular = load_font("https://github.com/google/fonts/blob/main/ofl/mukta/Mukta-Regular.ttf?raw=true")
thin = load_font("https://github.com/google/fonts/blob/main/ofl/mukta/Mukta-Light.ttf?raw=true")


# Data Handling
df.rename(columns={'2020 [YR2020]': '2020', '2021 [YR2021]': '2021','2022 [YR2022]': '2022','2023 [YR2023]': '2023','2024 [YR2024]': '2024'}, inplace=True)
mel = pd.melt(df, id_vars=['Country Name'], value_vars=['2020', '2021', '2022', '2023', '2024'], var_name="Year", value_name="GNI") # Converting from wide to long format
mel['GNI'] = pd.to_numeric(mel['GNI'], errors='coerce') # Handling the missing data points
mel['Year'] = mel['Year'].astype(int)  # Convert Year to integer

# -- Plot --
cm = 1 / 2.54
fig, ax = plt.subplots(figsize=(22 * cm, 23 * cm), facecolor='none')
# Adjusting the plot size to accommodate the title
fig.subplots_adjust(top=0.8)

for country in mel['Country Name'].unique():
    country_data = mel[mel['Country Name'] == country]
    ax.plot(country_data['Year'], country_data['GNI'], 
            marker='o', linewidth=2, label=country, color=country_colours[country])

# -- Cosmetics --
ax.grid(visible=False)
ax.spines[:].set_visible(False)
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False) #Do not use scientific notation
plt.yticks([2000,4000,6000,8000,10000,20000,25000])
plt.xticks([2020,2021,2022,2023,2024])

# Labels

label_offsets = {
    'Vanuatu': 500,
    'Tonga': 750, 
    'Fiji': -10,
    'Tuvalu': 650,
    'Marshall Islands' : -450
}

for i, country in enumerate(mel['Country Name'].unique()):
    country_data = mel[mel['Country Name'] == country].dropna(subset=['GNI']).reset_index(drop=True)
    
    if len(country_data) > 0:
        y_position = country_data['GNI'].iloc[-1]
        x_position = 2024.3 
        offset = label_offsets.get(country, 15)
        ax.text(x_position, y_position + offset, country,
                va='center', ha='left', fontsize=20,
                fontproperties=regular, color=country_colours[country])
y_max = ax.get_ylim()[1]
x_min = ax.get_xlim()[0]
ax.text(x_min, y_max * 1.02, "USD",
        va='bottom', ha='right', fontproperties=regular, size=17)
      
# Add title and subtitle  
ax.text(x_min, y_max * 1.15, size=25, font=bold, s="Economic Divergence Across the Pacific")
ax.text(x_min, y_max * 1.09, size=20, font=thin, s="GNI per capita in Pacific island nations, 2020–2024")
# Handle the tick fonts and size
font_ticks = regular.copy()
font_ticks.set_size(17)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(font_ticks) 

# Add data source
ax.text(0, -0.08, "Data: World Bank | Viz by Akin Orhan", 
           size=12, font=thin, color='gray', va='top', transform=ax.transAxes)

plt.savefig('week5-GNIperCapita.svg', transparent=True, dpi=300)
plt.show()