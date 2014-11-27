from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import numpy as np
import json
from sklearn.svm import SVC
from nltk.corpus import stopwords

class Classifier:

    def __init__(self, texts, labels):
        self.texts = texts
        self.classifier =  SVC()

        # Vectorize
        # mid_df debe ser 2 ;p
        self.vectorizer = CountVectorizer(ngram_range=(1, 1), min_df=1, max_df=0.8,
                                  strip_accents='unicode', stop_words=stopwords.words('spanish'), binary=False)
        self.vectorizer.fit(texts)
        
        # Normalize
        self.tf_transformer = TfidfTransformer(use_idf=False)
        word_counts = self.vectorizer.transform(texts)
        data = self.tf_transformer.fit_transform(word_counts)


        self.classifier.fit(data, labels)

    def get_vector(self, text):
        vector = self.vectorizer.transform([text])
        normalized_vector = self.tf_transformer.fit_transform(vector)
        return normalized_vector

    def classify(self, text):
        vector = self.get_vector(text)
        print(self.classifier.predict(vector))



texts = [
"El primero de ellos es básicamente un control parental bastante personalizable porque permite que los peques usen nuestros equipos sin meterse donde no deben ya que permite escoger e identificar por colores las aplicaciones que ellos pueden utilizar o, en todo caso, ocultarlas cuando el terminal esté en sus manos. En cuanto a Rooms, es básicamente una administración para compartir contenido por grupos, podemos seleccionar ciertos contactos con los que sólo queremos compartir imágenes y otro, por ejemplo, para el trabajo; cada grupo tiene un chat y la posibilidad de compartir imágenes, calendario y más.",
"En cuanto a DataSense, que no es una aplicación que primera vez llegamos a escuchar, vamos a poder tener el control de nuestros datos de navegación, incluso con estadísticas por cada aplicación. La pega está en que en algunos casos será necesario que nuestro operador lo permita."
]

labels = [0, 1]

c =Classifier(texts, labels)
c.classify("este es un texto acerca de app aplicaciones , pequeños")

