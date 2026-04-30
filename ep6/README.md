# EP6: Structured Data (NumPy) + Mini Project

## เป้าหมายของตอนนี้

ในตอนนี้ เราจะเข้าสู่หัวข้อสุดท้ายของ NumPy พื้นฐาน คือ **Structured Arrays**  
ซึ่งใช้สำหรับเก็บข้อมูลหลายประเภท (heterogeneous data) ใน array เดียว

เมื่อเรียนจบตอนนี้ คุณจะเข้าใจ:
- ทำไม array ปกติไม่พอสำหรับข้อมูลบางประเภท
- Structured Array คืออะไร
- วิธีสร้าง dtype แบบหลาย field
- วิธีเข้าถึงข้อมูลแบบ column และ row
- การ filter ข้อมูลด้วย mask
- ข้อดี/ข้อจำกัด เทียบกับ Pandas
- Record Array คืออะไร
- ใช้งานจริงกับ Mini Project

---

# 🔧 ปัญหาที่เจอในโลกจริง

สมมุติว่าเรามีข้อมูล user:
- name
- age
- score

แบบนี้:
```python
name = ['Alice', 'Bob', 'Cathy', 'Doug']
age = [25, 45, 37, 19]
score = [88.5, 72.0, 91.2, 60.5]
```

### ❗ ปัญหา

- ข้อมูลแยกกัน 3 list
- ไม่มี structure บอกว่า index 0 ของทุก list คือคนเดียวกัน
- จัดการยาก

---

# แนวคิด Structured Array

เราสามารถรวมข้อมูลทั้งหมดไว้ใน array เดียวได้ โดยใช้ dtype แบบหลาย field

```python
import numpy as np

data = np.zeros(4, dtype={
    'names': ('name', 'age', 'score'),
    'formats': ('U10', 'i4', 'f8')
})
```

### อธิบาย dtype

| Field | Type | ความหมาย |
|------|------|----------|
| name | U10 | string ยาวไม่เกิน 10 |
| age | i4 | integer 32-bit |
| score | f8 | float 64-bit |

---

# ใส่ข้อมูล

```python
data['name'] = name
data['age'] = age
data['score'] = score

print(data)
```

---

# การเข้าถึงข้อมูล

## 1) เลือก column

```python
print(data['name'])
```

## 2) เลือก row

```python
print(data[0])
```

## 3) เข้าถึงค่าเฉพาะ field

```python
print(data[0]['name'])
```

---

# Filtering (สำคัญมาก)

```python
young = data[data['age'] < 30]

print(young)
print(young['name'])
```

---

# วิธีสร้าง dtype หลายแบบ

## แบบ dict

```python
np.dtype({
    'names': ('name', 'age'),
    'formats': ('U10', 'i4')
})
```

## แบบ list of tuple

```python
np.dtype([
    ('name', 'U10'),
    ('age', 'i4')
])
```

## แบบ string

```python
np.dtype('U10,i4,f8')
```

---

# Advanced: Field เป็น matrix

```python
tp = np.dtype([
    ('id', 'i8'),
    ('mat', 'f8', (3, 3))
])

X = np.zeros(1, dtype=tp)

print(X[0])
print(X['mat'][0])
```

---

# Record Array

```python
data_rec = data.view(np.recarray)

print(data_rec.age)
```

### ข้อดี
- เขียนสั้น (`data.age`)

### ข้อเสีย
- ช้ากว่าเล็กน้อย

---

# Structured Array vs Pandas

| Feature | NumPy | Pandas |
|--------|------|--------|
| speed | เร็ว | ช้ากว่านิด |
| flexibility | ต่ำ | สูง |
| query | basic | advanced |
| ใช้งานจริง | บางกรณี | ใช้บ่อย |

👉 สรุป: ใช้ Pandas ในงานจริงบ่อยกว่า

---

# Mini Project: Log Analyzer

## เป้าหมาย

วิเคราะห์ log ของระบบ เช่น:
- user_id
- latency
- status_code

---

## Step 1: สร้าง data

```python
N = 10

log = np.zeros(N, dtype=[
    ('user', 'i4'),
    ('latency', 'f8'),
    ('status', 'i4')
])

log['user'] = np.random.randint(1, 5, N)
log['latency'] = np.random.uniform(50, 500, N)
log['status'] = np.random.choice([200, 500], N)

print(log)
```

---

## Step 2: Filter error

```python
error = log[log['status'] == 500]
print(error)
```

---

## Step 3: หา slow request

```python
slow = log[log['latency'] > 300]
print(slow)
```

---

## Step 4: Top latency

```python
idx = np.argsort(log['latency'])[::-1]

print(log[idx])
```

---

## Step 5: หา average latency

```python
print(np.mean(log['latency']))
```

---

ใน EP นี้ เราได้เรียนรู้ Structured Arrays ซึ่งช่วยให้เราสามารถเก็บข้อมูลหลายประเภทไว้ใน array เดียวได้

แม้ว่าในงานจริงเรามักจะใช้ Pandas มากกว่า แต่การเข้าใจ Structured Array จะช่วยให้เราเข้าใจพื้นฐานของการจัดเก็บข้อมูลในระดับลึกขึ้น

และใน Mini Project เราได้นำความรู้ทั้งหมดมารวมกัน เพื่อวิเคราะห์ log แบบง่าย ๆ ด้วย NumPy

---

# 📌 สรุปทั้ง Series

- EP1: Data Types
- EP2: Arrays
- EP3: Ufuncs + Aggregation
- EP4: Broadcasting + Mask
- EP5: Fancy Index + Sorting
- EP6: Structured Data

👉 คุณพร้อมไปต่อ Pandas แล้ว
