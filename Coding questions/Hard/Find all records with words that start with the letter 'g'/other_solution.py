import pandas as pd

# Start writing code
google_word_lists.head()

result = google_word_lists.loc[
    lambda x: (x.words1.str.contains("^g|,g")) | (x.words2.str.contains("^g|,g"))
]
