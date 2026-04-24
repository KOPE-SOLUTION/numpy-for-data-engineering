# EP3 Part 2: Aggregations — Min, Max, and Everything In Between

## เป้าหมายของ Part นี้

ใน Part นี้ เราจะเรียนรู้การสรุปข้อมูลด้วย NumPy Aggregation Functions

เมื่อมีข้อมูลจำนวนมาก เรามักไม่ได้ต้องการดูค่าทุกตัว แต่ต้องการสรุปว่า

- ข้อมูลเฉลี่ยอยู่ที่เท่าไหร่
- ค่าต่ำสุด / สูงสุดคืออะไร
- ข้อมูลกระจายมากแค่ไหน
- ค่ากลางคืออะไร
- percentile เป็นอย่างไร
- มี missing value หรือ NaN ไหม

---

## 1) Aggregation คืออะไร

Aggregation คือการนำข้อมูลหลายค่า มาสรุปให้เหลือค่าหรือชุดค่าที่บอกภาพรวมได้

ตัวอย่างเช่น:

- `sum` ผลรวม
- `mean` ค่าเฉลี่ย
- `min` ค่าต่ำสุด
- `max` ค่าสูงสุด
- `std` ส่วนเบี่ยงเบนมาตรฐาน
- `median` มัธยฐาน
- `percentile` เปอร์เซ็นไทล์

---

## 2) `sum()` ของ Python vs `np.sum()`

```python
import numpy as np

L = np.random.random(100)

print(sum(L))
print(np.sum(L))
```

ผลลัพธ์ใกล้เคียงกัน แต่เมื่อข้อมูลมีขนาดใหญ่ `np.sum()` มักเร็วกว่า เพราะทำงานในระดับที่ optimized กว่า

```python
big_array = np.random.rand(1000000)

print(np.sum(big_array))
```

### ข้อควรจำ
ถ้าข้อมูลเป็น NumPy array ให้ใช้ฟังก์ชันของ NumPy เช่น

- `np.sum`
- `np.min`
- `np.max`
- `np.mean`

---

## 3) Min, Max, Sum

```python
big_array = np.random.rand(20)

print("min =", np.min(big_array))
print("max =", np.max(big_array))
print("sum =", np.sum(big_array))
```

หรือเขียนแบบ method ได้

```python
print("min =", big_array.min())
print("max =", big_array.max())
print("sum =", big_array.sum())
```

---

## 4) Aggregation กับข้อมูลหลายมิติ

สร้าง array 2 มิติ

```python
M = np.random.random((3, 4))

print(M)
```

### รวมทั้ง array

```python
print(M.sum())
```

### สรุปตามคอลัมน์

```python
print(M.min(axis=0))
```

### สรุปตามแถว

```python
print(M.max(axis=1))
```

---

## 5) เข้าใจ `axis`

`axis` เป็นเรื่องที่หลายคนสับสน

### วิธีจำ

- `axis=0` คือยุบแกนแถวลง เหลือผลลัพธ์ตามคอลัมน์
- `axis=1` คือยุบแกนคอลัมน์ลง เหลือผลลัพธ์ตามแถว

ตัวอย่าง:

```python
M = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("sum all =", M.sum())
print("sum axis=0 =", M.sum(axis=0))
print("sum axis=1 =", M.sum(axis=1))
```

---

## 6) Aggregation ที่ใช้บ่อยในงาน Data

```python
data = np.array([120, 135, 110, 98, 145, 160, 175, 130, 125, 140])

print("mean =", np.mean(data))
print("median =", np.median(data))
print("std =", np.std(data))
print("var =", np.var(data))
print("min =", np.min(data))
print("max =", np.max(data))
print("argmin =", np.argmin(data))
print("argmax =", np.argmax(data))
print("p25 =", np.percentile(data, 25))
print("p50 =", np.percentile(data, 50))
print("p75 =", np.percentile(data, 75))
```

### ความหมาย
- `mean` ค่าเฉลี่ย
- `median` ค่ากลาง
- `std` ความแกว่งของข้อมูล
- `var` ความแปรปรวน
- `argmin` index ของค่าต่ำสุด
- `argmax` index ของค่าสูงสุด
- `percentile` ใช้ดูการกระจายของข้อมูล

---

## 7) Boolean Aggregation

