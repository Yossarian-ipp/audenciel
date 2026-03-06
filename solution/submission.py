from sklearn.ensemble import IsolationForest


# The submission here should simply be a function that returns a model
# compatible with scikit-learn API
def get_model():
    return IsolationForest() # will give labels like -1 or 1, not 0 or 1, so might be bad depebnding on what was done for the labelingh part of the data
