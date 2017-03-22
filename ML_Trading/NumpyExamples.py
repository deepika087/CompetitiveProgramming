

import numpy as np

if __name__ == "__main__":
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=int)
    meanVal = np.mean(arr, axis = 1)
    print meanVal
