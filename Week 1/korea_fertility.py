import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from pyfonts import load_font
import pandas as pd
from highlight_text import ax_text

# - Data Files -
url = "https://github.com/thatakin/52Chartsfor52Weeks/raw/refs/heads/main/Week%201/Vital%20Statistics%20of%20Korea%202026.xlsx"
df = pd.read_excel(url)

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
ax.plot(df['Year'], df['Fertility Rate'], color='#0047A0')

# -- Cosmetics --
ax.grid(visible=False)
ax.spines[:].set_visible(False)
ax_text(1945, 7, size=25, font=regular, s="<South Korea>'s dwindling birth rate", color='#0047A0',
        highlight_textprops=[{'color':'#CD2E3A', 'size':35, 'font':bold}])

y_max = ax.get_ylim()[1]  # Get the top of y-axis
x_min = ax.get_xlim()[0]  # Get the left of x-axis
ax.text(x_min, y_max, "Births\nper woman",
        va='top', ha='right', fontproperties=thin, size=14)

# Label Font
font_ticks = regular.copy()
font_ticks.set_size(14)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(font_ticks) 

# -- Arrows --
ax.annotate("", xytext=(2015, 2), xy=(2018.2, 1),
        arrowprops=dict(arrowstyle='->',
        linewidth=2,
        color='#CD2E3A',
        connectionstyle='arc3,rad=-0.25',
        shrinkA=0,  
        shrinkB=0))
ax_text(2015, 2.5, color='black', s="First time the <lowest>\nbirthrate in the world", 
        ha='right', va='top',
        font=regular, weight='500',
        fontsize=15, highlight_textprops=[{'color':'#CD2E3A', 'font':bold}])
plt.savefig('week1-Korea.svg', transparent=True, dpi=300)
plt.show()