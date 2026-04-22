# EP1: Understanding Data Types in Python

## เป้าหมาย
เข้าใจว่า:
- Python เก็บข้อมูลยังไง
- ทำไม NumPy ถึงเร็วกว่า
- ทำไมต้องใช้ array แบบ fixed-type

---

## 1️ Python Dynamic Typing

```python
x = 4
x = "four"
```

- Python ไม่ต้องประกาศชนิดตัวแปร  
- ตัวแปรเปลี่ยน type ได้

ข้อดี: เขียนง่าย
ข้อเสีย: มี overhead

<details>
<summary>💡 Overhead คืออะไร?</summary>

Overhead คือ ภาระเพิ่มเติมที่ระบบต้องใช้ในการจัดการข้อมูล
เช่น type, pointer, metadata ต่าง ๆ

ใน Python:
- ตัวแปร 1 ตัว ไม่ได้เก็บแค่ค่า
- แต่เก็บข้อมูลเพิ่มเติมด้วย

ผลลัพธ์:
- ใช้ memory มากขึ้น
- ทำงานช้าลงเมื่อข้อมูลเยอะ

NumPy แก้ปัญหานี้โดย:
- ใช้ fixed-type array
- เก็บข้อมูลติดกันใน memory
- ลด overhead → ทำให้เร็วขึ้นมาก

</details>

---

## 2️ Python Object คืออะไร

Python variable = Object

<details>
<summary>Python Object(อธิบายแบบเข้าใจง่าย)</summary>

## แนวคิดพื้นฐาน
ใน Python ทุกอย่างคือ “Object”

```python
x = 4
```

ตัวแปร x ไม่ได้เก็บแค่เลข 4
แต่ชี้ไปยัง Object ที่เก็บข้อมูลหลายอย่าง

</details>

ไม่ได้เก็บแค่ค่า แต่มี:
- type
- memory info
- reference


---

## 3️ Python List

```python
L = [1, 2, 3]
L2 = ["a", "b", "c"]
L3 = [1, "a", 3.14]
```

- ใส่หลาย type ได้  
- ยืดหยุ่นมาก

❗ แต่ช้าเมื่อข้อมูลเยอะ

---

## 4️ ปัญหาของ List

List เก็บแบบ: pointer → object → data

ทำให้:
- memory กระจัดกระจาย
- CPU cache ใช้ไม่ดี
- คำนวณช้า

---

## 5️ Fixed-Type Array (แนวคิดสำคัญ)

ถ้าข้อมูลเป็นตัวเลขเหมือนกันทั้งหมด:
- ไม่ต้องเก็บ type ซ้ำ  
- เก็บติดกันใน memory ได้  

ผลลัพธ์:
- เร็วขึ้น
- ประหยัด memory

---

## 6️ NumPy คืออะไร

```python
import numpy as np
```

NumPy = library สำหรับจัดการ array เร็ว ๆ

---

## 7️ สร้าง NumPy Array

```python
np.array([1, 2, 3, 4])
```

---

## 8️ dtype

```python
np.array([1, 2, 3], dtype='float32')
```

📌 ทุก element ต้อง type เดียวกัน

---

## 9️ Upcasting

```python
np.array([3.14, 4, 2])
```

จาก int → float อัตโนมัติ

---

## 10 Multi-dimensional

```python
np.array([[1,2,3],[4,5,6]])
```

---

## 1️1️ สร้าง array แบบเร็ว

```python
np.zeros(5)
np.ones((2,3))
np.arange(0,10,2)
np.linspace(0,1,5)
```

---

## 1️2️ dtype ที่ควรรู้

- int32 / int64
- float32 / float64
- bool

---

## สรุป

| Python List | NumPy Array |
|------------|------------|
| ยืดหยุ่น | เร็ว |
| เก็บ object | เก็บ raw data |
| ช้า | เร็วมาก |

- Python ใช้งานง่ายเพราะ dynamic typing
- แต่มี cost เรื่อง performance
- NumPy แก้ปัญหานี้ด้วย fixed-type array
- ข้อมูลถูกเก็บแบบต่อเนื่องใน memory
- ทำให้เร็วมากสำหรับงาน data

---

EP ถัดไป:

> EP2 : The Basics of NumPy Arrays
