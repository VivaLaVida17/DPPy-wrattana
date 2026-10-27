#!/usr/bin/env python3
import numpy as np

arr = np.array([2, 8, 9, 48, 8, 22, -12, 2])

result = set(arr[arr > 5] + 2)

print(arr.tolist())
print(result)