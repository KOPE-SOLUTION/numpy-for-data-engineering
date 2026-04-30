# EP5: Fancy Indexing + Sorting Arrays

## เป้าหมายของตอนนี้

ใน EP นี้ เราจะเรียน 2 เรื่องที่ช่วยให้ NumPy ใช้งานกับข้อมูลจริงได้คล่องขึ้นมาก คือ

1. **Fancy Indexing** การเลือกข้อมูลหลายตำแหน่งพร้อมกัน โดยใช้ list หรือ array ของ index

2. **Sorting Arrays** การเรียงข้อมูล การหาอันดับ การเลือก Top-K และการประยุกต์กับงานวิเคราะห์ข้อมูล

เมื่อเรียนจบตอนนี้ คุณควรเข้าใจว่า:
- Fancy Indexing คืออะไร
- ใช้ array ของ index เพื่อเลือกข้อมูลได้อย่างไร
- เลือกข้อมูลจาก 1D และ 2D array ได้อย่างไร
- รวม Fancy Indexing กับ slicing และ masking ได้อย่างไร
- แก้ไขค่าหลายตำแหน่งพร้อมกันได้อย่างไร
- จุดที่ต้องระวังเมื่อ index ซ้ำกัน
- ใช้ `np.sort`, `np.argsort`, `np.partition`, `np.argpartition`
- เรียงข้อมูลตาม row / column
- เลือก Top-K หรือ Bottom-K ได้โดยไม่ต้อง sort ทั้งหมด
- เข้าใจแนวคิดพื้นฐานของ Big-O แบบใช้งานจริง

---

## ภาพรวมของ EP นี้

เนื้อหาจะแบ่งเป็น 2 ส่วนหลัก

### Part A: Fancy Indexing
ใช้สำหรับเลือกข้อมูลหลายตำแหน่งพร้อมกัน

### Part B: Sorting Arrays
ใช้สำหรับเรียงลำดับ หาค่าอันดับ และเลือกข้อมูลสำคัญ

---

# Part A — Fancy Indexing

## 1) ทบทวนวิธีเลือกข้อมูลที่เรียนมาก่อน

ก่อนหน้านี้เราเลือกข้อมูลใน NumPy ได้หลายแบบ เช่น

```python
import numpy as np

x = np.array([10, 20, 30, 40, 50])

print(x[0])      # เลือกตำแหน่งเดียว
print(x[:3])     # slicing
print(x[x > 25]) # boolean mask
```

แต่บางครั้งเราไม่ได้ต้องการเลือกเป็นช่วงต่อเนื่อง และไม่ได้เลือกด้วยเงื่อนไข  
เราอาจต้องการเลือก “หลายตำแหน่งที่เจาะจง” พร้อมกัน

นั่นคือหน้าที่ของ **Fancy Indexing**

---

## 2) Fancy Indexing คืออะไร

Fancy Indexing คือการใช้ list หรือ NumPy array ของ index เพื่อเลือกข้อมูลหลายตำแหน่งพร้อมกัน

```python
rng = np.random.RandomState(42)

x = rng.randint(100, size=10)
print(x)
```

ถ้าต้องการเลือกตำแหน่งที่ 3, 7, 2

```python
ind = [3, 7, 2]
print(x[ind])
```

### อธิบาย

- `ind` คือ list ของตำแหน่งที่ต้องการเลือก
- NumPy จะดึงค่าจากตำแหน่งเหล่านั้นออกมาพร้อมกัน
- ผลลัพธ์จะเป็น NumPy array

---

## 3) Shape ของผลลัพธ์ขึ้นกับ shape ของ index

```python
ind = np.array([
    [3, 7],
    [4, 5]
])

print(x[ind])
```

ถ้า `ind` เป็น 2D ผลลัพธ์ก็จะออกมาเป็น 2D ด้วย

### หลักจำง่าย ๆ

