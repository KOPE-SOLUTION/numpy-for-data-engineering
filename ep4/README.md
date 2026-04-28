# EP4: Broadcasting + Comparisons, Masks, and Boolean Logic

## เป้าหมายของตอนนี้

ใน EP นี้ เราจะเรียน 2 เรื่องสำคัญมากของ NumPy คือ

1. **Broadcasting**   การคำนวณระหว่าง array ที่มีขนาดหรือ shape ต่างกัน โดย NumPy ช่วย "ขยายแนวคิด" ให้เข้ากันโดยไม่ต้อง copy ข้อมูลจริง

2. **Comparisons, Masks, and Boolean Logic**  การเปรียบเทียบข้อมูล การสร้างเงื่อนไข และการคัดกรองข้อมูลด้วย Boolean Mask

<br>

เมื่อเรียนจบตอนนี้ คุณควรเข้าใจว่า:
- Broadcasting คืออะไร
- ทำไม array คนละ shape ถึงบวก ลบ คูณ หารกันได้
- กฎ 3 ข้อของ Broadcasting
- `np.newaxis` ใช้ทำอะไร
- Comparison operators ทำงานแบบ element-wise อย่างไร
- Boolean mask คืออะไร
- ใช้ mask เพื่อ filter ข้อมูลยังไง
- ใช้ `&`, `|`, `~` แทน `and`, `or`, `not` ใน NumPy อย่างไร
- ใช้ `np.any`, `np.all`, `np.sum`, `np.count_nonzero` กับ Boolean array ได้อย่างไร

---

## ภาพรวมของ EP นี้

เนื้อหาจะแบ่งเป็น 2 ส่วนใหญ่:

### Part A: Broadcasting
ใช้สำหรับคำนวณ array ที่มี shape ต่างกัน

### Part B: Comparisons, Masks, and Boolean Logic
ใช้สำหรับสร้างเงื่อนไข คัดกรอง และสรุปข้อมูลจาก array

---

# Part A — Computation on Arrays: Broadcasting

## 1) Broadcasting คืออะไร

จาก EP3 เราเรียนเรื่อง `ufunc` และ `vectorization` ไปแล้ว  
Broadcasting คืออีกหนึ่งเครื่องมือที่ช่วยให้เราเขียนโค้ดแบบ vectorized ได้มากขึ้น

### นิยามแบบเข้าใจง่าย

> Broadcasting คือกฎที่ NumPy ใช้เพื่อคำนวณ array ที่มี shape ต่างกัน  
> โดยไม่ต้องเขียน loop เอง และไม่ต้อง duplicate ข้อมูลจริงใน memory

---

## 2) ตัวอย่างพื้นฐาน: array ขนาดเท่ากัน

ถ้า array มีขนาดเท่ากัน NumPy จะคำนวณแบบ element-wise

```python
import numpy as np

a = np.array([0, 1, 2])
b = np.array([5, 5, 5])

print(a + b)
```

ผลลัพธ์:

```text
[5 6 7]
```

### อธิบาย
- `0 + 5`
- `1 + 5`
- `2 + 5`

นี่คือการคำนวณทีละตำแหน่ง หรือ element-wise operation

---

## 3) Broadcasting กับ Scalar

เราสามารถบวก scalar กับ array ได้เลย

```python
a = np.array([0, 1, 2])

print(a + 5)
```

ผลลัพธ์:

```text
[5 6 7]
```

### แนวคิด
ให้จินตนาการว่า NumPy มองเลข `5` เหมือนถูกขยายเป็น

```python
[5, 5, 5]
```

แล้วค่อยนำมาบวกกับ `a`

### แต่สิ่งสำคัญคือ
NumPy ไม่ได้ copy ค่า 5 จริง ๆ เต็ม array  
มันใช้ broadcasting rule เพื่อคำนวณอย่างมีประสิทธิภาพ

---

## 4) Broadcasting กับ 2D Array

```python
M = np.ones((3, 3))
a = np.array([0, 1, 2])

print(M)
print(M + a)
```

ผลลัพธ์:

```text
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]

[[1. 2. 3.]
 [1. 2. 3.]
 [1. 2. 3.]]
```

### อธิบาย
`a` มี shape เป็น `(3,)`  
`M` มี shape เป็น `(3, 3)`

