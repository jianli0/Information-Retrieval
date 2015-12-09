1) environment:
	python:
	Python 2.7.8
	

2) run the code with:

train 
python nbtrain.py /textcat/train/ model.txt

test
python nbtest.py model.txt /textcat/dev/neg/ dev_neg_predictions.txt
python nbtest.py model.txt /textcat/dev/pos/ dev_pos_predictions.txt
python nbtest.py model.txt /textcat/test/ test_predictions.txt

3) percentage of positive and negative reviews in the development data were correctly classified : 61%(positive) ; 73%(negative)

4) files: 10 in total

	nbtrain.py 		(source code)
	nbtest.py 		(source code)

	readme.txt
	posmodel.txt		(parameters get from positive reviews in train set)
	negmodel.txt		(parameters get from negative reviews in train set)
	dev_pos_predictions.txt (scores model assigns to dev reviews positive)
	dev_neg_predictions.txt (scores model assigns to dev reviews negative)
	test_predictions.txt	(scores model assigns to test reviews positive and negative)
	
	top20pos.txt		(20 terms with the highest (log) ratio of positive to negative weight)
	top20neg.txt		(20 terms with the highest (log) ratio of negative to positive weight)
	
	
	


