from numpy import array
from ..regression import LogisticRegression

def test_create_model():
    return LogisticRegression(array([[1],[2],[3],[4]]), array([1,1,0,0]), 0.5, 200) 

def test_train_model():
    return LogisticRegression(array([[1],[2],[3],[4]]), array([1,1,0,0]), 0.5, 200).train() 