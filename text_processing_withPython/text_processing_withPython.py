# Sample text for processing
text = """
Artificial Intelligence (AI) and Machine Learning (ML) are powerful technologies that are transforming our world in remarkable ways.
AI enables computers to perform tasks that once required human intelligence, such as recognizing images, understanding speech, and making complex decisions.
Machine Learning, a branch of AI, allows computers to learn and improve from experience without explicit programming.
Together, AI and ML power applications like recommendation systems, voice assistants, and autonomous vehicles.
Their ability to analyze massive amounts of data and uncover patterns makes them essential tools in areas ranging from healthcare to finance.
The advancements in AI and ML continue to push the boundaries of innovation, making them some of the most exciting fields in technology today.
"""

import re

# Convert text to lowercase
cleaned_text = text.lower()

# Remove special characters and numbers, keeping only letters and spaces
cleaned_text = re.sub(r'[^a-z\s]', '', cleaned_text)

# Display cleaned text
print("Cleaned Text:")
print(cleaned_text)

from collections import Counter

# Split the cleaned text into individual words
words = cleaned_text.split()

# Count the frequency of each word
word_counts = Counter(words)

# Display the 10 most common words
print("Most Common Words:")
print(word_counts.most_common(10))

