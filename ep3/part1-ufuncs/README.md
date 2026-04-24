# EP3 Part 1: Computation on NumPy Arrays — Universal Functions

## เป้าหมายของ Part นี้

ใน Part นี้ เราจะเรียนรู้ว่า NumPy ทำให้การคำนวณบนข้อมูลจำนวนมากเร็วขึ้นได้อย่างไร โดยเน้นแนวคิดสำคัญคือ

- Vectorization
- Universal Functions หรือ UFuncs
- การคำนวณแบบ element-wise
- การลดการใช้ `for loop`
- ฟังก์ชันคณิตศาสตร์ที่ใช้บ่อยใน NumPy

---

## 1) ทำไม NumPy ถึงเร็วกว่า loop ธรรมดา

ใน Python เราสามารถวนลูปเพื่อคำนวณค่าทีละตัวได้ เช่น การหาค่า reciprocal หรือ `1 / x`

```python
import numpy as np

np.random.seed(0)

def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output

values = np.random.randint(1, 10, size=5)

print("values =", values)
print("reciprocal by loop =", compute_reciprocals(values))
```

<details>
<summary>อธิบาย</summary>

โค้ดนี้เข้าใจง่าย แต่ถ้าข้อมูลมีจำนวนมาก เช่น หลักแสนหรือหลักล้าน การวนลูปใน Python จะเริ่มช้า เพราะ Python ต้องจัดการหลายอย่างในแต่ละรอบ เช่น

- ตรวจสอบชนิดข้อมูล
- เรียก object
- จัดการ function dispatch
- ทำงานแบบ interpreted language

</details>


---

## 2) Vectorization คืออะไร

แทนที่จะวนลูปเอง เราสามารถให้ NumPy คำนวณทั้ง array ได้ในคำสั่งเดียว

```python
print("reciprocal by loop =", compute_reciprocals(values))
print("reciprocal by NumPy =", 1.0 / values)
```

ผลลัพธ์เหมือนกัน แต่แนวทางของ NumPy เร็วกว่าเมื่อข้อมูลใหญ่

<details>
<summary>สรุปแนวคิด</summary>

- Loop เอง = คำนวณทีละ element ด้วย Python
- Vectorization = เขียนคำสั่งเดียวให้ NumPy คำนวณทั้ง array
- ยิ่งข้อมูลใหญ่ ยิ่งเห็นความต่าง

</details>

---

## 3) UFunc คืออะไร

`ufunc` ย่อมาจาก **Universal Function**  คือ ฟังก์ชันของ NumPy ที่ทำงานแบบ element-wise บน array ได้อย่างรวดเร็ว

ตัวอย่าง:

```python
x = np.arange(5)

print("x =", x)
print("1.0 / x[1:] =", 1.0 / x[1:])
```

### คำนวณระหว่าง array กับ array

```python
a = np.arange(5)
b = np.arange(1, 6)

print("a =", a)
print("b =", b)
print("a / b =", a / b)
```

### คำนวณกับ array หลายมิติ

```python
x = np.arange(9).reshape((3, 3))

print("x =")
print(x)

print("2 ** x =")
print(2 ** x)
```

### จุดสำคัญ
- UFunc ทำงานกับทุก element
- ใช้ได้กับ scalar + array
- ใช้ได้กับ array + array
- ใช้ได้กับ array หลายมิติ

---

## 4) Array Arithmetic ที่ใช้บ่อย

NumPy ใช้ operator ปกติได้ เช่น `+`, `-`, `*`, `/`, `//`, `**`, `%`

```python
x = np.arange(4)

print("x      =", x)
print("x + 5  =", x + 5)
print("x - 5  =", x - 5)
print("x * 2  =", x * 2)
print("x / 2  =", x / 2)
print("x // 2 =", x // 2)
print("-x     =", -x)
print("x ** 2 =", x ** 2)
print("x % 2  =", x % 2)
```

### Expression ซ้อนกันได้

```python
result = -(0.5 * x + 1) ** 2
print(result)
```

---

## 5) Operator เหล่านี้คือ UFunc

จริง ๆ แล้ว operator ต่าง ๆ เป็น shortcut ของฟังก์ชันใน NumPy

```python
x = np.arange(4)

print(np.add(x, 2))
print(np.subtract(x, 2))
print(np.multiply(x, 2))
print(np.divide(x, 2))
print(np.power(x, 2))
print(np.mod(x, 2))
```

| Operator | UFunc | ความหมาย |
|---|---|---|
| `+` | `np.add` | บวก |
| `-` | `np.subtract` | ลบ |
| `*` | `np.multiply` | คูณ |
| `/` | `np.divide` | หาร |
| `//` | `np.floor_divide` | หารปัดลง |
| `**` | `np.power` | ยกกำลัง |
| `%` | `np.mod` | หารเอาเศษ |

