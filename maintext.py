import textrank

textrank.setup_environment()
filename = 'tests/bmw/bmw.txt'
with open(filename) as f:
	summary = textrank.extract_sentences(f.read(), 108)
	print(summary)
	text_file = open("tests/bmw/Output.txt", "w")
	text_file.write(summary)
	text_file.close()
