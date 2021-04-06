from tf_idf_test import data_tfidf
from tf_idf_test import papers_tfidf
from AuDoLab.subclasses.one_class_svm import One_Class_SVM
import os
import sys
import numpy as np

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")


nus = np.arange(0.001, 0.5, 0.001)

nus = np.round(nus, 5)

one_Class_SVM = One_Class_SVM()
classifier = one_Class_SVM.classification(
    training=papers_tfidf,
    predicting=data_tfidf,
    nus=nus,
    quality_train=0.85,
    min_pred=0.01,
    max_pred=0.1,
)