NumPy จะ broadcast `a` ให้เข้ากับแต่ละ row ของ `M`

---

## 5) Broadcasting ที่ขยายทั้งสองฝั่ง

```python
a = np.arange(3)
b = np.arange(3)[:, np.newaxis]

print(a)
print(b)
print(a + b)
```

ผลลัพธ์:

```text
[0 1 2]

[[0]
 [1]
 [2]]

[[0 1 2]
 [1 2 3]
 [2 3 4]]
```

### อธิบาย
- `a` มี shape `(3,)`
- `b` มี shape `(3, 1)`
- เมื่อนำมาบวกกัน NumPy broadcast ให้กลายเป็น shape `(3, 3)`

---

## 6) กฎ 3 ข้อของ Broadcasting

Broadcasting มีกฎหลัก 3 ข้อ

### Rule 1
ถ้า array มีจำนวนมิติไม่เท่ากัน  
NumPy จะเติมเลข `1` ทางด้านซ้ายของ shape ที่มีมิติน้อยกว่า

ตัวอย่าง:

```text
M.shape = (2, 3)
a.shape = (3,)
```

จะมองเป็น:

```text
M.shape -> (2, 3)
a.shape -> (1, 3)
```

### Rule 2
ถ้ามิติใดไม่เท่ากัน แต่มีฝั่งหนึ่งเป็น `1`  
NumPy จะขยายมิตินั้นให้เท่ากับอีกฝั่ง

```text
M.shape -> (2, 3)
a.shape -> (1, 3)
```

จะกลายเป็น:

```text
M.shape -> (2, 3)
a.shape -> (2, 3)
```

### Rule 3
ถ้ามิติใดไม่เท่ากัน และไม่มีฝั่งไหนเป็น `1`  
NumPy จะ error

ตัวอย่าง:

```text
(3, 2) กับ (3,)
```

หลังเติมด้านซ้าย:

```text
(3, 2)
(1, 3)
```

จะกลายเป็น:

```text
(3, 2)
(3, 3)
```

เข้ากันไม่ได้ จึงเกิด error

---

## 7) Broadcasting Example 1

```python
M = np.ones((2, 3))
a = np.arange(3)

print("M shape:", M.shape)
print("a shape:", a.shape)

print(M + a)
```

### วิเคราะห์ shape

```text
M.shape = (2, 3)
a.shape = (3,)
```

เติม `1` ด้านซ้ายให้ `a`

```text
M.shape -> (2, 3)
a.shape -> (1, 3)
```

ขยายมิติแรกของ `a`

```text
M.shape -> (2, 3)
a.shape -> (2, 3)
```

ดังนั้นบวกกันได้

---

## 8) Broadcasting Example 2

กรณีนี้ทั้งสอง array ต้องถูก broadcast

```python
a = np.arange(3).reshape((3, 1))
b = np.arange(3)

print("a shape:", a.shape)
print("b shape:", b.shape)

print(a + b)
```

### วิเคราะห์ shape

```text
a.shape = (3, 1)
b.shape = (3,)
```

เติม `1` ด้านซ้ายให้ `b`

```text
a.shape -> (3, 1)
b.shape -> (1, 3)
```

ขยายทั้งสองฝั่ง

```text
a.shape -> (3, 3)
b.shape -> (3, 3)
```

ดังนั้นบวกกันได้

---

## 9) Broadcasting Example 3: กรณี Error

```python
M = np.ones((3, 2))
a = np.arange(3)

print("M shape:", M.shape)
print("a shape:", a.shape)

# print(M + a)  # จะ error
```

ถ้าเปิดบรรทัดนี้:

```python
print(M + a)
```

จะได้ error ประมาณนี้:

```text
ValueError: operands could not be broadcast together with shapes (3,2) (3,)
```

### ทำไม error

```text
M.shape = (3, 2)
a.shape = (3,)
```

เติม `1` ด้านซ้ายให้ `a`

```text
M.shape -> (3, 2)
a.shape -> (1, 3)
```

ขยายมิติแรกของ `a`

```text
M.shape -> (3, 2)
a.shape -> (3, 3)
```

สุดท้าย shape ไม่ตรงกัน จึงบวกไม่ได้

