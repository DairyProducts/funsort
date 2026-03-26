# funsort

A little Python package with fun sorting algorithms. 
Perfect if you would like a simple way to explore and compare various sorting algorithms, 
or if you just want to make your programs less efficient for no reason.

## Usage

For a list of supported algorithms, see [ALGORITHMS.md](ALGORITHMS.md).

You can import a specific sorting function and use it to sort a list. 
For example, to use the `bubble_sort` function:
```python
from funsort import bubble_sort

data = [3, 1, 2]
print(bubblesort(data))
```

This will output:

```
[1, 2, 3]
```

You can also import the package of all prim-and-proper sorting algorithms and use any 
of the available functions. For example:

```python
from funsort import Proper
data = [3, 1, 2]
print(Proper.bubble_sort(data))
```

Likewise, with the esoteric sorting algorithms:

```python
from funsort import Esoteric
data = [3, 1, 2]
print(Esoteric.bogo_sort(data))
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.