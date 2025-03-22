import numpy as np

def mean_absolute_error(true, pred):

    """

    Calculates the Mean Absolute Error (MAE) between the true and predicted values.

        Args:

            true (numpy.ndarray): An array of true values.

            pred (numpy.ndarray): An array of predicted values.

        Returns:

            float: The Mean Absolute Error.

    """

    mae = np.mean(np.abs(true - pred))

    return mae
 
