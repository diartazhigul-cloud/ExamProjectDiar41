import numpy as np
def calculate_percentiles(data, percentiles=[50, 90, 95]):
    arr = np.array(data, dtype=np.float64)
    arr = arr[~np.isnan(arr)]
    if arr.size == 0:
        return [np.nan] * len(percentiles)
    return np.percentile(arr, percentiles)
successful_scores = input("Введите значения: ").split()
result = calculate_percentiles(successful_scores)
print("Перцентили 50, 90, 95:", result)
#input-қа мысал: 10 50 60 80 10 40