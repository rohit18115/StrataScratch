import pandas as pd
import re

# Start writing code
google_word_lists.head()
mark = [
    num
    for num, i in enumerate(google_word_lists["words1"])
    if bool(re.search("^g|,g", i))
]
mark1 = [
    num
    for num, i in enumerate(google_word_lists["words2"])
    if bool(re.search("^g|,g", i))
]
google_word_lists.iloc[mark + mark1, :]
