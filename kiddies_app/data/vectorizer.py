from sklearn.feature_extraction.text import CountVectorizer
import joblib

#tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle')

f = open('story.txt',encoding='utf-8', errors='ignore')
text = f.readlines()

# Vectorize the text
vectorizer = CountVectorizer(stop_words='english', min_df=0.0001)
X = vectorizer.fit_transform(text)

# Save the model
joblib.dump(vectorizer, 'vectors.joblib')

#import re
#string = ""
#with open("story.txt") as file:
#    for line in file:
 #       for l in re.split(r"(\. |\? |\! )",line):
  #          string += l +"\n"
#print(string)
#print = (file.splitlines())
#vectorizer = CountVectorizer(stop_words='english', min_df=0.0001)
#X = vectorizer.fit_transform(file)

# Save the model
#joblib.dump(vectorizer, 'vectorizer.joblib')