#!/usr/bin/env python3
import numpy as np

arr = np.array([5, 3, -7, 8 , 9 , 11])

result = arr[arr > 5] + 2

print(arr.tolist())
print(result.tolist())