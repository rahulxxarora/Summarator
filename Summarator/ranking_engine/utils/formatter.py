from nltk.stem.porter import *
from nltk.corpus import stopwords

#####################################################################
# Author : Rahul Arora
# Email  : coderahul94@gmail.com
#####################################################################
STEMMER = PorterStemmer()


#####################################################################
# Utility methods for formatting text
#####################################################################
def get_roots(sentence):
	temp = [STEMMER.stem(i) for i in sentence]
	return temp

def remove_noise(sentence):
	raw_text = []

	stop = set(stopwords.words('english'))
	temp = [i for i in sentence.lower().split() if i not in stop]
	raw_text = get_roots(temp)
	return  ' '.join(map(str, raw_text))

def content_to_paragraphs(text):
	return text.split('\n\n')

def content_to_sentences(text):
	text = text.replace('\n','. ')
	response = []
	sent = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
	for s in sent:
		response.append(s)
	return response

def format_sentence(text):
	return ''.join(e for e in text if e.isalnum())