---

## 10) แก้ด้วย `np.newaxis`

ถ้าอยากให้ `a` กลายเป็น column vector ให้ใช้ `np.newaxis`

```python
M = np.ones((3, 2))
a = np.arange(3)

print(a[:, np.newaxis].shape)
print(M + a[:, np.newaxis])
```

ผลลัพธ์:

```text
(3, 1)

[[1. 1.]
 [2. 2.]
 [3. 3.]]
```

### อธิบาย
เดิม `a` คือ shape `(3,)`  
เมื่อใช้ `a[:, np.newaxis]` จะกลายเป็น `(3, 1)`  
จึง broadcast กับ `(3, 2)` ได้

---

## 11) Broadcasting ใช้กับ ufunc อื่นได้ด้วย

ไม่ได้ใช้แค่ `+` เท่านั้น  
ใช้ได้กับ binary ufunc เกือบทั้งหมด เช่น `-`, `*`, `/`, `np.maximum`, `np.logaddexp`

```python
M = np.ones((3, 2))
a = np.arange(3)

print(np.logaddexp(M, a[:, np.newaxis]))
```

### สรุป
Broadcasting เป็นกฎกลางของ NumPy  
ไม่ใช่แค่ของการบวก

---

# Broadcasting in Practice

## 12) ตัวอย่างจริง: Centering Data

สมมุติว่าเรามีข้อมูล 10 observations และแต่ละ observation มี 3 features

```python
X = np.random.random((10, 3))

print(X)
```

หา mean ของแต่ละ feature

```python
Xmean = X.mean(axis=0)
print(Xmean)
```

นำข้อมูลแต่ละแถวลบด้วย mean

```python
X_centered = X - Xmean
print(X_centered)
```

ตรวจสอบว่า mean หลัง center ใกล้ 0 หรือไม่

```python
print(X_centered.mean(axis=0))
```

### อธิบาย
- `X` shape = `(10, 3)`
- `Xmean` shape = `(3,)`
- NumPy broadcast `Xmean` ไปทุก row
- ผลคือแต่ละ feature ถูกลบด้วยค่าเฉลี่ยของตัวเอง

### ใช้ทำอะไร
แนวคิดนี้ใช้บ่อยมากใน:
- Data preprocessing
- Machine Learning
- Feature scaling
- Statistical analysis

---

## 13) ตัวอย่างจริง: คำนวณฟังก์ชัน 2D

Broadcasting ใช้สร้าง grid calculation ได้ดีมาก

```python
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]

z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

print(z.shape)
```

ถ้าจะ plot:

```python
import matplotlib.pyplot as plt

plt.imshow(z, origin="lower", extent=[0, 5, 0, 5])
plt.colorbar()
plt.show()
```

### อธิบาย
- `x` เป็นแกนแนวนอน
- `y` เป็นแกนแนวตั้ง
- broadcasting ทำให้คำนวณค่า `z` ทุกจุดใน grid ได้โดยไม่ต้องเขียน loop ซ้อน

---

# Part B — Comparisons, Masks, and Boolean Logic

## 14) ทำไมต้องใช้ Boolean Mask

ในงาน Data จริง เรามักไม่ได้ต้องการดูข้อมูลทั้งหมด  
แต่ต้องการเลือกเฉพาะข้อมูลที่ตรงเงื่อนไข เช่น:

- ค่าเกิน threshold
- ค่าต่ำกว่ามาตรฐาน
- ข้อมูลที่ไม่ใช่ missing value
- ข้อมูลเฉพาะช่วงเวลา
- ข้อมูลที่ผ่านหลายเงื่อนไขพร้อมกัน

Boolean Mask คือวิธีที่ NumPy ใช้คัดกรองข้อมูลเหล่านี้อย่างรวดเร็ว

---

## 15) Comparison Operators เป็น ufunc

เหมือนกับ arithmetic operators ใน EP3  
comparison operators ก็ทำงานแบบ element-wise เช่นกัน

```python
x = np.array([1, 2, 3, 4, 5])

print(x < 3)
print(x > 3)
print(x <= 3)
print(x >= 3)
print(x != 3)
print(x == 3)
```

ผลลัพธ์จะเป็น Boolean array

```text
[ True  True False False False]
[False False False  True  True]
...
```

