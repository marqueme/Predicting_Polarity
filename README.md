# Predicting_Polarity

The goal of this code is to automatically predict the polarity of reviews. The dataset contains pre-processed positive and negative reviews. 

The code yielded a score for every review by scanning for words deemed postive and negative by an external data source. The score then indicated the label of the review, as either a positive or negative one. 


SETUP
=====
Python 2.7

The dataset is the one used by Pang et al. (2002) 
The dataset consists of two folders, pos and neg, each containing 1000 positive and negative documents, respectively. This data will serve as the test data.

In order to make predictions, a polarity lexicon is needed. The one by Hu and Liu (2004) at
http://www.cs.uic.edu/~liub/FBS/opinion-lexicon-English.rar was obtained. 

This dataset consists of two files, positive-words.txt and negative-words.txt, containing several thousand positive and negative words, respectively. 
