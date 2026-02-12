from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

texts = [
    # Greeting
    "ආයුබෝවන්",
    "හයි",
    "hello",
    "hi",
    "good morning",
    
    # FAQ
    "ලයිබ්රරි කවදාද විවෘත වෙන්නේ",
    "ලයිබ්රරි වෙලාව කියන්න",
    "library time eka kiyanna",
    "ලයිබ්රරි open වෙන වෙලාව",
    "library open time",
    
    # University
    "විශ්වවිද්‍යාලය ගැන කියන්න",
    "මෙය කුමන විශ්වවිද්‍යාලයක්ද",
    "university info",
    "විශ්වවිද්‍යාල තොරතුරු",
    "about university",
    
    # Smalltalk
    "ඔබ කොහොමද",
    "කොහොමද",
    "ඔයා හොඳින්ද",
    "how are you",
    "ඔබ හොඳින්ද"
]

labels = [
    # Greeting
    "greeting","greeting","greeting","greeting","greeting",
    
    # FAQ
    "faq","faq","faq","faq","faq",
    
    # University
    "university","university","university","university","university",
    
    # Smalltalk
    "smalltalk","smalltalk","smalltalk","smalltalk","smalltalk"
]


vectorizer = TfidfVectorizer(
    ngram_range=(1,2),
    analyzer='word',
    token_pattern=r"(?u)\b\w+\b"
)

X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

with open("model/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("model/intent_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Intent model trained successfully")
