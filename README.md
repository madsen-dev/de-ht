# Home Task - Data Engineering Solution

This repository contains solutions for a home task focused on data engineering.

## Prerequisites

- Python 3.12.3
- Virtual environment (recommended)

## Setup

1. Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install the required dependencies for analytics:

```bash
pip install -r requirements.txt
```

## Repository Structure

### Analytics (`/analytics`)

This folder contains data generation and analysis script.

**Files:**

- `generate_data.py` - Generates sample data (100 invoices and 10 countries) and saves to `invoices.csv`
- `sql_top_5_countries.py` - Performs SQL-based analysis using DuckDB, pandas, and numpy to find top 5 countries

**Technologies:** Python, SQL, DuckDB, Pandas, NumPy

### Programming (`/programming`)

This folder contains two different approaches to solving a string character uniqueness analysis.

**Files:**

- `simple_is_string_characters_unique.py` - Simple, readable solution that's quick to implement but less efficient for long strings
- `advanced_is_string_characters_unique.py` - Optimized solution with early exit capability for better performance on long strings. Also returns both unique and non-unique characters

**Key Differences:**

- **Simple**: Quick implementation, readable code, handles short-to-medium strings efficiently
- **Advanced**: Better performance on long strings due to early termination, provides additional insights (unique/non-unique character breakdown)

**Technologies:** Python

#### Tests (`/programming/tests`)

Contains test suites for both programming solutions to ensure correctness and reliability.

**Note:** Test cases were generated using AI assistance to improve development efficiency and coverage.

### Data Engineering (`/data-engineering`)

**Files:**

- `architecture.md` - Documentation covering:
  - Task description
  - Basic idea
  - Proposed solution
  - End-to-end flow

## Getting Started

1. **Generate Sample Data:**

   ```bash
   cd analytics
   python generate_data.py
   ```

2. **Run Analytics:**

   ```bash
   python sql_top_5_countries.py
   ```

3. **Test Programming Solutions:**

   ```bash
   cd programming
   python simple_is_string_characters_unique.py
   python advanced_is_string_characters_unique.py
   ```

4. **Run Tests:**
   ```bash
   From root/ directory:
   python -m pytest -v programming/tests/
   ```

## Technology Stack

- **Python 3.12.3**
- **SQL**
- **DuckDB**
- **Pandas**
- **NumPy**

## Solution Philosophy

This solution demonstrates different approaches to problem-solving in data engineering:

- **Simplicity vs. Optimization** - Comparing straightforward implementations with performance-optimized solutions
- **Modern Data Tools** - Leveraging DuckDB for efficient SQL-based analytics
- **Testing Best Practices** - Comprehensive test coverage for reliability
- **Documentation** - Clear architecture documentation for scalable solutions
