import numpy as np

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps
    
    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HERE
    shape_data = data.shape
    vector = np.ones(shape_data[1])
    for i in range(num_steps):
        prev = vector
        vector = np.dot(data, vector) / np.linalg.norm(np.dot(data, vector))
        lmbd = np.dot(prev, np.dot(data, vector)) / np.dot(prev, prev)
    return float(lmbd), vector
