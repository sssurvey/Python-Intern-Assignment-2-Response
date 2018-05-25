# Task 1 solution README
#### Required Modules:
---
```python
# using python 3.6.3 running on MacOS version 10.13.4
import os
import subprocess
import pandas as pd # for clean looking report, newest pandas version
import time as t
from subprocess import Popen
```
---
#### Output Result:
```console
haominshi@dhcp93:~/GitRepo/Python-Intern-Assignment-2-Response$ python Answer.py
++++++++++++++++++++++++++++++++++++++++
Executing cmd ---> 0 ---> sleep 3
Executing cmd ---> 1 ---> ls -l /
Executing cmd ---> 2 ---> find /
Executing cmd ---> 3 ---> sleep 4
Executing cmd ---> 4 ---> find /usr
Executing cmd ---> 5 ---> date
Executing cmd ---> 6 ---> sleep 5
Executing cmd ---> 7 ---> uptime
++++++++++++++++++++++++++++++++++++++++
Executing cmd ---> 0 ---> sleep 3
Executing cmd ---> 1 ---> ls -l /
Executing cmd ---> 2 ---> find /
Executing cmd ---> 3 ---> sleep 4
Executing cmd ---> 4 ---> find /usr
Executing cmd ---> 5 ---> date
Executing cmd ---> 6 ---> sleep 5
Executing cmd ---> 7 ---> uptime
++++++++++++++++++++++++++++++++++++++++
Executing cmd ---> 0 ---> sleep 3
Executing cmd ---> 1 ---> ls -l /
Executing cmd ---> 2 ---> find /
Executing cmd ---> 3 ---> sleep 4
Executing cmd ---> 4 ---> find /usr
Executing cmd ---> 5 ---> date
Executing cmd ---> 6 ---> sleep 5
Executing cmd ---> 7 ---> uptime
------------ Total Elapsedtime ------------
The avg total elapsed time when execute these cmds concurrently is: 
49.809443632761635
The avg total elapsed time when execute these cmds one by one is: 
64.31032840410869
------------ Overview ------------
          0         1          2         3         4         5         6         7
0  3.001968  0.017033  48.083046  4.001019  2.275434  0.005208  5.001420  0.002936
1  3.003887  0.023406  50.741262  4.001721  2.713882  0.006915  5.001996  0.003697
2  3.006751  0.023685  50.568169  4.001580  2.423175  0.012549  5.004983  0.005263
* vertical index indicates each run
* column index indicates each command
------------ Final Report ------------
              0         1          2         3         4         5         6         7
count  3.000000  3.000000   3.000000  3.000000  3.000000  3.000000  3.000000  3.000000
mean   3.004202  0.021375  49.797492  4.001440  2.470830  0.008224  5.002800  0.003965
std    0.002407  0.003762   1.487274  0.000371  0.223075  0.003841  0.001913  0.001186
min    3.001968  0.017033  48.083046  4.001019  2.275434  0.005208  5.001420  0.002936
25%    3.002928  0.020219  49.325608  4.001300  2.349305  0.006062  5.001708  0.003317
50%    3.003887  0.023406  50.568169  4.001580  2.423175  0.006915  5.001996  0.003697
75%    3.005319  0.023545  50.654715  4.001650  2.568529  0.009732  5.003489  0.004480
max    3.006751  0.023685  50.741262  4.001721  2.713882  0.012549  5.004983  0.005263
NOTE 1: mean is avg elapsed time
NOTE 2: min is minimum elapsed time
NOTE 3: max is maximum elapsed time
```