> Fancy Indexing คืนผลลัพธ์ตาม shape ของ index ที่เราใส่เข้าไป  
> ไม่ได้ยึดตาม shape เดิมของ array เสมอไป

---

## 4) Fancy Indexing กับ 2D Array

สร้าง array 2 มิติ

```python
X = np.arange(12).reshape((3, 4))
print(X)
```

ผลลัพธ์:

```text
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
```

เลือกตำแหน่งแบบ row-column pair

```python
row = np.array([0, 1, 2])
col = np.array([2, 1, 3])

print(X[row, col])
```

### อธิบาย

NumPy จะจับคู่ index ตามตำแหน่ง:

```text
X[0, 2]
X[1, 1]
X[2, 3]
```

<br>

ดังนั้นผลลัพธ์คือ:

```text
[ 2  5 11]
```

---

## 5) Fancy Indexing + Broadcasting

Fancy Indexing ยังทำงานร่วมกับ Broadcasting ได้ด้วย

```python
row = np.array([0, 1, 2])
col = np.array([2, 1, 3])

print(X[row[:, np.newaxis], col])
```

### อธิบาย

- `row[:, np.newaxis]` ทำให้ row กลายเป็น column vector
- `col` เป็น vector แนวนอน
- NumPy broadcast index ทั้งสองให้กลายเป็นตาราง
- ผลลัพธ์คือการเลือกหลาย row และหลาย column พร้อมกัน

---

## 6) Combined Indexing

Fancy Indexing สามารถผสมกับ indexing แบบอื่นได้

### 6.1 ผสมกับ simple index

```python
print(X[2, [2, 0, 1]])
```

หมายถึง:
- เลือก row ที่ 2
- แล้วเลือก column 2, 0, 1

---

### 6.2 ผสมกับ slicing

```python
print(X[1:, [2, 0, 1]])
```

หมายถึง:
- เลือก row ตั้งแต่ row 1 เป็นต้นไป
- แล้วเลือก column 2, 0, 1

---

### 6.3 ผสมกับ boolean mask

```python
mask = np.array([True, False, True, False])
row = np.array([0, 1, 2])

print(X[row[:, np.newaxis], mask])
```

หมายถึง:
- เลือกทุก row ตาม `row`
- เลือกเฉพาะ column ที่ mask เป็น `True`

---

## 7) ตัวอย่างจริง: เลือก sample จาก dataset

สมมุติว่าเรามีข้อมูล event log 100 แถว และแต่ละแถวมี 2 features

เช่น:
- feature 1 = latency
- feature 2 = payload size

```python
rng = np.random.RandomState(42)

logs = rng.normal(loc=[150, 500], scale=[30, 120], size=(100, 2))
print(logs.shape)
```

ถ้าต้องการสุ่มเลือก 10 แถวโดยไม่ซ้ำ

```python
indices = rng.choice(logs.shape[0], size=10, replace=False)

sample = logs[indices]

print(indices)
print(sample.shape)
print(sample)
```

### ใช้ทำอะไรได้

แนวคิดนี้ใช้บ่อยในงาน Data เช่น:
- sampling ข้อมูลมาดูเบื้องต้น
- แบ่ง train/test แบบง่าย
- เลือก subset สำหรับ debug
- เลือกข้อมูลบางกลุ่มมาตรวจสอบ

---

## 8) แก้ไขค่าหลายตำแหน่งด้วย Fancy Indexing

Fancy Indexing ไม่ได้ใช้แค่เลือกข้อมูล แต่ใช้แก้ข้อมูลได้ด้วย

```python
x = np.arange(10)
i = np.array([2, 1, 8, 4])

x[i] = 99
print(x)
```

หรือใช้ operator แบบเพิ่ม/ลดค่าได้

```python
x[i] -= 10
print(x)
```

---

## 9) จุดที่ต้องระวัง: index ซ้ำ

ถ้ามี index ซ้ำ ผลลัพธ์อาจไม่เป็นอย่างที่คิด

```python
x = np.zeros(10)
x[[0, 0]] = [4, 6]

print(x)
```

