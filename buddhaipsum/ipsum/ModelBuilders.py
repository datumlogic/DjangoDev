import random

class PageBuilder:

    def __init__(self,filespec):
		#  f.read().splitlines() removed trailing newlines, whereas f.readlines() didn't
		with open('latin_dictionary.txt') as f:
			self.content = f.read().splitlines()

    def buildPage(self,minWords, maxWords, minSentences, maxSentences, numParagraphs):
		highIndexList = len(self.content) - 1
		#generate page
		page = ''
		for v in range(numParagraphs):
			#generate paragraphs
			paragraph = ''
			sentence = ''
			for w in range(random.randint(int(minSentences),int(maxSentences))):
				#generate sentences
				for x in range(random.randint(int(minWords),int(maxWords))):
					word = self.content[random.randint(0,highIndexList)]
					if sentence == '':
						word = word.title()
					sentence += word + " "
				paragraph += sentence.strip() + '. '
				sentence = ''
			page += (paragraph.strip() + '\n\n')
			paragraph = ''
		return page