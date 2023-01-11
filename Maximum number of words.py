import re
text = "I will go to college tomorrow for sure. I eat apples. This is great thanks very much."

max_words = 0 
sentences = re.split("[.!?]", text)
for sentence in sentences:
 max_words = max( len( sentence.split() ), max_words ) 


print(f"max_words: {max_words}")
