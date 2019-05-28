from sklearn.datasets import load_breast_cancer
from logistic_regression.regression import LogisticRegression

def logistic_regression_with_breast_cancer():
    data = load_breast_cancer()["data"]
    target = load_breast_cancer()["target"]
    
    model = LogisticRegression(data, target, 0.75, 10)
    model.train()

    return model

if __name__ == "__main__":
    model = logistic_regression_with_breast_cancer()
    model.plot_train_test_results("acurracy")