ผลลัพธ์:

```text
[6. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
```

### ทำไมเลข 4 หายไป

เพราะ NumPy assign ตามลำดับ:

1. `x[0] = 4`
2. `x[0] = 6`

ค่าสุดท้ายเลยทับค่าก่อนหน้า

---

## 10) index ซ้ำกับ `+=`

อีกกรณีที่ชวนงง

```python
x = np.zeros(10)
i = [2, 3, 3, 4, 4, 4]

x[i] += 1
print(x)
```

หลายคนคาดหวังว่า:

- index 3 จะได้ 2
- index 4 จะได้ 3

แต่จริง ๆ อาจได้ไม่ตรงตามคาด เพราะ `x[i] += 1` ทำงานคล้ายกับ

```python
x[i] = x[i] + 1
```

คือคำนวณด้านขวาก่อน แล้วค่อย assign กลับ

---

## 11) แก้ปัญหา index ซ้ำด้วย `np.add.at`

ถ้าต้องการให้ index ซ้ำถูกนับซ้ำจริง ๆ ให้ใช้ `np.add.at`

```python
x = np.zeros(10)
i = [2, 3, 3, 4, 4, 4]

np.add.at(x, i, 1)

print(x)
```

ผลลัพธ์:

```text
[0. 0. 1. 2. 3. 0. 0. 0. 0. 0.]
```

### อธิบาย

`np.add.at(x, i, 1)` หมายถึง:

- ไปที่ตำแหน่งใน `i`
- บวกค่า 1
- ถ้า index ซ้ำ ให้บวกซ้ำจริง

---

## 12) ตัวอย่างจริง: ทำ binning แบบง่าย

สมมุติเรามีข้อมูล latency และต้องการนับว่าแต่ละค่าอยู่ในช่วงไหน

```python
rng = np.random.RandomState(42)

latency = rng.normal(loc=150, scale=40, size=100)

bins = np.array([0, 100, 150, 200, 300])
counts = np.zeros(len(bins), dtype=int)

bin_index = np.searchsorted(bins, latency)

np.add.at(counts, bin_index, 1)

print("bins:", bins)
print("counts:", counts)
```

### แนวคิด

- `np.searchsorted` หาว่าค่าแต่ละตัวควรอยู่ตำแหน่งไหนใน bins
- `np.add.at` ใช้นับจำนวนแบบรองรับ index ซ้ำ
- นี่คือพื้นฐานของ histogram

ในงานจริงสามารถใช้ `np.histogram()` ได้เลย

```python
hist, edges = np.histogram(latency, bins=bins)
print(hist)
print(edges)
```

---

# Part B — Sorting Arrays

## 13) ทำไมต้อง Sorting

Sorting คือการเรียงข้อมูล เช่น:

- เรียง latency จากน้อยไปมาก
- หา request ที่ช้าที่สุด
- หา top users
- หา top error count
- เลือก k ค่าที่น้อยที่สุดหรือมากที่สุด
- เตรียมข้อมูลก่อน ranking

---

## 14) ไม่ควรเขียน sorting เองถ้าไม่จำเป็น

เราสามารถเขียน selection sort เองได้ แต่ไม่เหมาะกับงานจริง

```python
def selection_sort(x):
    x = x.copy()
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        x[i], x[swap] = x[swap], x[i]
    return x

x = np.array([2, 1, 4, 3, 5])
print(selection_sort(x))
```

### ประเด็น

- เขียนเพื่อเรียนรู้ algorithm ได้
- แต่ไม่ควรใช้กับข้อมูลใหญ่
- ใช้ `np.sort()` จะเหมาะกว่า

---

## 15) ใช้ `np.sort`

```python
x = np.array([2, 1, 4, 3, 5])

print(np.sort(x))
print(x)
```

`np.sort(x)` จะคืน array ใหม่ที่เรียงแล้ว แต่ `x` เดิมยังไม่เปลี่ยน

