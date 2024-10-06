from citation_maker import CitationMaker

if __name__ == "__main__":
    maker = CitationMaker(src="input_urls.txt", des="output_citation.txt")
    maker.make_citation()
    maker.post_process()