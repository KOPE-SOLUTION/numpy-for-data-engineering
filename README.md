# NumPy for Data Engineering 🇹🇭

โปรเจกต์นี้สร้างขึ้นเพื่อเรียนรู้ **NumPy สำหรับงาน Data Engineering / Data Analysis / AI**  
โดยเน้นอธิบายแบบเข้าใจง่าย พร้อมตัวอย่างโค้ด

---

## เป้าหมายของ Repo นี้

- เข้าใจการจัดการข้อมูลใน Python
- เข้าใจว่า NumPy ต่างจาก Python List ยังไง
- ใช้ NumPy ทำงานกับข้อมูลขนาดใหญ่ได้
- ปูพื้นฐานสำหรับงาน:
  - Data Analysis
  - Machine Learning
  - IoT Data Processing
  - Time-Series

---

## โครงสร้างเนื้อหา

### EP1: Understanding Data Types in Python
- Python Dynamic Typing
- Python Object Model
- Python List vs NumPy Array
- Fixed-Type Array
- การสร้าง NumPy Array
- dtype และการเลือกใช้งาน

👉 ไปที่: [ep1/README.md](./ep1/README.md)

---

### EP2: The Basics of NumPy Arrays
- NumPy Array คืออะไร (ndarray)
- Shape, Dimension, Size
- การเข้าถึงข้อมูล (Indexing)
- การ Slice ข้อมูล
- Multi-dimensional Array (1D, 2D, 3D)
- View vs Copy (สำคัญมาก)

👉 ไปที่: [ep2/README.md](./ep2/README.md)

---

### EP3: Computation on NumPy Arrays
- Universal Functions (ufunc)
- Vectorization (ทำไม NumPy ถึงเร็ว)
- Arithmetic Operations บน Array
- Aggregations (sum, mean, min, max)
- การคำนวณแบบรวดเร็วกับข้อมูลจำนวนมาก

👉 ไปที่: [ep3/README.md](./ep3/README.md)

---

### EP4: Broadcasting & Boolean Logic
- Broadcasting คืออะไร
- กฎของ Broadcasting
- การคำนวณข้าม Dimension
- Comparisons (>, <, ==)
- Boolean Masking
- Filtering ข้อมูลแบบมือโปร

👉 ไปที่: [ep4/README.md](./ep4/README.md)

---

### EP5: Advanced Indexing & Sorting
- Fancy Indexing
- Indexing ด้วย Array
- Boolean Indexing (ขั้นสูง)
- Sorting Arrays
- argsort และการเรียงข้อมูลแบบกำหนดเอง
- การเลือก Top-N Data

👉 ไปที่: [ep5/README.md](./ep5/README.md)

---

### EP6: Structured Data & Mini Project
- Structured Arrays คืออะไร
- การเก็บข้อมูลหลาย field (เหมือน table)
- การจัดการข้อมูลแบบ record
- การเตรียมข้อมูลสำหรับ Data Analysis
- Mini Project:
  - วิเคราะห์ dataset จริง (เช่น sensor / log / transaction)
  - ทำ filtering, sorting, aggregation
  - สรุปผลเป็น insight

👉 ไปที่: [ep6/README.md](./ep6/README.md)

---

## วิธีใช้งาน

```bash
# Clone repo
git clone https://github.com/your-username/numpy-for-data-engineering.git

# เข้า folder
cd numpy-for-data-engineering

# ใช้กับ Python
python3
```

---

## 📌 หมายเหตุ

เนื้อหาทั้งหมดเน้น:
- ใช้จริงในงาน Data
- ไม่เน้นทฤษฎีลึกเกินไป
- เหมาะสำหรับสาย:
  - IoT
  - AI
  - Data Engineer

---

เป้าหมายสุดท้าย:
> จาก Python ธรรมดา → ไปสู่ Data Engineer / AI Engineer
