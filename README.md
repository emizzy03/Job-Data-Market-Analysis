# Chicago Tech Job Market Analysis

A comprehensive data analysis project examining the Chicago tech job market using job postings scraped from Indeed. This project identifies in-demand technical skills, analyzes salary trends, and provides actionable career insights for data science, AI/ML, software engineering, and analytics professionals.

## 📊 Project Overview

This analysis examines tech job postings in Chicago, Illinois to answer key questions:
- What are the most in-demand technical skills?
- Which skill combinations are most valuable?
- What are the salary trends by skill category?
- How do skill requirements correlate with compensation?

## 🗂️ Project Structure

```
Job Market Data Analysis/
├── data/
│   └── jobs.csv                    # Raw job posting data from Indeed
├── notebooks/
│   └── analysis.ipynb              # Main analysis notebook
├── job_summary/
│   ├── cleaned_jobs.xlsx           # Cleaned dataset
└── README.md                       # This file
```

## 🛠️ Technologies Used

- **Python 3.11**
- **pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **matplotlib** - Data visualization
- **re** - Regular expressions for text parsing
- **collections.Counter** - Skill frequency counting

## 📈 Key Features

### 1. Data Cleaning & Preparation
- Parses salary strings in various formats (annual ranges, hourly rates, etc.)
- Removes duplicate job postings
- Normalizes job titles for consistent analysis
- Handles missing data appropriately

### 2. Skills Extraction
Identifies 50+ technical skills from job descriptions across categories:
- **Programming Languages**: Python, Java, JavaScript, SQL, R, Scala, Go, C++, etc.
- **Data & Analytics**: Pandas, NumPy, Tableau, Power BI, Spark, Hadoop
- **Cloud & DevOps**: AWS, Azure, GCP, Docker, Kubernetes, Terraform
- **AI/ML**: Machine Learning, Deep Learning, NLP, TensorFlow, PyTorch
- **Databases**: PostgreSQL, MySQL, MongoDB, Snowflake, Redshift
- **Web Frameworks**: React, Angular, Django, Flask, Node.js

### 3. Data Visualizations
- **Top In-Demand Skills Bar Chart** - Shows the 20 most requested skills
- **Salary by Skill Category** - Average compensation by technical domain
- **Skill Combination Analysis** - Most valuable skill pairs
- **Salary vs Skills Scatter Plot** - Correlation between skill requirements and pay

### 4. Career Insights
- Identifies highest-paying skill categories
- Recommends skill combinations for career advancement
- Provides salary benchmarks for different technical domains
- Highlights trending technologies in the Chicago market

## 🚀 Getting Started

### Prerequisites
```bash
pip install pandas numpy matplotlib openpyxl
```

### Running the Analysis

1. **Load the Notebook**
   ```bash
   jupyter notebook notebooks/analysis.ipynb
   ```
   Or open in VS Code with Jupyter extension

2. **Execute Cells Sequentially**
   - Cell 1: Load and clean job market data
   - Cell 2: Extract technical skills from job descriptions
   - Cells 3-6: Generate visualizations and insights
   - Cell 7: Print summary report
   - Cell 8: Export cleaned data with skills

3. **View Results**
   - Inline visualizations will appear after each chart cell
   - Summary statistics and insights printed to console
   - Exported Excel files saved to `job_summary/` directory

## 📋 Analysis Workflow

### Step 1: Data Loading & Cleaning
- Reads CSV file containing Indeed job postings
- Filters jobs with salary information
- Parses salary strings into numeric values
- Handles various salary formats (annual, hourly, ranges)

### Step 2: Skills Extraction
- Scans job descriptions for technical skill mentions
- Uses regex pattern matching for accurate skill detection
- Counts skill frequency across all job postings
- Calculates percentage of jobs requiring each skill

### Step 3: Salary Analysis
- Groups jobs by skill categories
- Calculates average salaries for each category
- Identifies highest-paying technical domains
- Analyzes relationship between skill count and compensation

### Step 4: Visualization & Reporting
- Creates publication-ready charts and graphs
- Generates summary report with key insights
- Exports cleaned data with extracted skills
- Provides actionable career recommendations

## 📊 Sample Insights

Based on the analysis of Chicago tech job postings:

- **Most In-Demand Skills**: Machine Learning (45.9%), Python (43.5%), SQL (43.5%)
- **Highest Paying Categories**: AI/ML roles, Cloud & DevOps, Data Engineering
- **Skill Combinations**: Python + SQL, AWS + Kubernetes, Machine Learning + Python
- **Average Salary**: Varies by role, with senior data scientist roles averaging $140K+

## 📝 Data Sources

- **Source**: Indeed.com job postings
- **Location**: Chicago, IL metropolitan area
- **Focus**: Technology, Data Science, AI/ML, Software Engineering positions
- **Date Range**: 2024 job postings

## 🔍 Key Metrics Analyzed

1. **Skill Frequency** - How often each skill appears in job postings
2. **Salary Statistics** - Mean, median, min, max salaries by category
3. **Skill Combinations** - Most common skill pairs and triplets
4. **Market Demand** - Percentage of jobs requiring specific skills
5. **Compensation Trends** - Salary correlation with skill requirements

## 💡 Use Cases

- **Job Seekers**: Identify which skills to develop for career growth
- **Recruiters**: Understand market demands and competitive salaries
- **Career Counselors**: Provide data-driven career guidance
- **Students**: Choose relevant courses and certifications
- **Employers**: Benchmark compensation and skill requirements

## 📦 Output Files

- `cleaned_jobs.xlsx` - Cleaned dataset with parsed salaries


## 🔧 Customization

To analyze different datasets or markets:
1. Update the CSV file path in Cell 1
2. Modify the `tech_skills` list in Cell 2 to add/remove skills
3. Adjust skill categories in visualization cells
4. Update location references in documentation

## 📊 Example Output

```
Chicago Tech Job Market Salary Stats:
   Average: $135,000/year
   Median:  $130,000/year
   Range:   $58,000 - $356,600/year

Top Tech Roles in Chicago:
   senior data scientist: 15 postings
   data engineer: 12 postings
   software engineer: 10 postings
```

## 🤝 Contributing

Feel free to extend this analysis by:
- Adding more skills to the detection list
- Including additional data sources (LinkedIn, Glassdoor)
- Expanding geographic coverage
- Adding time-series analysis for trends
- Implementing predictive modeling


