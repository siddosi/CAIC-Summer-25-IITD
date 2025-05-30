import numpy as np
import pandas as pd


#WITH GRADIENT DESCENT 

def linearRegression(X: np.array, Y: np.array, lr: float, lambda_: float):
    theta = np.zeros(X.shape[1])
    prev = np.ones(X.shape[1])
    while np.linalg.norm(theta - prev) > 0.01:
        prev = theta.copy()
        gradient = -X.T @ (Y - X @ theta) + lambda_ * theta
        theta -= lr * gradient
    return theta
#uses less memory
def linearRegression_1(X: np.array, Y: np.array, lr: float, lambda_: float):
    theta = np.zeros(X.shape[1])
    for i in range(1000):
        gradient = -X.T @ (Y - X @ theta) + lambda_ * theta
        theta -= lr * gradient
    return theta

#LINEAR REGRESSION in MATRIX FORM WITH NEWTON RALPHSON METHOD, CAN BE DERIVED BY DOING DERIVATIVE = 0
def linearRegression_2(X: np.array, Y: np.array, lr: float, lambda_: float): 
    I = np.eye(X.shape[1])   # identity matrix 
    I[0, 0] = 0  
    X_TX_LAMBDA_INV = np.linalg.inv((X.T)@X + lambda_ * I)
    return X_TX_LAMBDA_INV@(X.T)@Y


'''EXTRA THINGS NOT RELEVANT TO WHAT WAS ASKED FOR SUBMISSION'''

X_train, Y_train = load_dataset('ds4_train.csv' , add_intercept=True)

x_test, y_test = load_dataset('ds4_valid.csv', add_intercept=True)


y_predict = x_test@(linearRegression(X_train,Y_train,0.01,0))
    

print(y_predict)
    
    
#robust dataset loader taken from cs229 if needed 

   
def load_dataset(csv_path, label_col='y', add_intercept=False):
    """Load dataset from a CSV file.

    Args:
         csv_path: Path to CSV file containing dataset.
         label_col: Name of column to use as labels (should be 'y' or 'l').
         add_intercept: Add an intercept entry to x-values.

    Returns:
        xs: Numpy array of x-values (inputs).
        ys: Numpy array of y-values (labels).
    """

    def add_intercept_fn(x):
        global add_intercept
        return add_intercept(x)

    # Validate label_col argument
    allowed_label_cols = ('y', 't')
    if label_col not in allowed_label_cols:
        raise ValueError('Invalid label_col: {} (expected {})'
                         .format(label_col, allowed_label_cols))

    # Load headers
    with open(csv_path, 'r') as csv_fh:
        headers = csv_fh.readline().strip().split(',')

    # Load features and labels
    x_cols = [i for i in range(len(headers)) if headers[i].startswith('x')]
    l_cols = [i for i in range(len(headers)) if headers[i] == label_col]
    inputs = np.loadtxt(csv_path, delimiter=',', skiprows=1, usecols=x_cols)
    labels = np.loadtxt(csv_path, delimiter=',', skiprows=1, usecols=l_cols)

    if inputs.ndim == 1:
        inputs = np.expand_dims(inputs, -1)

    if add_intercept:
        inputs = add_intercept_fn(inputs)

    return inputs, labels
