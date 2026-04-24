# EP3: Computation on NumPy Arrays + Aggregations

## เป้าหมายของ EP นี้

EP3 นี้แบ่งออกเป็น 2 Part เพื่อให้อ่านง่ายขึ้น เนื่องจาก ข้อมูลในส่วนนี้แน่น

---

## โครงสร้างไฟล์

```text
ep3/
├── README.md
├── part1-ufuncs/
│   └── README.md
├── part2-aggregations/
│   └── README.md
└── scripts/
    ├── ep3_part1_ufuncs.py
    └── ep3_part2_aggregations.py
```

---

## Part 1: Universal Functions (UFuncs)

หัวข้อนี้เน้นเรื่องการคำนวณบน NumPy Array ให้เร็วขึ้นด้วยแนวคิด **Vectorization** และ **Universal Functions**

### สิ่งที่จะได้เรียน
- ทำไม `for loop` ใน Python ถึงช้าเมื่อข้อมูลเยอะ
- Vectorization คืออะไร
- UFunc คืออะไร
- การคำนวณแบบ element-wise
- Arithmetic operations
- `np.add`, `np.multiply`, `np.abs`, `np.exp`, `np.log`
- Advanced UFunc เช่น `out=`, `reduce`, `accumulate`, `outer`

อ่านเนื้อหา: [part1-ufuncs/README.md](./part1-ufuncs/README.md)

รันตัวอย่าง:

```bash
python scripts/ep3_part1_ufuncs.py
```

---

## Part 2: Aggregations

หัวข้อนี้เน้นการสรุปข้อมูลจาก array จำนวนมาก เช่น ค่าเฉลี่ย ค่าสูงสุด ค่าต่ำสุด ส่วนเบี่ยงเบนมาตรฐาน และ percentile

### สิ่งที่จะได้เรียน
- Aggregation คืออะไร
- `sum()` ของ Python vs `np.sum()`
- `np.min`, `np.max`, `np.mean`, `np.std`
- การใช้ aggregation กับ array หลายมิติ
- การใช้ `axis=0` และ `axis=1`
- ฟังก์ชัน NaN-safe
- ตัวอย่างข้อมูล API response time และข้อมูล sensor

อ่านเนื้อหา: [part2-aggregations/README.md](./part2-aggregations/README.md)

รันตัวอย่าง:

```bash
python scripts/ep3_part2_aggregations.py
```

---

## วิธีใช้งานใน WSL Ubuntu

```bash
cd numpy-for-data-engineering/ep3

python3 -m venv .venv
source .venv/bin/activate

pip install numpy scipy

python scripts/ep3_part1_ufuncs.py
python scripts/ep3_part2_aggregations.py
```

---

## EP ถัดไป

> EP4: Broadcasting
