import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import pandas as pd
from matplotlib import font_manager
from highlight_text import ax_text
# - Data Files -
df = pd.read_excel("/Users/akke/Development/Random Projects/52 Charts for 2026/Week 1/Vital Statistics of Korea 2026.xlsx")

# -- Fonts --
font = "/Users/akke/Library/Fonts/Commissioner FLAR VOLM.ttf"
bold_font = FontProperties(fname=font, size=35, weight=900)
regular_font = FontProperties(fname=font, size=35, weight=400)
thin_font =FontProperties(fname=font, size=35, weight=100)

# -- Plot --
cm = 1 / 2.54
fig, ax = plt.subplots(figsize=(22 * cm, 23 * cm), facecolor='none')
fig.subplots_adjust(top=0.8)
ax.plot(df['Year'], df['Fertility Rate'])

# -- Cosmetics --
ax.grid(visible=False)
ax.spines[:].set_visible(False)
ax_text(1950, 7, size=25, font=regular_font, s="<South Korea>'s divindling birth rate", color='#0047A0',
        highlight_textprops=[{'color':'#CD2E3A', 'size':35, 'font':bold_font}])

# -- Arrows --
ax.annotate("", xytext=(2015, 2), xy=(2018.2, 1),
        arrowprops=dict(arrowstyle='->',
        linewidth=2,
        color='#CD2E3A',
        connectionstyle='arc3,rad=-0.25',
        shrinkA=0,  
        shrinkB=0))
ax.text(2015, 2.2, "First time the lowest\nbirthrate in the world", 
        ha='left', va='bottom',
        fontproperties=regular_font, weight='500',
        fontsize=15,
        )
plt.show()