ถ้าต้องการ sort แบบแก้ตัวแปรเดิม:

```python
x.sort()
print(x)
```

---

## 16) ใช้ `np.argsort`

`np.argsort()` ไม่ได้คืนค่าที่เรียงแล้ว  
แต่คืน index ที่ทำให้ array เรียงได้

```python
x = np.array([2, 1, 4, 3, 5])

idx = np.argsort(x)

print(idx)
print(x[idx])
```

### ใช้ทำอะไร

`argsort` สำคัญมากในงาน ranking เช่น:

- เรียงคะแนนแต่ยังอยากรู้ id เดิม
- เรียง latency แต่ยังอยากรู้ request id
- เรียง distance เพื่อหา nearest neighbor

---

## 17) Sorting 2D Array ตาม axis

```python
rng = np.random.RandomState(42)
X = rng.randint(0, 10, (4, 6))

print(X)
```

เรียงแต่ละ column:

```python
print(np.sort(X, axis=0))
```

เรียงแต่ละ row:

```python
print(np.sort(X, axis=1))
```

### ระวัง

เมื่อ sort ตาม row หรือ column ความสัมพันธ์ของข้อมูลเดิมใน row/column อาจหายไป

> Sorting แบบนี้เหมาะกับการดู distribution ภายในแต่ละแกน  
> แต่ถ้าข้อมูลแต่ละ row คือ record เดียวกัน ต้องระวัง เพราะการ sort อาจทำให้ feature ใน record เดิมไม่สัมพันธ์กันแล้ว

---

## 18) Partial Sort ด้วย `np.partition`

บางครั้งเราไม่ต้องเรียงทั้งหมด แค่ต้องการ k ค่าที่น้อยที่สุด

```python
x = np.array([7, 2, 3, 1, 6, 5, 4])

print(np.partition(x, 3))
```

ผลลัพธ์ไม่ได้เรียงทั้ง array  
แต่รับประกันว่า 3 ค่าที่เล็กที่สุดจะอยู่ด้านซ้าย

---

## 19) `np.argpartition`

ถ้าต้องการ index ของกลุ่ม top/bottom ให้ใช้ `np.argpartition`

```python
x = np.array([7, 2, 3, 1, 6, 5, 4])

idx = np.argpartition(x, 3)

print(idx)
print(x[idx[:3]])
```

### ใช้ทำอะไร

เหมาะมากกับ:

- หา 5 ค่า latency ต่ำสุด
- หา 10 คะแนนสูงสุด
- หา k nearest neighbors
- เลือกข้อมูลที่น่าสนใจโดยไม่ sort ทั้งหมด

---

## 20) ตัวอย่างจริง: หา Top-K Latency

สมมุติมี latency ของ request หลายตัว

```python
latency = np.array([120, 95, 300, 250, 180, 500, 130, 220, 410, 160])
```

### หา 3 request ที่ช้าที่สุดด้วย `argsort`

```python
idx = np.argsort(latency)

slowest_idx = idx[-3:][::-1]
print("indices:", slowest_idx)
print("values:", latency[slowest_idx])
```

### ใช้ `argpartition` เพื่อเลือก Top-K แบบเร็วกว่าในข้อมูลใหญ่

```python
k = 3
idx = np.argpartition(latency, -k)[-k:]

print("top-k indices:", idx)
print("top-k values:", latency[idx])
```

ถ้าต้องการเรียง top-k อีกที:

```python
idx_sorted = idx[np.argsort(latency[idx])[::-1]]

print("sorted top-k indices:", idx_sorted)
print("sorted top-k values:", latency[idx_sorted])
```

---

## 21) ตัวอย่างจริง: Ranking คะแนนโมเดลหรือระบบ

```python
scores = np.array([0.82, 0.91, 0.75, 0.88, 0.95, 0.67])
model_names = np.array(["A", "B", "C", "D", "E", "F"])

rank_idx = np.argsort(scores)[::-1]

print(model_names[rank_idx])
print(scores[rank_idx])
```

