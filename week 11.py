# import pandas as pd
# class Week11:
#     def __init__(self, duration, status):
#         self.df = pd.DataFrame({
#             "duration_sec": duration,
#             "status": status})
#     def filter_ok(self):
#         return self.df[self.df["status"] == "ok"]
#     def describe_ok(self):
#         df_ok = self.filter_ok()
#         return df_ok["duration_sec"].describe()
#     def run(self):
#         return self.describe_ok()
# duration = list(map(float, input().split()))
# status = input().split()
# task = Week11(duration, status)
# print(task.run())
#50 60 40 10 20 30 80
#ok ok fail error ok ok fail