import pandas as pd
import matplotlib.pyplot as plt
from pyfonts import load_font
import numpy as np
from highlight_text import ax_text
from matplotlib.font_manager import FontProperties
# --- Fonts ---
# Using Pyfonts to handle the fonts
bold = load_font("https://github.com/google/fonts/blob/main/ofl/mukta/Mukta-Bold.ttf?raw=true")
regular = load_font("https://github.com/google/fonts/blob/main/ofl/mukta/Mukta-Regular.ttf?raw=true")
thin = load_font("https://github.com/google/fonts/blob/main/ofl/mukta/Mukta-Light.ttf?raw=true")

# --- Data ---
data = "https://github.com/thatakin/52Chartsfor52Weeks/blob/main/Week%203/population_tr.csv"
books = 'https://github.com/thatakin/52Chartsfor52Weeks/blob/main/Week%203/books.csv'

df_provinces = pd.read_csv(data)
df_books = pd.read_csv(books)

# -- Data Prep --
df_provinces['capita'] = df_provinces['Population'].div(df_books['Province'].map(df_books.set_index('Province')['Books'])) # Calculate number of books borrowed per capita
df_ordered = df_provinces.sort_values(by='capita') # Order the data frame by capita

# --- Plot ---
cm = 1 / 2.54
fig, ax = plt.subplots(figsize=(22 * cm, 40 * cm), facecolor='none')
fig.subplots_adjust(top=0.8)
plt.hlines(df_ordered['Province'],df_ordered["capita"],xmax=0, color="#C8102E")
plt.plot(df_ordered["capita"], df_ordered['Province'],"o", c= "#C8102E")

# --- Cosmetics ---
text_space = 32 # Adding additional space to accommodate the province names
ax.set_xlim(0, df_ordered['capita'].max() + text_space)
ax.set_ylim(-3, 87) # Extending the y-axis to mitigate issues with the title/subtitle

ax.grid(visible=False)
ax.spines[:].set_visible(False)
ax.set_ylabel("")
ax.set_xlabel("")
ax.get_yaxis().set_ticks([])
ax.get_xaxis().set_ticks([])


ax_text(2, 87, size=25, font=regular, s="<Turkey>'s reading divide", color='#0047A0',
        highlight_textprops=[{'color':'#C8102E', 'size':35, 'font':bold}])

ax.text(2, 81, size=15, font=regular, s="Per capita library book consumption in Turkey's 81 provinces", color='black')

# Function to add the data labels aka name and 'books/person' of each province
for i, (idx, row) in enumerate(df_ordered.iterrows()):
    ax.text(row['capita'] + 3, i, f"{row['Province']} - {row['capita']:.2f} books/person", 
            va='center', ha='left', fontsize=10, 
            fontproperties=regular)

fig.text(0.13, 0.12, size=10, font=thin, s="Data: 2024 Turkish Statistical Institute | Viz by Akin Orhan", color='black')

plt.savefig('week3-book_reading_Turkey.svg', transparent=True, dpi=300)
plt.show()
