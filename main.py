import numpy as np
result = duration[status == "ok"]
result = df[df["status"] == "ok"]["duration"]
result = []
for i in range(len(duration)):
    if status[i] == "ok":
        result.append(duration[i])