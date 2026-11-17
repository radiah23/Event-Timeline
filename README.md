# Event Timeline (Python · Doubly Linked List)

**A chronological event manager built on a doubly linked list I implemented from scratch, with in-place insertion sort and search from either end.**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Data Structures](https://img.shields.io/badge/topic-linked%20lists-blue)

---

## What it does

A `timeline` stores `event` objects (a date and an optional description) as nodes linked in both directions, so it can be walked forward from `start` or backward from `end`.

| Method | What it does | Time |
|---|---|---|
| `add(event, front=False)` | Append to the end, or prepend with `front=True` | O(1) |
| `add_sorted(event, rev=False)` | Insert in chronological (or reverse) order without re-sorting | O(n) |
| `remove(target, front=False)` | Search from the end, or from the start with `front=True`, and unlink the match; raises `ValueError` if absent | O(n) |
| `sort(rev=False)` | **In-place insertion sort** that relinks nodes instead of copying them; returns immediately if already sorted | O(n²) worst case |
| `isSorted(rev)` | Check ascending or descending order | O(n) |
| `len(timeline)` | Number of events, tracked in a counter | O(1) |
| `str(timeline)` | Dates joined with `→` | O(n) |

`event` overloads `<`, `>` and `==` to compare by date, so the list logic never has to read dates directly.

### Design details

- Every operation keeps `start`, `end`, `count` and each node's `next`/`previous` pointers consistent, including the edge cases (empty list, single node, removing the head or tail).
- `add` refuses an event that is already linked elsewhere, which prevents corrupting two lists at once.
- `sort` detaches each node and walks backward to its correct position, so no new nodes or extra lists are created.

## Example

```python
from event import event as Event
from timeline import timeline

t = timeline()
t.add(Event("2019-04-04"))
t.add(Event("1999-12-25"))
t.add(Event("2005-07-13"))

t.sort()                          # 1999-12-25→2005-07-13→2019-04-04
t.add_sorted(Event("2004-02-23")) # slots in between 1999 and 2005
print(t, len(t))
```

Run the built-in demo with:

```bash
python timeline.py
```

## Files

| File | Purpose |
|---|---|
| `event.py` | Node class with date, description, `next`/`previous` pointers and comparison operators |
| `timeline.py` | The doubly linked list and a `main()` demo |

## Author

**Radiah Khan** · [Portfolio](https://radiah23.github.io)
