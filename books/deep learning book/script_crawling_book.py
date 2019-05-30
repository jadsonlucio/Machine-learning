"""
	Install wkhtmltopdf on https://wkhtmltopdf.org/downloads.html
	copy instalation folder to path variable.

"""


import pdfkit

from time import sleep
from urllib.request import urlopen
from bs4 import BeautifulSoup


PATH = "C:\Program Files\wkhtmltopdf"
PATH_WKTHTMLTOPDF = PATH + "\\bin\\wkhtmltopdf.exe"
CONFIG = pdfkit.configuration(wkhtmltopdf=PATH_WKTHTMLTOPDF)
HTML_FILES_PATH = "html\\"
PDF_FILES_PATH = "pdfs\\"

ignored_tags = [("div", {"class":"robots-nocontent sd-block sd-social sd-social-icon sd-sharing"}),
				("div", {"class":"sharedaddy sd-block sd-like jetpack-likes-widget-wrapper jetpack-likes-widget-loaded"}),
				("div", {"id":"jp-relatedposts"}),
				("nav", {"class":"navigation post-navigation"}),
				("footer", {"id":"colophon"}),
				("aside", {"id":"secondary"}),
				("div", {"class":"col-md-4 col-sm-12 col-xs-12 branding-container"})]



def crawling_chapter(url):
	response = urlopen(url)
	html_text = response.read()
	soup = BeautifulSoup(html_text, 'html.parser')
	print(soup.html)

	for tag, attrs in ignored_tags:
		for element in soup.find_all(tag, attrs): 
			element.decompose()

	return soup.html.__str__()


def crawling_chapters_urls(urls):
	chapters_url = []

	for url in urls:
		response = urlopen(url)
		html_text = response.read()
		soup = BeautifulSoup(html_text, 'html.parser')
		for element in soup.find_all('h4', {"class":"entry-title"}):
			chapters_url.append(element.a.get("href"))

	return chapters_url
			


	return chapters_html

def save_book(book_name,urls):
	cont = 0
	urls = crawling_chapters_urls(urls)
	for url in urls:
		html_chapter = crawling_chapter(url)
		print(html_chapter)
		path = HTML_FILES_PATH + "file_" + str(cont) + ".html"
		with open(path, "w", encoding="utf-8") as f:
			f.write(html_chapter)

		pdfkit.from_file(path, PDF_FILES_PATH+"cap_{0}.pdf".format(cont), configuration=CONFIG)
		sleep(10)
		cont+=1






if __name__ == "__main__":
	book_name = "Deep Learning.pdf"
	save_book(book_name, ["http://deeplearningbook.com.br/capitulos/"])




