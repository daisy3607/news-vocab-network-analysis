# News Vocabularies Network Analysis
The project analyzes relations among vocabularies/terms used in Chinese medical news.

After visualizing relations of term usage, you could see which terms often appears together. 

## Procedures

The project composed of three parts:

* Preparing raw data:
Crawling news from media websites, including PEOPO, UDN and etc.
* Processing the corpus:
(1) integrate corpus with different encoding.
(2) cleaning corpus
* Analyze relations among terms
* Visualizing networks
use [Baidu API](http://echarts.baidu.com/examples/editor.html?c=graph-force)


## Requirements
  * NumPy >= 1.12.0
  * Pandas

## File description
  * `parameter.py` includes input/output parameters.
  * `preprocessing.py` includes functions for preprocessing raw data and integrate them.
  * `cal_cofreq.py` does social network analysis and return results of vocabularies relations.
  * `create_sna.py` converts analysis result into nodes & links prepared for visualization later.
 

## Results
![](https://imgur.com/nCVbvR4.jpg)
