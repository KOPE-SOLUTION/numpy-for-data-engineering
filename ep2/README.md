# EP2: The Basics of NumPy Arrays

## เป้าหมาย

สิ่งที่จะเข้าใจ:
- โครงสร้างของ NumPy Array (`ndarray`)
- การเข้าถึงข้อมูล (`Indexing / Slicing`)
- View vs Copy (สำคัญมาก)
- การเปลี่ยนรูป (`Reshape`)
- การรวมและแยกข้อมูล (`Concatenate / Split`)

---

## วิธีทดลองใน Ubuntu / Python Shell

สามารถเปิด Python shell แล้วพิมพ์ตามทีละบรรทัดได้ เช่น

```bash
python3
```

หรือจะสร้างไฟล์ชื่อ `ep2_demo.py` แล้ววางโค้ดแต่ละส่วนไปรันก็ได้

---

## 1️ NumPy Array Attributes

```python
import numpy as np
np.random.seed(0)

print("NumPy imported successfully")
```

<details>
<summary>seed คืออะไร</summary>

seed คือการ “ล็อคผลลัพธ์สุ่ม” และถ้ารันใหม่ ก็จะได้ค่าเดิมทุกครั้ง

</details>

<br>

```python
x1 = np.random.randint(10, size=6)
print("x1 =", x1)
```

<details>
<summary>1D Array (x1) — เส้นเดียว</summary>

```text
[ 5 | 0 | 3 | 3 | 7 | 9 ]
   0   1   2   3   4   5   ← index
```

- เป็น “แถวเดียว”

</details>

<br>

```python
x2 = np.random.randint(10, size=(3,4))
print("x2 =")
print(x2)
```

<details>
<summary>2D Array (x2) — ตาราง</summary>

```text
      col →
      0   1   2   3
row  ┌───────────────┐
 0   │ 3 | 5 | 2 | 4 │
 1   │ 7 | 6 | 8 | 8 │
 2   │ 1 | 6 | 7 | 7 │
     └───────────────┘
```

- มี 3 แถว 4 คอลัมน์

</details>

<br>

```python
x3 = np.random.randint(10, size=(3,4,5))
print("x3 =")
print(x3)
```

<details>
<summary>3D Array (x3) — ซ้อนหลายตาราง</summary>

`size=(3,4,5)`

- 3 ชั้น (depth)
- แต่ละชั้นมี 4 แถว
- แต่ละแถวมี 5 คอลัมน์

## ภาพ 3D (แยกเป็น layer)

### Layer 0

```text
Layer 0
┌─────────────────────┐
│ 5 | 0 | 3 | 3 | 7   │
│ 9 | 3 | 5 | 2 | 4   │
│ 7 | 6 | 8 | 8 | 1   │
│ 6 | 7 | 7 | 8 | 1   │
└─────────────────────┘
```

### Layer 1

```text
Layer 1
┌─────────────────────┐
│ 5 | 9 | 8 | 9 | 4   │
│ 3 | 0 | 3 | 5 | 0   │
│ 2 | 3 | 8 | 1 | 3   │
│ 3 | 3 | 7 | 0 | 1   │
└─────────────────────┘
```

### Layer 2

```text
Layer 2
┌─────────────────────┐
│ 9 | 9 | 0 | 4 | 7   │
│ 3 | 2 | 7 | 2 | 0   │
│ 0 | 4 | 5 | 5 | 6   │
│ 8 | 4 | 1 | 4 | 9   │
└─────────────────────┘
```

</details>

### Attribute สำคัญ

```python
print("x3.ndim =", x3.ndim)
print("x3.shape =", x3.shape)
print("x3.size =", x3.size)
print("x3.dtype =", x3.dtype)
print("x3.itemsize =", x3.itemsize, "bytes")
print("x3.nbytes =", x3.nbytes, "bytes")
```

<details>
<summary>อธิบายทีละตัว</summary>

- **ndim (Number of Dimensions)** : จำนวนมิติหรือชั้นของข้อมูล  
  ตัวอย่าง `x3.ndim = 3`

- **shape (รูปร่าง)** : บอกโครงสร้างของข้อมูล  
  ถ้าเป็น 3 มิติจะเป็น `(ชั้น, แถว, คอลัมน์)`  
  ตัวอย่าง `x3.shape = (3, 4, 5)`