### ตารางเปรียบเทียบ

| Operator | UFunc | ความหมาย |
|---|---|---|
| `==` | `np.equal` | เท่ากับ |
| `!=` | `np.not_equal` | ไม่เท่ากับ |
| `<` | `np.less` | น้อยกว่า |
| `<=` | `np.less_equal` | น้อยกว่าหรือเท่ากับ |
| `>` | `np.greater` | มากกว่า |
| `>=` | `np.greater_equal` | มากกว่าหรือเท่ากับ |

---

## 16) เปรียบเทียบ array กับ expression

```python
x = np.array([1, 2, 3, 4, 5])

print((2 * x) == (x ** 2))
```

### อธิบาย
NumPy จะคำนวณทีละ element แล้วตอบกลับเป็น Boolean array

---

## 17) Comparison กับ 2D Array

```python
rng = np.random.RandomState(0)
x = rng.randint(10, size=(3, 4))

print(x)
print(x < 6)
```

ผลลัพธ์เป็น Boolean array ขนาดเดียวกับ `x`

---

# Working with Boolean Arrays

## 18) นับจำนวนค่าที่เข้าเงื่อนไข

```python
print(np.count_nonzero(x < 6))
```

หรือใช้ `np.sum()` ได้ เพราะ

- `True` ถูกมองเป็น `1`
- `False` ถูกมองเป็น `0`

```python
print(np.sum(x < 6))
```

### นับตาม row

```python
print(np.sum(x < 6, axis=1))
```

### อธิบาย
ถ้า `x` เป็น 2D array  
`axis=1` หมายถึงนับตามแต่ละ row

---

## 19) ใช้ `np.any` และ `np.all`

```python
print(np.any(x > 8))
print(np.any(x < 0))
print(np.all(x < 10))
print(np.all(x == 6))
```

### ใช้ตาม axis ได้

```python
print(np.all(x < 8, axis=1))
```

### อธิบาย
- `np.any()` = มีอย่างน้อยหนึ่งค่าที่จริงไหม
- `np.all()` = ทุกค่าจริงไหม

---

## 20) Boolean Operators: `&`, `|`, `~`

ถ้าต้องการหลายเงื่อนไขพร้อมกัน ให้ใช้:

| Operator | ความหมาย | UFunc |
|---|---|---|
| `&` | AND | `np.bitwise_and` |
| `|` | OR | `np.bitwise_or` |
| `^` | XOR | `np.bitwise_xor` |
| `~` | NOT | `np.bitwise_not` |

ตัวอย่าง:

```python
data = np.array([0.1, 0.4, 0.6, 0.8, 1.2, 1.5])

mask = (data > 0.5) & (data < 1.0)
print(mask)
print(data[mask])
```

### สำคัญมาก
ต้องใส่วงเล็บรอบแต่ละเงื่อนไข

ถูก:

```python
(data > 0.5) & (data < 1.0)
```

ผิด:

```python
data > 0.5 & data < 1.0
```

เพราะ precedence จะทำให้ Python ตีความผิด

---

## 21) Boolean Mask คืออะไร

Boolean Mask คือ array ของ `True` / `False` ที่ใช้เลือกข้อมูล

```python
x = np.array([[5, 0, 3, 3],
              [7, 9, 3, 5],
              [2, 4, 7, 6]])

mask = x < 5

print(mask)
print(x[mask])
```

ผลลัพธ์:

```text
[0 3 3 3 2 4]
```

### อธิบาย
ตำแหน่งไหนเป็น `True` NumPy จะดึงค่านั้นออกมา  
ตำแหน่งไหนเป็น `False` จะถูกข้าม

---

## 22) ตัวอย่างจริง: วิเคราะห์เวลาตอบกลับของ API

เพื่อหลีกเลี่ยงข้อมูลเฉพาะขององค์กร เราใช้เคสทั่วไปอย่าง **API response time**

```python
response_ms = np.array([
    120, 135, 98, 240, 310, 180, 95, 400, 155, 210,
    130, 500, 145, 160, 175
])
```

### นับ request ที่ช้ากว่า 200 ms

```python
slow = response_ms > 200

print(slow)
print(np.sum(slow))
```

### ดึงเฉพาะ request ที่ช้า

