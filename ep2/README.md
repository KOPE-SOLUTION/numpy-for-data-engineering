# EP2: The Basics of NumPy Arrays

## 0) Setup
```bash
python3
```

```python
import numpy as np
np.random.seed(0)
print("NumPy version:", np.__version__)
```

---

## 1) NumPy Array Attributes

```python
x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(3,4))
x3 = np.random.randint(10, size=(3,4,5))

print("x1:", x1)
print("x2:\n", x2)
print("x3 shape:", x3.shape)
```

### Attributes
```python
print("ndim:", x3.ndim)
print("shape:", x3.shape)
print("size:", x3.size)
print("dtype:", x3.dtype)
print("itemsize:", x3.itemsize, "bytes")
print("nbytes:", x3.nbytes, "bytes")
```

---

## 2) Indexing

```python
x1 = np.array([5,0,3,3,7,9])
print("x1:", x1)
print("x1[0]:", x1[0])
print("x1[-1]:", x1[-1])

print("x2:\n", x2)
print("x2[0,0]:", x2[0,0])
print("x2[2,-1]:", x2[2,-1])
```

---

## 3) Slicing

```python
x = np.arange(10)
print("x:", x)

print("x[:5]  =", x[:5])
print("x[5:]  =", x[5:])
print("x[::2] =", x[::2])
print("x[::-1]=", x[::-1])

print("x2[:2, :3] =\n", x2[:2, :3])
print("x2[:, 0]   =", x2[:, 0])
print("x2[0, :]   =", x2[0, :])
```

---

## 4) View vs Copy

```python
x2_sub = x2[:2, :2]
print("x2_sub (view):\n", x2_sub)

x2_sub[0,0] = 99
print("after change x2_sub:")
print("x2_sub:\n", x2_sub)
print("x2 (changed too!):\n", x2)

x2_copy = x2[:2, :2].copy()
x2_copy[0,0] = 42
print("x2_copy (independent):\n", x2_copy)
print("x2 (no change now):\n", x2)
```

---

## 5) Reshape

```python
a = np.arange(1,10)
print("a:", a)

grid3 = a.reshape((3,3))
print("reshape 3x3:\n", grid3)

x = np.array([1,2,3])
print("x:", x)

print("row vector:", x.reshape((1,3)))
print("column vector:\n", x.reshape((3,1)))

print("newaxis row:", x[np.newaxis, :])
print("newaxis col:\n", x[:, np.newaxis])
```

### Broadcasting demo
```python
x = np.array([1,2,3])
y = np.array([10,20,30])

res = x[:, np.newaxis] + y
print("broadcast result:\n", res)
```

---

## 6) Concatenate

```python
x = np.array([1,2,3])
y = np.array([[99],[99]])
grid = np.array([[9,8,7],[6,5,4]])

print("concat 1D:", np.concatenate([x, x]))
print("vstack:\n", np.vstack([x, grid]))
print("hstack:\n", np.hstack([grid, y]))
```

---

## 7) Split

```python
x = np.array([1,2,3,99,99,3,2,1])
print("split:", np.split(x,[3,5]))

grid = np.arange(16).reshape((4,4))
print("grid:\n", grid)

upper, lower = np.vsplit(grid,[2])
print("vsplit upper:\n", upper)
print("vsplit lower:\n", lower)

left, right = np.hsplit(grid,[2])
print("hsplit left:\n", left)
print("hsplit right:\n", right)
```

---

## สรุป
- slicing = view
- copy() = แยก memory
- reshape = เปลี่ยนรูป
- concatenate = รวม
- split = แยก

---

EP ถัดไป:

> EP3: Computation on NumPy Arrays
