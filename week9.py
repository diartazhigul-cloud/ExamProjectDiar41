# import numpy as np
# class Week9:
#     def __init__(self):
#         pass
#     def get_successful_durations(self, duration_sec, status):
#         duration_sec = np.array(duration_sec)
#         status = np.array(status)
#         return duration_sec[status == 'ok']
#     def average_successful(self, durations):
#         if len(durations) == 0:
#             return 0
#         return sum(durations) / len(durations)
# durations = list(map(int, input("Введите длительности: ").split()))
# statuses = input("Введите статусы: ").split()
# week9 = Week9()
# result = week9.get_successful_durations(durations, statuses)
# avg = week9.average_successful(result)
# print("Время успешных запросов:", result)
# print("Среднее время успешных запросов:", avg)
#Мысал:
#50 60 40 10 20 30 80
#ok ok fail error ok ok fail