```python
print(response_ms[slow])
```

### หาค่าเฉลี่ยเฉพาะ request ที่ช้า

```python
print(response_ms[slow].mean())
```

---

## 23) หลายเงื่อนไขพร้อมกัน

เช่น เลือก request ที่อยู่ระหว่าง 150 ถึง 300 ms

```python
mid_range = (response_ms >= 150) & (response_ms <= 300)

print(response_ms[mid_range])
print(np.sum(mid_range))
```

เลือกค่าที่ “ไม่ช้า”

```python
not_slow = ~(response_ms > 200)

print(response_ms[not_slow])
```

---

## 24) ตัวอย่างจริง: วิเคราะห์ sensor temperature

```python
temperature = np.array([
    28.5, 29.0, 30.2, 31.5, 35.0,
    36.2, 32.1, 29.8, 27.9, 38.0
])
```

### เงื่อนไขอุณหภูมิสูง

```python
high_temp = temperature > 35

print(high_temp)
print(temperature[high_temp])
```

### ค่าปกติในช่วง 29 ถึง 35

```python
normal_temp = (temperature >= 29) & (temperature <= 35)

print(temperature[normal_temp])
```

### สรุปผล

```python
print("จำนวนค่าที่สูงเกิน 35:", np.sum(high_temp))
print("ค่าเฉลี่ยช่วงปกติ:", temperature[normal_temp].mean())
```

---

## 25) `and/or` vs `&/|` ต่างกันยังไง

นี่คือจุดที่มือใหม่ NumPy งงบ่อยมาก

### `and` / `or`
ใช้กับ Boolean เดี่ยว ๆ หรือการตัดสินทั้ง object เป็นค่าเดียว

```python
print(bool(42))
print(bool(0))
print(bool(42 and 0))
print(bool(42 or 0))
```

### `&` / `|`
ใช้กับข้อมูลทีละ element หรือ Boolean array

```python
A = np.array([True, False, True, False])
B = np.array([True, True, False, False])

print(A & B)
print(A | B)
```

### ห้ามใช้แบบนี้กับ NumPy array

```python
x = np.arange(10)

# ผิด
# print((x > 4) and (x < 8))
```

ให้ใช้แบบนี้แทน

```python
print((x > 4) & (x < 8))
```

### จำง่าย ๆ
- Python ปกติ: ใช้ `and`, `or`, `not`
- NumPy array: ใช้ `&`, `|`, `~`

---

## 26) รวม Masking + Aggregation

นี่คือ pattern ที่ใช้บ่อยมากในงาน Data

```python
response_ms = np.array([
    120, 135, 98, 240, 310, 180, 95, 400, 155, 210,
    130, 500, 145, 160, 175
])

slow = response_ms > 200

print("จำนวน request ช้า:", np.sum(slow))
print("ค่าเฉลี่ย request ช้า:", response_ms[slow].mean())
print("ค่าสูงสุด request ช้า:", response_ms[slow].max())
print("p75 ของ request ทั้งหมด:", np.percentile(response_ms, 75))
```

### อธิบาย
เราสามารถสร้าง mask แล้วนำไปใช้กับ aggregation ได้ทันที  
นี่คือพื้นฐานของ exploratory data analysis

---

## 27) Mini Lab: วิเคราะห์ข้อมูล Log แบบง่าย

ให้ลองรันโค้ดนี้:

```python
import numpy as np

latency = np.array([
    85, 90, 95, 110, 120, 130, 140, 160, 180, 200,
    220, 250, 300, 350, 500
])

# 1) request ที่ช้ากว่า 200 ms
slow = latency > 200

# 2) request ที่อยู่ในช่วงปกติ 90-200 ms
normal = (latency >= 90) & (latency <= 200)

# 3) request ที่เร็วกว่า 90 ms
fast = latency < 90

print("จำนวนข้อมูลทั้งหมด:", latency.size)
print("Fast:", np.sum(fast))
print("Normal:", np.sum(normal))
print("Slow:", np.sum(slow))

print("ค่าเฉลี่ยทั้งหมด:", latency.mean())
print("ค่าเฉลี่ยเฉพาะ normal:", latency[normal].mean())
print("ค่า slow สูงสุด:", latency[slow].max())
print("P90:", np.percentile(latency, 90))
```

