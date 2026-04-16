# import pandas as pd
# duration = list(map(float, input().split()))
# status = input().split()
# df = pd.DataFrame({"duration_sec": duration,
#     "status": status})
# df_ok = df[df["status"] == "ok"]
# print(df_ok["duration_sec"].describe())#Мысал:
# #50 60 40 10 20 30 80
# #ok ok fail error ok ok fail