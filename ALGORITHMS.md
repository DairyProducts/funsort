# Supported Algorithms
All algorithms below support `inPlace=False` by default and return a sorted list.
With `inPlace=True`, they mutate and return the original list.

## Proper Algorithms
Found in the `Proper` subpackage. These are, as the name implies,
"proper" sorting algorithms that are relatively efficient and commonly used in practice.

Import with `from funsort import Proper` or
`from funsort.Proper import <algorithm>`.

| Algorithm | Function Name | File Name | Best Case | Worst Case | Average Case | Notes |
|-----------|---------------|-----------|-----------|------------|--------------|-------|
| Bubble Sort | `bubble_sort` | `bubble.py` | O(n) | Ω(n^2) | Θ(n^2) | Includes early-exit optimization when a pass makes no swaps. |
| Counting Sort | `counting_sort` | `count.py` | O(n + k) | Ω(n + k) | Θ(n + k) | `int` only; supports negatives via offset by `min(data)`. |
| Heap Sort | `heap_sort` | `heap.py` | O(n log n) | Ω(n log n) | Θ(n log n) | Comparison-based in-place heapify/extract implementation. |
| Insertion Sort | `insertion_sort` | `insertion.py` | O(n) | Ω(n^2) | Θ(n^2) | Best case occurs for already sorted input. |
| Merge Sort | `merge_sort` | `merge.py` | O(n log n) | Ω(n log n) | Θ(n log n) | Uses recursive split/merge; allocates temporary lists. |
| Quick Sort | `quick_sort` | `quick.py` | O(n log n) | Ω(n^2) | Θ(n log n) | Uses middle-element pivot with list comprehensions. |
| Radix Sort | `radix_sort` | `radix.py` | O(n · k) | Ω(n · k) | Θ(n · k) | Non-negative `int` values only. |
| Selection Sort | `selection_sort` | `selection.py` | O(n^2) | Ω(n^2) | Θ(n^2) | Always performs nested scans for minimum. |

## Esoteric Algorithms
Found in the `Esoteric` subpackage. These are intentionally impractical,
joke, or experimental algorithms.

Import with `from funsort import Esoteric` or
`from funsort.Esoteric import <algorithm>`.

| Algorithm | Function Name | File Name | Best Case | Worst Case | Average Case | Notes |
|-----------|---------------|-----------|-----------|------------|--------------|-------|
| ADHD Sort | `adhd_sort` | `adhd.py` | O(n^2) | Ω(n^2) | Θ(n^2) | Bubble sort but the interpreter has ADHD. |
| Bogo Sort | `bogo_sort` | `bogo.py` | O(n!) | Ω(∞) | Θ(n!) | Randomly shuffles until sorted. |
| Bozo Sort | `bozo_sort` | `bozo.py` | O(n^2) | Ω(∞) | Θ(n^2) | Randomly swaps two elements until sorted. |
| Intelligent Design Sort | `intelligent_design_sort` | `intelligentdesign.py` | O(1) | Ω(1) | Θ(1) | Returns a copy unchanged; does **not** sort unsorted input. |
| Miracle Sort | `miracle_sort` | `miracle.py` | O(n log n) | Ω(n log n) | Θ(n log n) | If unsorted, waits for a miracle to sort the list. |
| Schrödinger Sort | `schrodinger_sort` | `schrodinger.py` | O(n) | Ω(n log n) | Θ(n log n) | Randomly returns either sorted output or unchanged copy. |
| 6-7 Sort | `six_seven_sort` | `sixseven.py` | O(n) | Ω(n) | Θ(n) | Keeps only values equal to `6` or `7`, then sorts. |
| Sleep Sort | `sleep_sort` | `sleep.py` | O(n + max(data)) | Ω(n) | Θ(n + max(data)) | Non-negative `int`/`float` only; output timing depends on thread scheduling. |
| Stalin Sort | `stalin_sort` | `stalin.py` | O(n) | Ω(n) | Θ(n) | Removes out-of-order elements; result is non-decreasing subsequence, not full sort. |
| Stooge Sort | `stooge_sort` | `stooge.py` | O(n^2.7095) | Ω(n^2.7095) | Θ(n^2.7095) | Extremely inefficient recursive sorting algorithm. |
| Thanos Sort | `thanos_sort` | `thanos.py` | O(n) | Ω(n) | Θ(n) | Repeatedly keeps every other element; output may be reduced to one element. |