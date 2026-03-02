import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from pyfonts import load_font
import pandas as pd
from pypalettes import load_cmap
from highlight_text import ax_text


# -- Fonts --
# Using Pyfonts to handle the fonts
bold = load_font("https://github.com/google/fonts/blob/main/ofl/mukta/Mukta-Bold.ttf?raw=true")
regular = load_font("https://github.com/google/fonts/blob/main/ofl/mukta/Mukta-Regular.ttf?raw=true")
thin = load_font("https://github.com/google/fonts/blob/main/ofl/mukta/Mukta-Light.ttf?raw=true")

# --- Data Frame and Handling ---
url = "https://github.com/thatakin/52Chartsfor52Weeks/blob/main/Week%206/IDMC_disaster%20displacement%202019-2024.xlsx?raw=true"
df = pd.read_excel(url, engine='openpyxl')
df_yearly = df.groupby('Year')['Disaster Internal Displacements'].sum().reset_index()

# -- Plot --
cm = 1 / 2.54
fig, ax = plt.subplots(figsize=(22 * cm, 23 * cm), facecolor='none')

ax.plot(df_yearly['Year'], df_yearly['Disaster Internal Displacements'], color='#0047A0', marker='o')

# -- Cosmetics --
ax.grid(visible=False)
ax.spines[:].set_visible(False)
plt.ticklabel_format(style='plain')
plt.yticks([15000000,20000000,25000000,30000000,35000000,40000000,45000000],["15M","20M","25M",'30M','35M','40M','45M'])

#Title and Subtitle
ax.text(2007, 48000000, size=25, font=regular, s="Internal Displacement due to disasters", color='#0047A0')
ax.text(2007.3, 45500000, size=15, font=regular, s="Internal displacement of people due to natural disasters\nis on the rise across the world", color='black')

# Y-axis tag
y_max = ax.get_ylim()[1]  # Get the top of y-axis
x_min = ax.get_xlim()[0]  # Get the left of x-axis
ax.text(x_min-0.5, y_max, "Internal\nDisplacements",
        va='top', ha='right', fontproperties=thin, size=14)


# -- Arrows --
# 2010 China and Pakistan
ax.annotate("", xytext=(2012, 43000000), xy=(2010, 43000000),
        arrowprops=dict(arrowstyle='->',
        linewidth=2,
        color='#CD2E3A',
        connectionstyle='arc3,rad=0.25',
        shrinkA=0,  
        shrinkB=0))
ax_text(2012, 44000000, color='black', s="Major floods in\n<China> and <Pakistan>", 
        ha='left', va='top',
        font=regular, weight='500',
        fontsize=15, highlight_textprops=[{'color':'#CD2E3A', 'font':bold},
                                          {'color':'#CD2E3A', 'font':bold}])
# 2012 China, Pakistan, Philippines
ax.annotate("", xytext=(2014, 31000000), xy=(2012, 30000000+500000),
        arrowprops=dict(arrowstyle='->',
        linewidth=2,
        color='#CD2E3A',
        connectionstyle='arc3,rad=0.25',
        shrinkA=0,  
        shrinkB=0))
ax_text(2014, 32000100, color='black', s="Floods in <China>,\n<Pakistan>, <India> and \n<the Philippines>", 
        ha='left', va='top',
        font=regular, weight='500',
        fontsize=15, highlight_textprops=[{'color':'#CD2E3A', 'font':bold},
                                          {'color':'#CD2E3A', 'font':bold},
                                          {'color':'#CD2E3A', 'font':bold},
                                          {'color':'#CD2E3A', 'font':bold}])

# 2020-2022 Monsoon Floods
ax.annotate("", xytext=(2019, 37000000), xy=(2020, 31500000),
        arrowprops=dict(arrowstyle='->',
        linewidth=2,
        color='#CD2E3A',
        connectionstyle='arc3,rad=-0.25',
        shrinkA=0,  
        shrinkB=0)) #Arrow to 2020
ax.annotate("", xytext=(2019, 37000000), xy=(2022, 33500000),
        arrowprops=dict(arrowstyle='->',
        linewidth=2,
        color='#CD2E3A',
        connectionstyle='arc3,rad=-0.25',
        shrinkA=0,  
        shrinkB=0)) # Arrow to 2022
ax_text(2018.9, 39000000, color='black', s="Floods in <East>,\nand <Southeast Asia>", 
        ha='right', va='top',
        font=regular, weight='500',
        fontsize=15, highlight_textprops=[{'color':'#CD2E3A', 'font':bold},
                                          {'color':'#CD2E3A', 'font':bold},
                                          ])
# 2024 Storms
ax.annotate("", xytext=(2022, 43000000), xy=(2024, 46000000),
        arrowprops=dict(arrowstyle='->',
        linewidth=2,
        color='#CD2E3A',
        connectionstyle='arc3,rad=-0.25',
        shrinkA=0,  
        shrinkB=0))
ax_text(2022, 43000000, color='black', s="Storms across <the USA>\nand <the Philippines>", 
        ha='right', va='top',
        font=regular, weight='500',
        fontsize=15, highlight_textprops=[{'color':'#CD2E3A', 'font':bold},
                                          {'color':'#CD2E3A', 'font':bold},
                                          ])

fig.text(0.13, 0.12, size=10, font=thin, s="Data: 2025 IDMC | Viz by Akin Orhan", color='black')
plt.savefig('week6-disaster_displacement.svg', transparent=True, dpi=300)
plt.show()