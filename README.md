# KAIM 3 Program - Test Project

## Week 0

### Project Overview
This is a Python-based project designed to analyze datasets and generate insightful reports for MoonLight Company. The project demonstrates foundational concepts and practical applications of data analysis.

---

## Getting Started

### 1. Setting Up the Virtual Environment
1. Navigate to your project directory:
   ```bash
   cd /path/to/project
   ```
2. Install the virtual environment package:
   ```bash
   pip install venv
   ```
3. Create a virtual environment:
   ```bash
   python3 -m venv <venv_name>
   ```
4. Activate the virtual environment:
   ```bash
   source <venv_name>/Scripts/activate
   ```
   **Note:** If activation fails, run the following command in your terminal and retry the activation:
   ```bash
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```

### 2. Installing Required Packages
Install all the dependencies listed in the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Running the Project
1. Execute the main script:
   ```bash
   python main.py
   ```
2. Open and run all cells in `notebook.ipynb` to analyze the data and generate reports.

### 4. Running the Dashboard  

To run the Streamlit dashboard, follow these steps:  

1. **Navigate to the Dashboard Directory**:  
   Open your terminal or command prompt and navigate to the `dashboard` directory:  
   ```bash
   cd dashboard
   ```

2. **Run the Dashboard**:  
   Start the Streamlit application by executing:  
   ```bash
   streamlit run app.py
   ```
   Or
   ```bash
   python -m streamlit run app.py
   ```

4. **View the Dashboard**:  
   Once the server starts, a link will be provided (e.g., `http://localhost:8501`). Click the link or copy it into your browser to interact with the dashboard.  

---

## Author
**Yonas Walelign**  
Email: [yonaseth12@gmail.com](mailto:yonaseth12@gmail.com)

---

Feel free to reach out for questions or collaboration opportunities!