### อธิบาย

- `np.argsort(scores)` เรียงจากน้อยไปมาก
- `[::-1]` กลับเป็นมากไปน้อย
- ใช้ index ไปดึงชื่อ model ตามอันดับ

นี่คือ pattern ที่ใช้บ่อยมากในงาน Data

---

## 22) Mini Project: k-Nearest Neighbors แบบ NumPy ล้วน

ในตัวอย่างนี้ เราจะใช้ NumPy หาเพื่อนบ้านที่ใกล้ที่สุดของแต่ละจุด

### สร้างข้อมูล 2D points

```python
rng = np.random.RandomState(42)
points = rng.rand(10, 2)

print(points)
```

### คำนวณระยะห่างทุกคู่ด้วย Broadcasting

```python
diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]

print(diff.shape)
```

`diff.shape` จะเป็น:

```text
(10, 10, 2)
```

หมายถึง:

- จุดต้นทาง 10 จุด
- จุดปลายทาง 10 จุด
- แต่ละคู่มี 2 มิติ คือ x และ y

### ยกกำลังสองและรวมแกนสุดท้าย

```python
dist_sq = np.sum(diff ** 2, axis=-1)

print(dist_sq.shape)
print(dist_sq)
```

### ตรวจสอบ diagonal

```python
print(np.diag(dist_sq))
```

ค่าบน diagonal ควรเป็น 0 เพราะเป็นระยะจากจุดเดียวกันไปยังตัวเอง

<details>
<summary>💡 ถ้ายัง งงๆ ก็ ลองลดเหลือ 3 กับข้อมูลง่ายๆ กันดู แล้วย้อนกลับไปลองทำด้านบนใหม่</summary>

```py
import numpy as np

points = np.array([
    [1, 1],  # P0
    [3, 2],  # P1
    [2, 5],  # P2
])

diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]

print(diff)
print(diff.shape)
```

<br>

`diff[i, j] = points[i] - points[j]`

```sh
          j=0        j=1        j=2
          P0          P1        P2
i=0 P0   P0-P0      P0-P1      P0-P2
         [0,0]      [-2,-1]    [-1,-4]

i=1 P1   P1-P0      P1-P1      P1-P2
         [2,1]      [0,0]      [1,-3]

i=2 P2   P2-P0      P2-P1      P2-P2
         [1,4]      [-1,3]     [0,0]
```

<br>

ผลลัพธ์จริงจะเป็น

```sh
[
 [[ 0,  0], [-2, -1], [-1, -4]],
 [[ 2,  1], [ 0,  0], [ 1, -3]],
 [[ 1,  4], [-1,  3], [ 0,  0]]
]
```

<br>

ต่อเป็นระยะทาง

```py
dist_sq = np.sum(diff ** 2, axis=-1)
print(dist_sq)
```

<br>

ได้

```sh
[
 [ 0,  5, 17],
 [ 5,  0, 10],
 [17, 10,  0]
]

# เช่น P0 → P1
# P0 - P1 = [1-3, 1-2] = [-2, -1]
# distance² = (-2)² + (-1)² = 5
```

<br>

สรุป

```sh
diff.shape = (3,3,2)
= 3 จุดต้นทาง × 3 จุดปลายทาง × [dx, dy]
```

</details>

---

## 23) ใช้ `argsort` หา nearest neighbors

```python
nearest = np.argsort(dist_sq, axis=1)

print(nearest)
```

### อธิบาย

ในแต่ละ row:

- index แรกมักเป็นตัวเอง
- index ถัดไปคือเพื่อนบ้านที่ใกล้ที่สุด
- index ถัดไปอีกคือเพื่อนบ้านลำดับถัดไป

### หา 2 เพื่อนบ้านที่ใกล้ที่สุด โดยไม่เอาตัวเอง

```python
k = 2

nearest_2 = nearest[:, 1:k+1]

print(nearest_2)
```

---

