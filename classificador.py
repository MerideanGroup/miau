from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import numpy as np
import json
from sklearn.svm import SVC
from nltk.corpus import stopwords
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier

import numpy as np
import matplotlib as mlp
import matplotlib.pyplot as plt
from sklearn import decomposition

class Classifier:

    def __init__(self, texts, labels, weights):
        self.texts = texts
        self.classifier = linear_model.LogisticRegression()

        # Vectorize
        self.vectorizer = CountVectorizer(ngram_range=(1, 1), min_df=0.0, max_df=0.9,
                                  strip_accents='unicode', stop_words=stopwords.words('spanish'), binary=False)
        self.vectorizer.fit(texts)
        word_counts = self.vectorizer.transform(texts)
        # Normalize
        self.tf_transformer = TfidfTransformer(use_idf=True)
        data = self.tf_transformer.fit_transform(word_counts)

        n_eigenfaces = 200
        self.pca = decomposition.RandomizedPCA(n_components=n_eigenfaces, whiten=True)
        pca_features = self.pca.fit_transform(data.toarray() )

        #with plt.style.context('cev_plot'):
        # revisando que el numero de eigenfaces tenga sentido..
        plt.figure(figsize=(8, 6))
        plt.title('cev vs eigenFace')
        plt.plot(self.pca.explained_variance_ratio_.cumsum())
        plt.show()

        self.classifier.fit(pca_features, labels)

    def get_vector(self, text):
        vector = self.vectorizer.transform([text])
        normalized_vector = self.tf_transformer.transform(vector)
        vector = self.pca.transform(vector.toarray() )
        return vector

    def classify(self, text):
        vector = self.get_vector(text)
        print("%s : %s"%(self.classifier.predict(vector), text))

