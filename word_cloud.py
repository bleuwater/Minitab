from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image
from mtbpy import mtbpy

# Set the maximum number of words for the word cloud.
nWords = 150

# Open and read the dataset into a variable.
dataset = open("coffee_reviews.txt", "r", encoding="utf8").read()

# Change all the characters in the dataset to lowercase.
dataset = dataset.lower()

# Open and read the mask image into a numpy array.
maskArray = np.array(Image.open("cloud.png"))

# Specify the properties of the word cloud.
cloud = WordCloud(background_color = "white", max_words = nWords, mask = maskArray, stopwords = set(STOPWORDS))

# Generate the word cloud.
cloud.generate(dataset)

# Save the word cloud to a png file.
cloud.to_file("word_cloud.png")

# Send the png file to the Minitab output.
mtbpy.mtb_instance().add_image("word_cloud.png")

# Initialize the arrays to store words and their frequencies in a table.
words = []
freqs = []

# Begin a loop to count the words in the word cloud frequency dictionary
for word in cloud.words_:
    # Append the word to the list of words for the table
    words.append(word)
    # Append the frequency of the word to the list of frequencies for the table
    freqs.append(int(cloud.words_[word]*4716))

# Send the table to the Minitab output
mtbpy.mtb_instance().add_table(columns=[words, freqs], headers=["Word", "Frequency"], title="Word Cloud Data", footnote="{0} rows are in this table".format(nWords))