## 24) ใช้ `argpartition` หา nearest neighbors แบบไม่ sort ทั้งหมด

```python
k = 2

nearest_partition = np.argpartition(dist_sq, k + 1, axis=1)

nearest_2_fast = nearest_partition[:, 1:k+1]

print(nearest_2_fast)
```

### อธิบาย

- `argsort` เรียงทั้งหมด
- `argpartition` สนใจแค่กลุ่มที่เล็กที่สุด k ตัว
- ถ้าข้อมูลใหญ่ `argpartition` มักเหมาะกว่า

---

## 25) Visualize kNN แบบง่าย

ถ้าต้องการ plot จุดและเส้นเชื่อม nearest neighbors:

```python
import matplotlib.pyplot as plt

plt.scatter(points[:, 0], points[:, 1], s=80)

for i in range(points.shape[0]):
    for j in nearest_2[i]:
        xs = [points[i, 0], points[j, 0]]
        ys = [points[i, 1], points[j, 1]]
        plt.plot(xs, ys)

plt.title("Simple k-Nearest Neighbors with NumPy")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
```

### หมายเหตุ

ตัวอย่างนี้เป็น brute-force kNN  
คือคำนวณระยะทุกคู่ ซึ่งเข้าใจง่าย แต่ถ้าข้อมูลใหญ่มาก อาจต้องใช้วิธีที่ optimize กว่า เช่น KD-Tree ใน Scikit-learn

---

# Aside: Big-O แบบเข้าใจง่าย

## 26) Big-O คืออะไร

Big-O คือวิธีอธิบายว่า algorithm ใช้เวลาหรือจำนวนขั้นตอนเพิ่มขึ้นอย่างไร เมื่อข้อมูลมีขนาดใหญ่ขึ้น

| Big-O | ความหมายแบบง่าย |
|---|---|
| `O(1)` | เวลาแทบคงที่ |
| `O(N)` | ข้อมูลเพิ่ม 10 เท่า เวลาก็เพิ่มประมาณ 10 เท่า |
| `O(N log N)` | มักเจอใน sorting ที่ดี |
| `O(N^2)` | ข้อมูลเพิ่ม 10 เท่า เวลาอาจเพิ่มประมาณ 100 เท่า |
| `O(N!)` | โตเร็วมาก ไม่เหมาะกับงานจริง |

---

## 27) ทำไมต้องสนใจ Big-O

ในงาน Data เราอาจเริ่มจากข้อมูลหลักร้อย  
แต่พอระบบจริง ข้อมูลอาจกลายเป็นหลักล้านหรือมากกว่านั้น

algorithm ที่ดูเร็วตอนข้อมูลเล็ก อาจช้ามากเมื่อข้อมูลโต

### ตัวอย่าง

- sort ทั้งหมด อาจเกินจำเป็น ถ้าต้องการแค่ Top-K
- loop ซ้อน loop อาจช้ามากเมื่อข้อมูลเยอะ
- vectorized NumPy มักช่วยให้โค้ดเร็วขึ้น
- แต่บางปัญหาใหญ่มาก ต้องใช้อัลกอริทึมเฉพาะทางเพิ่ม

---

# Cheat Sheet

## Fancy Indexing

| Pattern | ความหมาย |
|---|---|
| `x[[1, 3, 5]]` | เลือกหลายตำแหน่งจาก 1D |
| `X[row, col]` | เลือกตำแหน่งแบบ row-column pair |
| `X[row[:, np.newaxis], col]` | เลือกแบบ broadcasted index |
| `X[1:, [2, 0, 1]]` | ผสม slicing กับ fancy indexing |
| `X[:, mask]` | ผสม slicing กับ boolean mask |
| `x[i] = value` | แก้ค่าหลายตำแหน่ง |
| `np.add.at(x, i, 1)` | บวกซ้ำตาม index ที่ซ้ำจริง |

## Sorting

