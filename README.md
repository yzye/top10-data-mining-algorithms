The article Top 10 algorithms in data mining “presents the top 10 data mining algorithms identified by the IEEE International Conference on Data Mining (ICDM) in December 2006: C4.5, k-Means, SVM, Apriori, EM, PageRank, AdaBoost, kNN, Naive Bayes, and CART.” We will be implementing some of these algorithms in this project.

### K-means
To begin with, we will implement the K-means algorithm. Download a test dataset [“seeds”] (http://archive.ics.uci.edu/ml/datasets/seeds).
We will read in the instances into two lists: instances and labels. The former will a list of 7-dimensional instance. An instance will itself be represented using a list of length 7. The latter will be a list of the labels. Then we run 
`python kmeans.py` in the command line.

### Simple Optimization

In the problem, we will implement two simple optimization algorithms: gradient descent and coordinate descent. 

### Nearest Neighbor Classification

Implement the function nn classifier. Given a point to classify, we first sort examples in train data ac- cording to their distances from point. Then we want to look at the labels of the k-nearest data points. These should get stored in nearest k labels. Then we find the label that occurs the most in nearest k labels and return it. If there are ties, we break them at random.

### Pagerank

run the script using `python pagerank.py`. 

### Support Vector Machine 
Training an SVM using the rbf/gaussian kernel has the best accuracy.

### Adaboost

The first step in the Adaboost loop is to train a weak learner. Remember Adaboost is a “boosting” algorithm: it combines weak classifiers to create a stronger classifier.

### Verifying the Semicircle and Tracy-Widom Laws from Random Matrix Theory [RMT]

In this problem, we will numerically verify two important RMT laws following the algorithmic recipes mentioned in Section 1 of the following article: [http://www-math.mit.edu/~edelman/publications/random_matrix.pdf] (http://www-math.mit.edu/~edelman/publications/random_matrix.pdf)

The ouput looks like:

Semicircle | Tracy-Widom
:-------------------------:|:-------------------------:
![](/res/Semicircle.pdf) | ![](/res/Tracy-Widom.pdf) 

### Creating animation videos for online learning algorithms

In this problem, we will create short video animations for two online learning algorithms for binary classifi- cation: perceptron and online logistic regression. Both algorithms start with a weight vector w ∈ Rd (d will be equal to 2 so that we can plot everything in 2D). They both process the data one example, label pairs at a time.

![](/res/Perceptron_anim.gif) 

### Fetching Alternative Fuel Stations Data via the NREL Web API


In this problem, we will fetch data from the NREL (National Renewable Energy Laboratory) web API described at: [https://developer.nrel.gov/docs/transportation/alt-fuel-stations-v1/nearest/](https://developer.nrel.gov/docs/transportation/alt-fuel-stations-v1/nearest/)

Familiarize yourself with how the API works by browsing the above website. Note that you will have to fill out a form to receive your own private API key: [https://developer.nrel.gov/docs/api-key/] (https://developer.nrel.gov/docs/api-key/)
run `python fuel.py`.



