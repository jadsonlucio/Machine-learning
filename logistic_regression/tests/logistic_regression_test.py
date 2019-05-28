from numpy import array
from sklearn.datasets import load_breast_cancer
from ..regression import LogisticRegression


def test_create_model():
    return LogisticRegression(array([[1],[2],[3],[4]]), array([1,1,0,0]), 0.5, 200) 

def test_train_model():
    return LogisticRegression(array([[1],[2],[3],[4]]), array([1,1,0,0]), 0.5, 200).train() 

def test_train_model_with_breast_cancer_dataset():
    data = load_breast_cancer()["data"]
    target = load_breast_cancer()["target"]

    return LogisticRegression(data, target, 0.75, 1000).train()