```python
data = np.array([120, 135, 110, 98, 145, 160, 175, 130, 125, 140])

print(np.any(data > 170))
print(np.all(data > 50))
```

### อธิบาย
- `np.any()` เช็กว่ามีค่าใดค่าหนึ่งเป็นจริงไหม
- `np.all()` เช็กว่าทุกค่าเป็นจริงไหม

ใช้บ่อยมากในการตรวจ condition ของข้อมูล

---

## 8) ฟังก์ชัน NaN-safe

ข้อมูลจริงมักมี missing value หรือ `NaN`

```python
x = np.array([1, 2, np.nan, 4, 5])

print("sum =", np.sum(x))
print("mean =", np.mean(x))
```

จะเห็นว่าผลลัพธ์อาจกลายเป็น `nan`

ให้ใช้เวอร์ชันที่ข้าม NaN แทน

```python
print("nansum =", np.nansum(x))
print("nanmean =", np.nanmean(x))
print("nanmin =", np.nanmin(x))
print("nanmax =", np.nanmax(x))
print("nanmedian =", np.nanmedian(x))
print("nanpercentile 50 =", np.nanpercentile(x, 50))
```

### ฟังก์ชันที่ควรรู้
- `np.nansum`
- `np.nanmean`
- `np.nanstd`
- `np.nanvar`
- `np.nanmin`
- `np.nanmax`
- `np.nanmedian`
- `np.nanpercentile`

---

## 9) ตัวอย่างงานจริง: วิเคราะห์เวลาตอบกลับของ API

ตัวอย่างนี้ใช้ข้อมูลสมมุติของ API response time หน่วยเป็น millisecond

```python
api_response_ms = np.array([120, 135, 110, 98, 145, 160, 175, 130, 125, 140])

print("Mean:   ", np.mean(api_response_ms))
print("Std:    ", np.std(api_response_ms))
print("Min:    ", np.min(api_response_ms))
print("Max:    ", np.max(api_response_ms))
print("Median: ", np.median(api_response_ms))
print("P75:    ", np.percentile(api_response_ms, 75))
```

### ตีความ
- `mean` คือเวลาตอบกลับเฉลี่ย
- `std` คือความแกว่งของระบบ
- `min` และ `max` คือขอบเขตต่ำสุด / สูงสุด
- `median` คือค่ากลางที่ทนต่อ outlier ได้ดีกว่า mean
- `percentile` ใช้ดูคุณภาพของระบบในเชิง distribution

---

## 10) ตัวอย่างงานจริง: ข้อมูลอุณหภูมิจาก Sensor

```python
temperature = np.array([29.5, 30.1, 30.0, 29.8, 31.2, 32.5, 33.0, 31.8, 30.6])

print("Mean: ", temperature.mean())
print("Min:  ", temperature.min())
print("Max:  ", temperature.max())
print("P25:  ", np.percentile(temperature, 25))
print("P50:  ", np.median(temperature))
print("P75:  ", np.percentile(temperature, 75))
```

---

## 11) Cheat Sheet Aggregation

| ฟังก์ชัน | ความหมาย |
|---|---|
| `np.sum` | ผลรวม |
| `np.prod` | ผลคูณ |
| `np.mean` | ค่าเฉลี่ย |
| `np.std` | ส่วนเบี่ยงเบนมาตรฐาน |
| `np.var` | ความแปรปรวน |
| `np.min` | ค่าต่ำสุด |
| `np.max` | ค่าสูงสุด |
| `np.argmin` | index ของค่าต่ำสุด |
| `np.argmax` | index ของค่าสูงสุด |
| `np.median` | มัธยฐาน |
| `np.percentile` | percentile |
| `np.any` | มีอย่างน้อยหนึ่งค่าที่เป็นจริง |
| `np.all` | ทุกค่าเป็นจริง |

---

## สรุป Part 2

สิ่งที่ต้องจำ:

1. Aggregation คือการสรุปข้อมูลจำนวนมาก
2. ใช้ NumPy aggregation เมื่อทำงานกับ NumPy array
3. `axis=0` และ `axis=1` สำคัญมาก
4. ข้อมูลจริงอาจมี `NaN` จึงควรรู้จัก NaN-safe functions
5. Aggregation เป็นพื้นฐานของ Exploratory Data Analysis

