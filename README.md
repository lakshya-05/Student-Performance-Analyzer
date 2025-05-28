# 🎓 Student Performance Analyzer

A collaborative Flask-based web application developed by Kid and Khushi to analyze academic performance of 2,000 students. Utilizing the power of Pandas and Matplotlib, this tool offers insightful visualizations and analyses to aid educators and students alike.

## 📌 Project Overview

This project aims to provide a user-friendly interface for analyzing student performance data. By leveraging data visualization and statistical analysis, users can gain a deeper understanding of academic trends and individual student metrics.

## 🛠️ Features

- **Interactive Dashboard**: Visual representations of student performance metrics.
- **Individual Analysis**: Detailed insights into each student's academic journey.
- **Comparative Studies**: Compare performances across different cohorts or subjects.
- **Data Filtering**: Customize views based on specific criteria or parameters.

## 📂 Project Structure

```
Student-Performance-Analyzer/
├── Data/
│   └── student_data.csv
├── templates/
│   ├── index.html
│   ├── full.html
│   └── individual.html
├── static/
│   └── styles.css
├── analysis.py
├── main.py
├── DataAnalysis.ipynb
└── README.md
```

- **Data/**: Contains the dataset used for analysis.
- **templates/**: HTML templates rendered by Flask.
- **static/**: CSS files and other static assets.
- **analysis.py**: Core analysis functions.
- **main.py**: Entry point of the Flask application.
- **DataAnalysis.ipynb**: Jupyter notebooks for exploratory data analysis.

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/lakshya-05/Student-Performance-Analyzer.git
   cd Student-Performance-Analyzer
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages**:

   ```bash
   pip install flask pandas matplotlib
   ```

### Running the Application

```bash
python main.py
```

Navigate to `http://127.0.0.1:5000/` in your web browser to access the application.

## 📊 Usage

- **Home Page**: Overview of the dataset with general statistics.
- **Individual Analysis**: Enter a student's ID to view detailed performance metrics.
- **Full Analysis**: Full analysis of students and their performance.

## 🧠 Insights

Through this application, users can:

- Identify top-performing students and subjects.
- Detect areas where students are underperforming.
- Make informed decisions to enhance teaching strategies.

## 🤝 Contributing

This project was developed by Kid and Khushi. If you'd like to contribute or build upon it, feel free to fork the repository and submit a pull request.

## ✒️ Authors

- [Kid](https://github.com/lakshya-05)
- [Khushi](https://github.com/jainkhushi22)
