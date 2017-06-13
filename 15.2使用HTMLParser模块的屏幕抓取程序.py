from urllib import urlopen
from HTMLParser import HTMLParser

class SCraper(HTMLParser):
	"""docstring for SCraper"""
	
	in_h3 = False
	in_link = False

	def handle_starttag(self, tag, atrrs):
		atrrs = dict(atrrs)
		if tag == 'h3':
			self.in_h3 = True
			
		if tag == 'a' and 'href' in atrrs:
			self.in_link = True
			self.chunks = []
			self.url = atrrs['href']

	def handle_data(self, data):
		if self.in_link:
			self.chunks.append(data)

	def handle_endtag(self, tag):
		if tag == 'h3':
			self.in_h3 = False
		if tag == 'a':
			if self.in_h3 and self.in_link:
				print '%s (%s)' %(''.join(self.chunks), self.url)
			self.in_link = False

text = urlopen('http://python.org/community/jobs').read()
parser = SCraper()
parser.feed(text)
parser.close()
