instruction:

1) run the code with: 
	python indexer.py tccorpus.txt index.txt
	python bm25.py index.txt queries.txt 100 > results.eval


2) files (7 in total):	
	1) source files:
		bm25.py
		indexer.py
	2) given files:
		tccorpus.txt
		queries.txt
		
	3) output files:
		index.txt
		results.eval
	4) readme file:
		readme.txt
	

3) description of implementation:
	1)indexer.py
		1)
		Use nested dictionary to store inverted index.
		Such as,
		{word1:{doc11:tf11, doc12:tf12 }, word2:{doc2:tf2}} 
		2)
		Write length of each document and total number of documents and avdl at the beginning of index.txt
		And the inverted indexes in following
	2)bm25.py
		First read the length of docs, inverted index and queries.
		for each query:
			for each term in query:
				for each doc:
					calculate K
					calculate bm25 score
		



