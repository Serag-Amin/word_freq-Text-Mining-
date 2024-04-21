import nltk
from nltk.corpus import stopwords
from collections import Counter


# Read the text file
with open('paragraphs.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Tokenize the text into words
words = nltk.word_tokenize(text)

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_words = [word.lower() for word in words if word.lower() not in stop_words]

# Count word frequency
word_count = Counter(filtered_words)

# Get the 15 most common words
most_common_words = word_count.most_common(15)

# Print the most common words
print("Top 15 Most Common Words:")
for word, count in most_common_words:
    print(f"{word}: {count}")

