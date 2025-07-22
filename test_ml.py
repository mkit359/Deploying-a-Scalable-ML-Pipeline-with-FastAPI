import pytest
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.data import process_data
from ml.model import train_model, compute_model_metrics, load_model
from train_model import data, train, test, X_train, y_train 


def test_shape_consistency():
    """
    # Makes sure that joining the training and testing set, produces the same shape as the original dataset.
    """

    training_rows = train.shape[0]
    testing_rows = test.shape[0]

    assert data.shape[0] == training_rows + testing_rows



# TODO: implement the second test. Change the function name and input as needed
def test_ML_model_algorithm():
    """
    # Reviewing if the ML model is utilizing the RandomForestClassifier as expected
    """

    model = train_model(X_train, y_train)

    assert isinstance(model, RandomForestClassifier)


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # Reviewing that the precision, recall and fbeta are greater than or equal to 0 and less than or equall to one.
    """
    
    y_true = np.array([0,1,1,0])
    y_pred = np.array([0,1,1,0])

    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)

    assert precision >= 0
    assert precision <= 1
    assert recall >= 0
    assert recall <= 1
    assert fbeta >= 0
    assert fbeta <= 1
