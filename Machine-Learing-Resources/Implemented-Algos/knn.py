import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

def euclidean_distance(x, y):
    #Get euclidian distance
    return np.sqrt(np.sum((x - y)**2))

class KNN:

    def __init__(self, k):
        self.k = k
    
    def fit(self,X,y):
        self.X_train = X
        self.y_train = y

    def predict(self,X):
        predicted_labels = [self._predicted(x) for x in X]
        return np.array(predicted_labels)

    def _predicted(self,x):
        #Compute the distance
        distances = [euclidean_distance(x,x_train) for x_train in self.X_train]

        #Compute the k nearest neighbors
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]

        #Compute the majority vote, getting the most common label
        most_common = Counter(k_nearest_labels).most_common(1)
        
        #Return the most common label
        return most_common[0][0]




#MAIN
if __name__ == "__main__":
    # Imports
    from matplotlib.colors import ListedColormap
    from sklearn import datasets
    from sklearn.model_selection import train_test_split

    cmap = ListedColormap(["#FF0000", "#00FF00", "#0000FF"])

    def accuracy(y_true, y_pred):
        accuracy = np.sum(y_true == y_pred) / len(y_true)
        return accuracy

    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1234
    )

    k = 3
    clf = KNN(k=k)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    print("KNN classification accuracy", accuracy(y_test, predictions))
    plt.scatter(X_test[:, 0], X_test[:, 1], c=predictions, cmap=cmap)
    print(X_test[:, 0])
    plt.show()