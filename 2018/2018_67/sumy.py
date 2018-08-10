import csv
import os
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Lsa
from sumy.summarizers.luhn import LuhnSummarizer as Luhn
from sumy.summarizers.text_rank import TextRankSummarizer as TxtRank
from sumy.summarizers.lex_rank import LexRankSummarizer as LexRank
from sumy.summarizers.sum_basic import SumBasicSummarizer as SumBasic
from sumy.summarizers.kl import KLSummarizer as KL
from sumy.summarizers.edmundson import EdmundsonSummarizer as Edmundson
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

LANGUAGE = "english"
SENTENCES_COUNT = 1

urlinput = os.path.join(os.path.dirname(__file__), input('Enter input text file: '))
urls = open(urlinput, "r")

outputcsv = os.path.join(os.path.dirname(__file__), input('Enter a filename (minus file extension): ')+'.csv')

f = csv.writer(open(outputcsv, "w+", newline="\n", encoding="utf-8"))
f.writerow(["URL", "Copy", "Summarization Algorithm"])

for line in iter(urls):
	stemmer = Stemmer(LANGUAGE)
	
	lsaSummarizer = Lsa(stemmer)
	lsaSummarizer.stop_words = get_stop_words(LANGUAGE)
	
	luhnSummarizer = Luhn(stemmer)
	luhnSummarizer.stop_words = get_stop_words(LANGUAGE)
	# edmundsonSummarizer.bonus_words = get_bonus_words
	
	lexrankSummarizer = LexRank(stemmer)
	lexrankSummarizer.stop_words = get_stop_words(LANGUAGE)
	
	textrankSummarizer = TxtRank(stemmer)
	textrankSummarizer.stop_words = get_stop_words(LANGUAGE)
	
	sumbasicSummarizer = SumBasic(stemmer)
	sumbasicSummarizer.stop_words = get_stop_words(LANGUAGE)
	
	klSummarizer = KL(stemmer)
	klSummarizer.stop_words = get_stop_words(LANGUAGE)
	
	parser = HtmlParser.from_url(line, Tokenizer(LANGUAGE))
	
	for sentence in lsaSummarizer(parser.document, SENTENCES_COUNT):
		print(sentence)
		f.writerow([line,sentence,"LSA"])
	print("Summarizing URL via LSA: " + line)
	
	for sentence in luhnSummarizer(parser.document, SENTENCES_COUNT):
		print(sentence)
		f.writerow([line,sentence,"Luhn"])
	print("Summarizing URL via Luhn: " + line)	

	for sentence in lexrankSummarizer(parser.document, SENTENCES_COUNT):
		print(sentence)
		f.writerow([line,sentence,"LexRank"])
	print("Summarizing URL via LexRank: " + line)	

	for sentence in textrankSummarizer(parser.document, SENTENCES_COUNT):
		print(sentence)
		f.writerow([line,sentence,"TextRank"])
	print("Summarizing URL via TextRank: " + line)
	
	for sentence in sumbasicSummarizer(parser.document, SENTENCES_COUNT):
		print(sentence)
		f.writerow([line,sentence,"SumBasic"])
	print("Summarizing URL via SumBasic: " + line)	

	for sentence in klSummarizer(parser.document, SENTENCES_COUNT):
		print(sentence)
		f.writerow([line,sentence,"KL-Sum"])
	print("Summarizing URL via KL-Sum: " + line)
	
urls.close()
print ("Writing to " + outputcsv + " complete.")
