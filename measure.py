import numpy as np


def MAPE(y, y_pred):
    return np.mean(np.abs(percentage_error(np.array(y), np.array(y_pred)))) * 100


def percentage_error(actual, predicted):
    res = np.empty(actual.shape)
    for j in range(actual.shape[0]):
        if actual[j] != 0:
            res[j] = (actual[j] - predicted[j]) / actual[j]
        elif predicted[j] == 0:
            res[j] = 0
        elif np.mean(actual) == 0:
            res[j] = np.abs(predicted[j]) / (
                np.mean(np.abs(predicted)) * len(predicted))
        else:
            res[j] = predicted[j] / np.mean(actual)
    return res


def MAE(y, y_pred):
    return np.mean(np.abs(y - y_pred))
