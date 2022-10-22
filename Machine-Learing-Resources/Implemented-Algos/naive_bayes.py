"""
Naive Bayes classifier
Based on Bayes Theorem
Easy explaination : https://www.youtube.com/watch?v=O2L2Uv9pdDA
It assumes that: 
    - the data is independent
    - P(y|X) = P(X|y) * P(y) / P(X)
    - P(y|X) = P(x1|y) * P(x2|y) * ... * P(xn|y) * P(y) / P(X)
Need to select the highest probability
y = argmax(P(y|X)) = argmax(P(x1|y) * P(x2|y) * ... * P(xn|y) * P(y) / P(X))
y = argmax(P(y|X)) = argmax(P(x1|y) * P(x2|y) * ... * P(xn|y) * P(y))
If number to short, overflow problem, so use the Loagrithm operation, that changes from multiplication to sum
y = argmax( log(P(x1|y)) + log(P(x2|y)) + ... + log(P(xn|y)) + log(P(y)) )

Class conditional probability
P(xi|y) = 1/ sqrt(2*pi*sigma^2) * e^(-1/2 * (xi-mu)^2 / sigma^2)

Sometimes is added an extra "ALPHA" to avoid that there is a value that is 0 because one signle data is not in the sample
Or you can use log ( I think, but not sure )

Naive Bayes is a good classifier when the data is independent
Naive Bayes is a bad classifier when the data is dependent

Naive Bayes is naive because it does not care about order of data
It uses words like they are in a bag, in no particular order. Only the probability is important
Because of that, it has a large bias, but low variance
"""

import numpy as np

class NaiveBayes:

    def fit(self, X, y):
        # Get the dimension of the dataset
        n_samples, n_features = X.shape
        
        # Return the sorted unique elements of the array
        self.__classes = np.unique(y) 
        # Get the length of the classes, to then caluclate the prior probability
        n_classes = len(self.__classes)

        # init mean, variance and prior probability
        self.__mean = np.zeros((n_classes, n_features), dtype=np.float64)
        self.__var = np.zeros((n_classes, n_features), dtype=np.float64)
        self.__priors = np.zeros(n_classes, dtype=np.float64)

        for c in self.__classes:
            # Get the index of the class
            x_c = X[y == c]
            # Get the mean of the class
            self.__mean[c, :] = x_c.mean(axis=0)
            # Variance calculation
            self.__var[c, :] = x_c.var(axis=0)
            # Frequency of prior probability
            self.__priors[c] = x_c.shape[0] / float(n_samples)   


    def predict(self, X):
        # Predict calculating for each class the probability and chosing
        y_pred = [self._predic(x) for x in X]
        return y_pred

    def _predict(self, x):
        posteriors = []

        for idx, c in enumerate(self.__classes):
            # Calculate the probability of the class
            prior = np.log(self.__priors[idx])
            class_conditional = np.sum(np.log(self._probability_density_function(idx, x)))
            posterior = prior + class_conditional
            posteriors.append(posterior)

        return self.__classes[np.argmax(posteriors)]


    def _probability_density_function(self, class_idx, x):
        mean = self.__mean[class_idx]
        var = self.__var[class_idx]
        numerator = np.exp(- (x - mean)**2 / (2 * var))
        denominator = np.sqrt(2 * np.pi * var)
        return numerator / denominator