- **size (จำนวนข้อมูลทั้งหมด)** : จำนวนตัวเลขทั้งหมดใน array  
  ตัวอย่าง `x3.size = 3 × 4 × 5 = 60`

- **dtype (ชนิดข้อมูล)** : ชนิดข้อมูล เช่น `int`, `float`  
  ตัวอย่าง `x3.dtype = int64`

- **itemsize (ขนาดต่อ 1 ค่า)** : ขนาดของข้อมูล 1 ตัว  
  ตัวอย่าง `x3.itemsize = 8 bytes`

- **nbytes (ขนาดทั้งหมด)** : memory ทั้งหมดที่ใช้  
  ตัวอย่าง `x3.nbytes = 8 × 60 = 480 bytes`

</details>

---

## 2️ Indexing

```python
x1 = np.array([5, 0, 3, 3, 7, 9])

print("x1 =", x1)
print("x1[0] =", x1[0])
print("x1[-1] =", x1[-1])
```

```python
x2 = np.array([
    [3, 5, 2, 4],
    [7, 6, 8, 8],
    [1, 6, 7, 7]
])

print("x2 =")
print(x2)
print("x2[0, 0] =", x2[0, 0])
print("x2[2, -1] =", x2[2, -1])
```

<details>
<summary>อธิบาย</summary>

- `x1[0]` = สมาชิกตัวแรก
- `x1[-1]` = สมาชิกตัวสุดท้าย
- `x2[0, 0]` = แถว 0 คอลัมน์ 0
- `x2[2, -1]` = แถว 2 คอลัมน์สุดท้าย

</details>

---

## 3️ Slicing

```python
x = np.arange(10)

print("x =", x)
print("x[:5] =", x[:5])
print("x[5:] =", x[5:])
print("x[::2] =", x[::2])
print("x[::-1] =", x[::-1])
```

```python
x2 = np.array([
    [12, 5, 2, 4],
    [7, 6, 8, 8],
    [1, 6, 7, 7]
])

print("x2 =")
print(x2)
print("x2[:2, :3] =")
print(x2[:2, :3])
print("x2[:, 0] =", x2[:, 0])
print("x2[0, :] =", x2[0, :])
```

<details>
<summary>อธิบาย</summary>

- `x[:5]` = เอา 5 ตัวแรก
- `x[5:]` = เอาตั้งแต่ตำแหน่ง 5 ถึงจบ
- `x[::2]` = เอาทุก ๆ 2 ตัว
- `x[::-1]` = กลับลำดับ
- `x2[:2, :3]` = 2 แถวแรก และ 3 คอลัมน์แรก
- `x2[:, 0]` = คอลัมน์แรกทั้งหมด
- `x2[0, :]` = แถวแรกทั้งหมด

</details>

---

## 4️ View vs Copy

```python
x2 = np.array([
    [12, 5, 2, 4],
    [7, 6, 8, 8],
    [1, 6, 7, 7]
])

print("x2 ก่อนตัด =")
print(x2)

x2_sub = x2[:2, :2]
print("x2_sub =")
print(x2_sub)

x2_sub[0, 0] = 99

print("x2_sub หลังแก้ค่า =")
print(x2_sub)

print("x2 หลัง x2_sub ถูกแก้ =")
print(x2)
```

<details>
<summary>เกิดอะไรขึ้น ?</summary>

ใน NumPy เวลาเรา slice array  
มันจะไม่ copy ข้อมูล  
แต่มันจะสร้าง view ที่ชี้ไปยัง memory เดิม

เพราะฉะนั้น ถ้าเราแก้ค่าใน subarray  
ค่าใน array หลักจะเปลี่ยนด้วย

แต่ถ้าเราอยากให้แยกจริง  
เราต้องใช้ `.copy()`

</details>

```python
x2 = np.array([
    [12, 5, 2, 4],
    [7, 6, 8, 8],
    [1, 6, 7, 7]
])

x2_copy = x2[:2, :2].copy()
x2_copy[0, 0] = 42

print("x2_copy =")
print(x2_copy)

print("x2 ต้นฉบับ =")
print(x2)
```

---

## 5️ Reshape

```python
grid_3x3 = np.arange(1, 10).reshape((3, 3))
print("grid_3x3 =")
print(grid_3x3)
```

<details>
<summary>Reshape คืออะไร</summary>

reshape คือการเอาข้อมูลเดิมมาเรียงใหม่ให้เป็นรูปแบบที่เราต้องการ  
เช่น เอา array 1 มิติ มาแปลงเป็นตาราง 2 มิติ

