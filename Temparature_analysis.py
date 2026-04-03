import numpy as np
import time
celsius = np.array([22,25,28,24,26])
print(f"Celsius:{celsius}")
fahrenheit =(celsius*1.8)+32
print(f"Fahrenheit:{fahrenheit}")
average = fahrenheit.mean()
print(f"Average:{average}")
arr=np.array([85,90,78,92,88,76,95,82,89,91,87,84])
print(f"shape:{np.shape(arr)}")
print(f"Total:{len(arr)}")
print(f"Highest score:{max(arr)}")
print(f"Lowest score:{min(arr)}")
print(f"Range:{np.ptp(arr)}")
arr_1=np.arange(1,50001)
start=time.time()
numpy_time=time.time()-start
arr=np.sum(arr_1)
print(f"NumPy Sum:{arr}")
list_1=range(1,50001)
li=sum(list_1)
print(f"Python Sum:{li}")
start=time.time()
python_time=time.time()-start
speed_up=python_time/numpy_time
print(f"NumPy time:{round(numpy_time,4)}")
print(f"Python time:{round(python_time,4)}")
print(f"numpy is {speed_up:.1f}x faster")