| Function | ความหมาย |
|---|---|
| `np.sort(x)` | คืน array ที่เรียงแล้ว |
| `x.sort()` | sort แบบแก้ array เดิม |
| `np.argsort(x)` | คืน index สำหรับเรียง |
| `np.partition(x, k)` | แบ่งให้ k ค่าน้อยสุดอยู่ด้านซ้าย |
| `np.argpartition(x, k)` | คืน index ของ partition |
| `np.sort(X, axis=0)` | sort ตาม column |
| `np.sort(X, axis=1)` | sort ตาม row |

---

# สรุปท้าย EP

## สิ่งที่ต้องจำ

1. Fancy Indexing ใช้เลือกหลายตำแหน่งพร้อมกัน
2. Shape ของผลลัพธ์ขึ้นกับ shape ของ index
3. Fancy Indexing ใช้กับ 2D array ได้โดยจับคู่ row และ column
4. สามารถผสม Fancy Indexing กับ slicing และ masking ได้
5. ถ้า index ซ้ำและต้องการสะสมค่าจริง ให้ใช้ `np.add.at`
6. `np.sort` ใช้เรียงข้อมูล
7. `np.argsort` ใช้หา index ของลำดับ
8. `np.partition` และ `np.argpartition` เหมาะกับ Top-K / Bottom-K
9. Big-O ช่วยให้เราเข้าใจว่า algorithm จะช้าลงแค่ไหนเมื่อข้อมูลโต
10. ตัวอย่าง kNN แสดงให้เห็นการรวม Broadcasting + Aggregation + Sorting เข้าด้วยกัน

---

## 🔥 EP ถัดไป

> EP6: Structured Data + Mini Project

---

## โค้ดทดลองรวมท้ายตอน

```python
import numpy as np

# -----------------------------
# Fancy Indexing 1D
# -----------------------------
rng = np.random.RandomState(42)

x = rng.randint(100, size=10)
print("x =", x)

ind = [3, 7, 2]
print("selected =", x[ind])

ind_2d = np.array([[3, 7], [4, 5]])
print("selected 2d =")
print(x[ind_2d])

# -----------------------------
# Fancy Indexing 2D
# -----------------------------
X = np.arange(12).reshape((3, 4))
print("X =")
print(X)

row = np.array([0, 1, 2])
col = np.array([2, 1, 3])

print("X[row, col] =", X[row, col])
print("broadcasted indexing =")
print(X[row[:, np.newaxis], col])

# -----------------------------
# Combined Indexing
# -----------------------------
print("row 2 with selected cols =", X[2, [2, 0, 1]])
print("slice + fancy =", X[1:, [2, 0, 1]])

mask = np.array([True, False, True, False])
print("mask columns =")
print(X[:, mask])

# -----------------------------
# Modify with Fancy Indexing
# -----------------------------
x = np.arange(10)
i = np.array([2, 1, 8, 4])

x[i] = 99
print("modified x =", x)

x = np.zeros(10)
i = [2, 3, 3, 4, 4, 4]
np.add.at(x, i, 1)
print("add.at result =", x)

# -----------------------------
# Sorting
# -----------------------------
x = np.array([2, 1, 4, 3, 5])
print("sort =", np.sort(x))

idx = np.argsort(x)
print("argsort =", idx)
print("x sorted by idx =", x[idx])

# -----------------------------
# Top-K latency
# -----------------------------
latency = np.array([120, 95, 300, 250, 180, 500, 130, 220, 410, 160])

k = 3
idx = np.argpartition(latency, -k)[-k:]
idx_sorted = idx[np.argsort(latency[idx])[::-1]]

print("top-k indices =", idx_sorted)
print("top-k values =", latency[idx_sorted])

# -----------------------------
# Simple kNN
# -----------------------------
points = rng.rand(10, 2)

diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]
dist_sq = np.sum(diff ** 2, axis=-1)

nearest = np.argsort(dist_sq, axis=1)
nearest_2 = nearest[:, 1:3]

print("nearest 2 neighbors =")
print(nearest_2)
```