---

## 6) Absolute Value

```python
x = np.array([-2, -1, 0, 1, 2])

print(abs(x))
print(np.absolute(x))
print(np.abs(x))
```

### Complex Number

```python
x = np.array([3 - 4j, 4 - 3j, 2 + 0j, 0 + 1j])

print(np.abs(x))
```

### อธิบาย
สำหรับจำนวนเชิงซ้อน `np.abs()` จะคืนค่า magnitude

---

## 7) Trigonometric Functions

```python
theta = np.linspace(0, np.pi, 3)

print("theta      =", theta)
print("sin(theta) =", np.sin(theta))
print("cos(theta) =", np.cos(theta))
print("tan(theta) =", np.tan(theta))
```

### Inverse Trigonometric

```python
x = [-1, 0, 1]

print("arcsin(x) =", np.arcsin(x))
print("arccos(x) =", np.arccos(x))
print("arctan(x) =", np.arctan(x))
```

### หมายเหตุ
บางค่าที่ควรเป็น 0 อาจไม่ออกมาเป็น 0 เป๊ะ เพราะคอมพิวเตอร์คำนวณด้วย floating point

---

## 8) Exponential และ Logarithm

### Exponential

```python
x = [1, 2, 3]

print("exp(x)  =", np.exp(x))
print("exp2(x) =", np.exp2(x))
print("3^x     =", np.power(3, x))
```

### Logarithm

```python
x = [1, 2, 4, 10]

print("ln(x)    =", np.log(x))
print("log2(x)  =", np.log2(x))
print("log10(x) =", np.log10(x))
```

### ฟังก์ชันที่แม่นขึ้นสำหรับค่าขนาดเล็ก

```python
x = [0, 0.001, 0.01, 0.1]

print("expm1(x) =", np.expm1(x))
print("log1p(x) =", np.log1p(x))
```

### อธิบาย
- `np.expm1(x)` คือ `exp(x) - 1`
- `np.log1p(x)` คือ `log(1 + x)`
- ใช้เมื่อต้องการความแม่นยำกับค่าขนาดเล็กมาก

---

## 9) Specialized UFuncs

NumPy ยังมีฟังก์ชันเฉพาะทางอีกจำนวนมาก เช่น

- comparison
- bitwise
- rounding
- degree/radian conversion

ถ้าต้องการฟังก์ชันคณิตศาสตร์พิเศษ สามารถใช้ `scipy.special`

```python
from scipy import special

x = [1, 5, 10]

print("gamma(x)   =", special.gamma(x))
print("gammaln(x) =", special.gammaln(x))
print("beta(x, 2) =", special.beta(x, 2))
```

```python
x = np.array([0, 0.3, 0.7, 1.0])

print("erf(x)    =", special.erf(x))
print("erfc(x)   =", special.erfc(x))
print("erfinv(x) =", special.erfinv(x))
```

---

## 10) Advanced UFunc Features

### 10.1 กำหนด output ด้วย `out=`

```python
x = np.arange(5)
y = np.empty(5)

np.multiply(x, 10, out=y)

print(y)
```

เขียนผลลัพธ์ลงบางตำแหน่งได้

```python
y = np.zeros(10)

np.power(2, x, out=y[::2])

print(y)
```

### อธิบาย
`out=` ช่วยลดการสร้าง temporary array ซึ่งมีประโยชน์มากเมื่อข้อมูลมีขนาดใหญ่

---

### 10.2 reduce

```python
x = np.arange(1, 6)

print(np.add.reduce(x))
print(np.multiply.reduce(x))
```

### อธิบาย
- `np.add.reduce(x)` รวมค่าทั้งหมด
- `np.multiply.reduce(x)` คูณค่าทั้งหมด

---

### 10.3 accumulate

```python
print(np.add.accumulate(x))
print(np.multiply.accumulate(x))
```

### อธิบาย
`accumulate` แสดงผลสะสมทุกขั้น เช่น cumulative sum หรือ cumulative product

---

### 10.4 outer

```python
x = np.arange(1, 6)

print(np.multiply.outer(x, x))
```

### อธิบาย
`outer` ใช้คำนวณทุกคู่ระหว่าง input สองชุด เหมาะกับงาน pairwise calculation

---

## สรุป Part 1

สิ่งที่ต้องจำ:

1. NumPy เร็วเพราะใช้ vectorized operations
2. UFunc คือฟังก์ชันที่คำนวณแบบ element-wise
3. ควรลดการเขียน loop เองเมื่อทำงานกับ array
4. Operator ปกติ เช่น `+`, `-`, `*`, `/` ใช้กับ NumPy array ได้เลย
5. `out=`, `reduce`, `accumulate`, `outer` เป็น feature ขั้นสูงที่มีประโยชน์มาก

