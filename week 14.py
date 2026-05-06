import numpy as np
import json
class week14:
    def __init__(self):
        self.values = []
    def load_from_file(self):
        filename = input("Введите имя файла (или Enter чтобы пропустить): ")
        if not filename:
            return False
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.values = data.get("values", [])
                return True
        except:
            print("Не удалось прочитать файл")
            return False
    def add_values(self):
        nums = input("Введите числа через пробел: ")
        self.values = list(map(float, nums.split()))
    def calculate(self):
        if not self.values:
            return {"error": "no data"}
        arr = np.array(self.values)
        return {"p50": float(np.percentile(arr, 50)),
            "p90": float(np.percentile(arr, 90)),
            "p99": float(np.percentile(arr, 99)),
            "fail_rate": float(np.mean(arr > 0))}
w = week14()
if not w.load_from_file():
    w.add_values()
result = w.calculate()
print(result)
#Мысал:10 20 30 40 50
