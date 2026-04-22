class week12:
    def __init__(self):
        self.data = []
        self.fail_value = "fail"
    def get_input(self):
        self.data = input("Пробел арқылы жазыныз:\n").split()
        self.fail_value = input("не санайын? success? error?\n").lower()
    def calculate(self):
        if not self.data:
            print("Нет данных")
            return
        data_lower = [x.lower() for x in self.data]
        fail_count = data_lower.count(self.fail_value)
        total = len(data_lower)
        fail_ratio = fail_count / total
        return fail_count, fail_ratio
    def show_result(self):
        result = self.calculate()
        if result:
            count, ratio = result
            print("Количество:", count)
            print("Доля:", round(ratio, 4))
obj = week12()
obj.get_input()
obj.show_result()
#Мысал:
#ok fail FAIL success fail error