### คำถาม
- ทำไมค่าเฉลี่ยทั้งหมดอาจสูงกว่าความรู้สึกจริง?
- ทำไมต้องแยก slow request ออกมาดู?
- ทำไม percentile มีประโยชน์กว่าดูแค่ max?

---

# Cheat Sheet

## Broadcasting

| Concept | ความหมาย |
|---|---|
| Broadcasting | คำนวณ array shape ต่างกัน |
| Rule 1 | เติม `1` ด้านซ้ายถ้ามิติน้อยกว่า |
| Rule 2 | มิติที่เป็น `1` ขยายตามอีกฝั่ง |
| Rule 3 | ถ้าไม่เท่ากันและไม่มี `1` จะ error |
| `np.newaxis` | เพิ่มมิติใหม่ |
| `axis=0` | ทำงานตามแกนแรก / ยุบแถว |
| `axis=1` | ทำงานตามแกนสอง / ยุบคอลัมน์ |

## Boolean Mask

| Concept | ความหมาย |
|---|---|
| `x < 5` | ได้ Boolean array |
| `x[x < 5]` | เลือกเฉพาะค่าที่เข้าเงื่อนไข |
| `np.sum(mask)` | นับจำนวน True |
| `np.count_nonzero(mask)` | นับจำนวน True |
| `np.any(mask)` | มี True อย่างน้อยหนึ่งไหม |
| `np.all(mask)` | ทุกค่าเป็น True ไหม |
| `&` | AND แบบ element-wise |
| `|` | OR แบบ element-wise |
| `~` | NOT แบบ element-wise |

---

# สรุปท้าย EP

## สิ่งที่ต้องจำ

1. Broadcasting ทำให้คำนวณ array คนละ shape ได้
2. Broadcasting ไม่ได้ copy ข้อมูลจริงแบบตรง ๆ แต่เป็นกลไกการคำนวณที่มีประสิทธิภาพ
3. ต้องเข้าใจกฎ shape 3 ข้อ
4. `np.newaxis` ช่วยเพิ่มมิติเพื่อให้ broadcast ได้
5. Comparison operators ให้ผลลัพธ์เป็น Boolean array
6. Boolean mask ใช้เลือกข้อมูลที่เข้าเงื่อนไข
7. กับ NumPy array ให้ใช้ `&`, `|`, `~` ไม่ใช่ `and`, `or`, `not`
8. Masking + Aggregation คือ pattern สำคัญของงาน Data จริง


---

## EP ถัดไป
> EP5: Fancy Indexing + Sorting Arrays

---

## โค้ดทดลองรวมท้ายตอน

```python
import numpy as np

# -----------------------------
# Broadcasting
# -----------------------------
a = np.array([0, 1, 2])
M = np.ones((3, 3))

print("a + 5 =", a + 5)
print("M + a =")
print(M + a)

b = np.arange(3)[:, np.newaxis]
print("a + b =")
print(a + b)

# -----------------------------
# Centering data
# -----------------------------
X = np.random.random((10, 3))
Xmean = X.mean(axis=0)
X_centered = X - Xmean

print("Xmean =", Xmean)
print("Centered mean =", X_centered.mean(axis=0))

# -----------------------------
# Boolean comparisons
# -----------------------------
x = np.array([[5, 0, 3, 3],
              [7, 9, 3, 5],
              [2, 4, 7, 6]])

print("x < 5 =")
print(x < 5)

print("values < 5:")
print(x[x < 5])

print("count < 6:", np.sum(x < 6))
print("any > 8:", np.any(x > 8))
print("all < 10:", np.all(x < 10))

# -----------------------------
# Masking with real-like data
# -----------------------------
latency = np.array([
    85, 90, 95, 110, 120, 130, 140, 160, 180, 200,
    220, 250, 300, 350, 500
])

slow = latency > 200
normal = (latency >= 90) & (latency <= 200)
fast = latency < 90

print("Fast count:", np.sum(fast))
print("Normal count:", np.sum(normal))
print("Slow count:", np.sum(slow))
print("Slow values:", latency[slow])
print("Mean normal:", latency[normal].mean())
print("P90:", np.percentile(latency, 90))
```

---



