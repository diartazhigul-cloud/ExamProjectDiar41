import numpy as np
class Week10:
    def __init__(self, percentiles=[50, 90, 95]):
        self.percentiles = percentiles
    def calculate_percentiles(self, data):
        arr = np.array(data, dtype=np.float64)
        arr = arr[~np.isnan(arr)]
        if arr.size == 0:
            return [np.nan] * len(self.percentiles)
        return np.percentile(arr, self.percentiles)
successful_scores = input("Введите значения: ").split()
week10 = Week10()
result = week10.calculate_percentiles(successful_scores)
print("Перцентили 50, 90, 95:", result)
# Мысал input:
# 10 50 60 80 10 40