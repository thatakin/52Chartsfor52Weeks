import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from pyfonts import load_font
import pandas as pd
from highlight_text import ax_text

# - Data Files -
url = "https://github.com/thatakin/52Chartsfor52Weeks/raw/refs/heads/main/Week%201/Vital%20Statistics%20of%20Korea%202026.xlsx"
df = pd.read_excel(url)