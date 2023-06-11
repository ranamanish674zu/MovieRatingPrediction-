from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
# pip install nltk
import nltk
nltk.download('stopwords')


def getStemmedReview(review):
    review = review.lower()
    review = review.replace("<br/><br/>", " ")
    # Tokenize
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(review)
    # Remove stopwords
    en_stopwords = set(stopwords.words('english'))
    new_tokens = [token for token in tokens if token not in en_stopwords]
    # Stem tokens
    ps = PorterStemmer()
    stemmed_tokens = [ps.stem(token) for token in new_tokens]
    cleaned_review = ' '.join(stemmed_tokens)
    return cleaned_review
import sys

def getStemmedDocument(inputFile,outputFile):
  out= open(outputFile,'w',encoding="utf8")
  with open(inputFile,encoding="utf8") as f:
    reviews=f.readlines()
  for review in reviews:
    cleaned_review=getStemmedReview(review)
    print((cleaned_review),file=out)
  out.close()
#read command line arguments
inputFile=sys.argv[1]
outputFile=sys.argv[2]
getStemmedDocument(inputFile,outputFile)