</details>

```python
x = np.array([1, 2, 3])

print("x =", x)
print("x.reshape((1,3)) =")
print(x.reshape((1, 3)))   # Row vector

print("x.reshape((3,1)) =")
print(x.reshape((3, 1)))   # Column vector

print("x[np.newaxis, :] =")
print(x[np.newaxis, :])    # Row vector

print("x[:, np.newaxis] =")
print(x[:, np.newaxis])    # Column vector
```

<details>
<summary>ตัวอย่างใช้งานจริง</summary>

```python
x = np.array([1, 2, 3])
y = np.array([10, 20, 30])

result = x[:, np.newaxis] + y

print("result =")
print(result)
```

ผลลัพธ์:

```text
[[11 21 31]
 [12 22 32]
 [13 23 33]]
```

<br>

reshape ใช้เมื่อ
- เปลี่ยนรูปข้อมูล
- เตรียม data เข้า model
- จัด matrix

<br>

newaxis ใช้เมื่อ
- Broadcasting
- บังคับ dimension
- ทำ vector ให้เป็น row/column แบบเร็ว ๆ

</details>

---

## 6️ Concatenate

### เตรียมข้อมูลก่อนใช้งาน

```python
x = np.array([1, 2, 3])

y = np.array([
    [99],
    [99]
])

grid = np.array([
    [9, 8, 7],
    [6, 5, 4]
])

print("x =", x)
print("y =")
print(y)
print("grid =")
print(grid)
```

<br>

```python
print("np.concatenate([x, x]) =")
print(np.concatenate([x, x]))   # รวม 1D

print("np.vstack([x, grid]) =")
print(np.vstack([x, grid]))     # ต่อแนวตั้ง

print("np.hstack([grid, y]) =")
print(np.hstack([grid, y]))     # ต่อแนวนอน
```

<details>
<summary>อธิบาย</summary>

- `np.concatenate([x, x])` = เอา array 1 มิติมาต่อกัน
- `np.vstack([x, grid])` = ต่อแนวตั้ง → จำนวนคอลัมน์ต้องเท่ากัน
- `np.hstack([grid, y])` = ต่อแนวนอน → จำนวนแถวต้องเท่ากัน

</details>

<details>
<summary>⚠️ Error ที่เจอบ่อย</summary>

- ถ้ายังไม่ได้ประกาศตัวแปร เช่น `grid` → จะเกิด `NameError`
- `vstack` → จำนวนคอลัมน์ต้องเท่ากัน
- `hstack` → จำนวนแถวต้องเท่ากัน
- ถ้า shape ไม่ตรง → จะเกิด `ValueError`

</details>

---

## 7️ Split

```python
x = np.array([1, 2, 3, 99, 99, 3, 2, 1])

print("x =", x)

x1, x2, x3 = np.split(x, [3, 5])

print("x1 =", x1)
print("x2 =", x2)
print("x3 =", x3)
```

```python
grid = np.arange(16).reshape((4, 4))
print("grid =")
print(grid)

upper, lower = np.vsplit(grid, [2])
print("upper =")
print(upper)
print("lower =")
print(lower)

left, right = np.hsplit(grid, [2])
print("left =")
print(left)
print("right =")
print(right)
```

<details>
<summary>อธิบาย</summary>

- `np.split(x, [3,5])` = ตัด array 1 มิติที่ index 3 และ 5
- `np.vsplit(grid, [2])` = ตัดแนวนอนที่แถว 2 → ได้ส่วนบนและส่วนล่าง
- `np.hsplit(grid, [2])` = ตัดแนวตั้งที่คอลัมน์ 2 → ได้ส่วนซ้ายและส่วนขวา

</details>

<details>
<summary>⚠️ ข้อควรระวัง</summary>

- index ที่ใช้ตัดต้องไม่เกินขนาด array
- จำนวนจุดตัด + 1 = จำนวนผลลัพธ์
- `vsplit` ใช้กับแนวแถว
- `hsplit` ใช้กับแนวคอลัมน์

</details>

---

## สรุป

- NumPy Array = เร็ว + มีโครงสร้าง
- slicing = view
- copy() = แยก memory
- reshape = เปลี่ยนรูป
- concatenate = รวม
- split = แยก

---

EP3:

> Computation on NumPy Arrays
