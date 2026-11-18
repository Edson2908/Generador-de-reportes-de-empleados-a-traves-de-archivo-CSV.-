# Employee Report Generator (CSV to Text)

A lightweight, zero-dependency Python automation script that parses employee records from a CSV file, aggregates headcount metrics by department, and generates a clean, alphabetically sorted summary report.

---

## Key Features

* **Zero External Dependencies:** Built entirely using Python's standard library (`csv` and `os`).
* **CSV File Validation:** Prompts for a CSV filename and reports an error if the file is missing or does not have a `.csv` extension.
* **Custom CSV Dialect Parsing:** Implements `csv.register_dialect` with `skipinitialspace=True` and `strict=True` to sanitize whitespace and enforce formatting integrity.
* **Cross-Platform Path Handling:** Uses `os.path` to dynamically resolve file paths, ensuring seamless execution across Windows, Linux, and macOS.
* **UTF-8 Encoding Support:** Safely processes special characters and accents during file read/write operations.

---

##  Project Structure

```text
employee-report-generator/
├── Employee Report CSV.py # Main automation script
├── employees.csv        # Example input dataset
├── report.txt           # Output summary report (generated)
└── README.md            # Project documentation
```

---

## Getting Started

### Prerequisites
* **Python 3.x** installed on your system.

### Installation & Usage

1. **Clone the repository** (or download the script):
   ```bash
   git clone https://github.com
   cd employee-report-generator
   ```

2. **Run the script:**
   ```bash
   python "Employee Report CSV.py"
   ```
3. **Enter the CSV filename** when prompted (for example, `employees.csv`). The file must be in the same folder as the script.

4. **View the generated report:**
   Open the newly created `report.txt` file in the project directory.

---

## Sample Input & Output

### Input (`employees.csv`)
```csv
Full Name,Username,Department
Audrey Miller,audrey,Development
Arden Garcia,ardeng,Sales
Bailey Thomas,baileyt,Human Resources
Blake Sousa,sousa,IT infrastructure
Cameron Nguyen,nguyen,Marketing
Charlie Grey,greyc,Development
```

### Output (`report.txt`)
```text
Development:2
Human Resources:1
IT infrastructure:1
Marketing:1
Sales:1
```

---

## How It Works

1. **`validate_csv_file()`**: Checks that the provided file has a `.csv` extension and exists. Otherwise, it raises an error.
2. **`read_employees()`**: Registers a custom CSV dialect and parses each row into a Python dictionary using `csv.DictReader`.
3. **`process_data()`**: Extracts department values, deduplicates keys using `set()`, and calculates total headcount per department.
4. **`write_report()`**: Sorts department names alphabetically and writes the formatted `Department:Count` pairs into `report.txt`.

---

## License

This project is open-source and available under the [MIT License](https://opensource.org).
