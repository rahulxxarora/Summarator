import math

from formatter import *

#####################################################################
# Author : Rahul Arora
# Email  : coderahul94@gmail.com
#####################################################################


def sentences_intersection(a, b):
	a_set = set(a.split(' '))
	b_set = set(b.split(' '))

	if (len(a_set)+len(b_set))==0:
		return 0

	return float(len(a_set.intersection(b_set)))/float(len(a_set)+len(b_set))

def get_sentences_rank(text):
	sentences_score_dic   = {}
	sentences_mapping_dic = {}
	sentences       	  = content_to_sentences(text)
	total_sentences 	  = len(sentences)
	values          	  = [[0 for x in xrange(total_sentences)] for x in xrange(total_sentences)]

	for i in range(0, total_sentences):
		for j in range(0, total_sentences):
			values[i][j] = sentences_intersection(sentences[i], sentences[j])

	for i in range(0, total_sentences):
		score = 0
		
		for j in range(0, total_sentences):
			if i == j:
				continue
			score += values[i][j]

		sentences_mapping_dic[format_sentence(sentences[i])] = sentences[i]
		sentences_score_dic[format_sentence(sentences[i])]   = score

	return sentences_score_dic

def get_best_sentence(paragraph, sentences_dic):
	sentences              = content_to_sentences(paragraph)
	total_sentences        = len(sentences)
	selection_factor       = math.ceil((0.4)*(total_sentences))
	best_sentences         = []
	selected_sentences_ctr = 0

	while selected_sentences_ctr < selection_factor:
		best_sentence = ''
		max_value     = 0

		for s in sentences:
			strip_s = format_sentence(s)
			if strip_s:
				if sentences_dic[strip_s] > max_value and s not in best_sentences:
					max_value     = sentences_dic[strip_s]
					best_sentence = s

		selected_sentences_ctr += 1
		best_sentences.append(best_sentence)

	return ''.join(s for s in best_sentences)

def get_summary(temp_content):
	sentences_score_dic = get_sentences_rank(temp_content)
	summarized_content  = []

	paragraphs = content_to_paragraphs(temp_content)

	for p in paragraphs:
		sentence = get_best_sentence(p, sentences_score_dic).strip()
		if sentence:
			if sentence[-1] != '.':
				sentence = sentence + '.'
			summarized_content.append(sentence)

	return ('\n').join(summarized_content)