```python
from fibonacci import fiboo
```


```python
fiboo(17)
```




    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]




```python
from golden_ratio import phy
```


```python
phy()
```

    1.0
    2.0
    1.5
    1.666667
    1.6
    1.625
    1.615385
    1.619048
    1.617647
    1.618182
    1.617978
    1.618056
    1.618026
    1.618037
    1.618033
    1.618034
    A partir de f_ 17 / f_ 16 la division empieza converger a 1.618034 



```python
from Matriz import Matriz
```


```python
x = "1,3|3,1"
A=Matriz(x)
```


```python
A.n
```




    2




```python
A.t()
A.show(A.T)
```

    1.0	3.0
    3.0	1.0



```python
A.show(A.A)
```

    1.0	3.0
    3.0	1.0



```python
A.determinante()
```




    -8.0




```python
A.inversa()
A.show(A.I)
```

    1.0	0.0	-0.125	0.375
    -0.0	1.0	0.375	-0.125

