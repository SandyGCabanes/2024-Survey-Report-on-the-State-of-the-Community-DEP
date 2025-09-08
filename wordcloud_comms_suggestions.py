# sandy.g.cabanes
# Date: April 4, 2025
# ------------------------------------------------------------
""" This code creates a wordcloud from the open-end question."""
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import random #for the color function

# Function to generate colors
def new_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
   return random.choice(["#152B79", "#B9191E", "#DD9404", "#2F4293", "#FEB303", "#D22D2D"])

# Text from a file (using open)
with open('text_only.txt', 'r') as file:
    text_wc = file.read()

# Generate Word Cloud
wordcloud = WordCloud(width=3200, height=1600, background_color='white').generate(text_wc)

# Use the color function
wordcloud = wordcloud.recolor(color_func=new_color_func)

# Display Word Cloud
plt.figure(figsize=(320, 160))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()