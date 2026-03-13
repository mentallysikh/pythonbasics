# 🐍 Python Automation & Systems Programming Suite

A collection of **10 standalone Python programs** designed to solve real-world problems in **automation, data processing, validation, and system monitoring**.

Each script demonstrates practical Python concepts such as:

- Regex validation
- Secure password generation
- File hashing
- System monitoring
- Linux automation
- Data transformation
- Version control simulation

All scripts include **clean console output, modular logic, and error handling**.

---

# 📂 Project Structure

| File | Description |
|-----|-------------|
| `q1_validation.py` | Network IP and Gmail identity validator |
| `q2_withregex.py` | Secure 16-character password generator using regex |
| `q2_withoutregex.py` | Secure password generator without regex |
| `q3_uptime.py` | Real-time URL health monitor with logging |
| `q4_updater.py` | Automated Linux package management tool |
| `q5_duplicate_finder.py` | Checksum-based duplicate file identification |
| `q6_visualizer.py` | ASCII table formatter for CSV files |
| `q7_ec2_recommend.py` | Cloud instance optimization based on CPU metrics |
| `q8_json_processor.py` | E-commerce JSON data restructuring and calculations |
| `q9_vcs_system.py` | Simulated file version control system |
| `q10_tuple_demo.py` | Demonstration of mutable object updates in tuples |

---
# 🛠️ Script Documentation & Logic

## 1️⃣ Network & Identity Validation (`q1_validation.py`)

### Purpose
Validates **IPv4 addresses** and **Gmail usernames**.

### Logic

**IPv4 Validation**
- Uses **Regular Expressions** for structural pattern matching
- Additional logic ensures:
  - Each octet is within **0–255**
  - No invalid **leading zeros**

**Gmail Validation**
- Ensures domain is **@gmail.com**
- Username validation allows only:
  - Letters
  - Numbers
  - `.`
  - `_`

---

## 2️⃣ Secure Password Generator (`q2_withregex.py`, `q2_withoutregex.py`)

### Purpose
Generates **strong 16-character passwords** with strict complexity requirements.

### Without Regex

Uses:
`random.sample()`

Ensures:
- Unique characters
- Balanced selection from character sets

### With Regex

Uses **Lookahead Assertions**:
`(?=.*[A-Z])`
`(?=.*[a-z])`
`(?=.*\d)`
`(?=.*[@#$%^&*])`

Ensures the password contains:
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

---

## 3️⃣ Website Uptime Monitoring System (`q3_uptime.py`)

### Purpose
Continuously checks website availability and detects **HTTP errors (4xx / 5xx)**.

### Key Features

**Logging**
Results are written to:
`uptime_monitor.log`

**Exponential Backoff**
If errors persist, the script **increases wait intervals automatically** to reduce network congestion.

---

## 4️⃣ Linux Package Updater (`q4_updater.py`)

### Purpose
Automates checking and installing **Linux package updates**.

### Key Features

**Interactive Package Selection**
Displays an indexed list of available upgrades and allows:
- Updating specific packages
- Performing bulk updates

**Error Logging**
Failures are logged in:
`package_update.log`

---

## 5️⃣ Duplicate File Finder (`q5_duplicate_finder.py`)

### Purpose
Detects duplicate files using **SHA-256 hashing**.

### Key Features

- Hash-based file comparison
- Minimum file size filter
- Detailed report generation

Output file:
`duplicate_report.txt`

---

## 6️⃣ CSV Table Visualizer (`q6_visualizer.py`)

### Purpose
Displays CSV data as **formatted ASCII tables** without external libraries.

### Implementation

- Dynamically calculates column widths
- Uses string padding with:

```python
str.ljust()
```

**Example Output**
```text
+---------+------+
| Name    | Age  |
+---------+------+
| Alice   | 24   |
| Bob     | 29   |
+---------+------+
```

---

## 7️⃣ EC2 Recommendation System (`q7_ec2_recommend.py`)

### Purpose
Recommends AWS EC2 instance resizing based on CPU utilization metrics.

### Logic
Instance size hierarchy:
`nano → micro → small → medium → large`

**Decision rules:**

| CPU Usage | Recommendation |
| :--- | :--- |
| **< 20%** | Downsize instance |
| **20–80%** | Instance is optimal |
| **> 80%** | Upgrade instance |

---

## 8️⃣ E-commerce JSON Order Processor (`q8_json_processor.py`)

### Purpose
Transforms nested JSON order data into a flattened CSV dataset.

### Calculations
- 10% discount applied to orders exceeding $100
- Shipping cost: $5 per item

### Data Processing
- Flatten hierarchical JSON structure
- Compute order totals
- Sort customers by total spending

---

## 9️⃣ Simple Version Control System (`q9_vcs_system.py`)

### Purpose
Implements a basic file version control system.

### Implementation
Versions are stored in:
`.versions/`

### Key Features
**Version Tracking**
Stores snapshots of file states.

**Diff Tool**
Shows line-by-line differences between versions.

**Automatic Cleanup**
Retains only the last N versions to reduce storage usage.

---

## 🔟 Tuple Mutation Demonstration (`q10_tuple_demo.py`)

### Purpose
Demonstrates how mutable objects inside tuples can still be modified.

### Example

```python
t = ([1,2,3],)
t[0].append(4)
```

The tuple itself remains unchanged, but the list inside it mutates.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone [https://github.com/mentallysikh/pythonbasics.git](https://github.com/mentallysikh/pythonbasics.git)
cd pythonbasics
```

### 2️⃣ Install Dependencies
Only required for the uptime monitor:

```bash
pip install requests
```

### 3️⃣ Run a Script
Example:

```bash
python q1_validation.py
```

---

## 📚 Concepts Demonstrated
This repository showcases several important Python programming concepts:

- Regular Expressions
- System Automation
- File Hashing
- Logging
- Data Transformation
- Linux Package Management
- Cloud Resource Optimization
- JSON & CSV Processing
- Version Control Concepts
- Python Mutability

---

## 👨‍💻 Author
**MentallySikh**
GitHub: [mentallysikh](https://github.com/mentallysikh)
