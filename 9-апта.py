#9 esep
import numpy as np
def get_successful_durations(duration_sec, status):
    duration_sec = np.array(duration_sec)
    status = np.array(status)
    return duration_sec[status == 'ok']
durations = list(map(int, input("Введите длительности: ").split()))
statuses = input("Введите статусы: ").split()
result = get_successful_durations(durations, statuses)
print("Время успешных запросов:",result)
print("Среднее время успешных запросов:",sum(result)/len(result))
#input-қа мысал:50 60 40 10 20 30 80
#input-қа мысал:ok ok fail error ok ok fail