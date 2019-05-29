"""
	Install wkhtmltopdf on https://wkhtmltopdf.org/downloads.html
	copy instalation folder to path variable.

"""

import pdfkit
import urllib3
from urllib.request import urlopen
from bs4 import BeautifulSoup
from requests import get

PATH = "C:\Program Files\wkhtmltopdf"
PATH_WKTHTMLTOPDF = PATH + "\\bin\\wkhtmltopdf.exe"
CONFIG = pdfkit.configuration(wkhtmltopdf=PATH_WKTHTMLTOPDF)
HTML_FILES_PATH = "html\\"

ignored_tags = [("div", {"class":"robots-nocontent sd-block sd-social sd-social-icon sd-sharing"}),
				("div", {"class":"sharedaddy sd-block sd-like jetpack-likes-widget-wrapper jetpack-likes-widget-loaded"}),
				("div", {"id":"jp-relatedposts"}),
				("nav", {"class":"navigation post-navigation"}),
				("footer", {"id":"colophon"}),
				("aside", {"id":"secondary"})]



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
	files_paths = []
	for url in urls:
		html_chapter = crawling_chapter(url)
		print(html_chapter)
		path = HTML_FILES_PATH + "file_" + str(cont)
		files_paths.append(path)
		with open(path, "w") as f:
			f.write(html_chapter.encode("utf-8").decode("utf-8"))

		cont+=1


	pdfkit.from_file(files_paths, book_name, configuration=CONFIG)



if __name__ == "__main__":
	book_name = "Deep Learning.pdf"
	save_book(book_name, ["http://deeplearningbook.com.br/capitulos/"])




