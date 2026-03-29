#  Smart Expense Categorizer using Machine Learning

##  Overview

Managing daily expenses is a common challenge for students and individuals. This project aims to automatically categorize expenses and provide useful insights using Machine Learning techniques.

The system takes a text-based expense input (e.g., *"Dominos pizza 250"*) and predicts its category such as Food, Travel, Shopping, etc., while also tracking overall spending behavior.

---

##  Problem Statement

People often struggle to track and analyze their expenses manually. This project solves the problem by:

* Automatically classifying expenses
* Providing spending summaries
* Generating simple financial insights

---

##  Features

*  Automatic expense categorization using ML
*  Category-wise spending analysis
*  Visualization using pie charts
*  Smart suggestions based on spending patterns
*  NLP-based text processing

---

##  Technologies Used

* Python
* Scikit-learn
* Pandas
* Matplotlib
* Natural Language Processing (TF-IDF)

---

##  Project Structure

```
expense-ai/
│── data/
│   └── expenses.csv
│── src/
│   ├── preprocess.py
│   ├── model.py
│   ├── predict.py
│   └── utils.py
│── main.py
│── README.md
│── requirements.txt
```

---

## ⚙️ How It Works

1. User enters an expense description
2. Text is cleaned and preprocessed
3. TF-IDF converts text into numerical features
4. Naive Bayes model predicts category
5. System stores and analyzes expenses
6. Summary and insights are generated

---

##  How to Run

### 1. Clone the repository

```
git clone <your-repo-link>
cd expense-ai
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Train the model

```
python src/model.py
```

### 4. Run the application

```
python main.py
```

---

##  Sample Input

```
Dominos pizza 250
Uber ride 120
Zara shirt 1500
```

---

##  Sample Output

```
Category: Food
Amount: ₹250

Total Spending: ₹1870
Top Category: Shopping

Breakdown:
Food: ₹250
Travel: ₹120
Shopping: ₹1500
```

---

##  Visualization

The project generates a pie chart showing spending distribution across categories.

---

##  Insights

* Identifies highest spending category
* Suggests areas to reduce expenses
* Helps improve financial awareness

---

##  Challenges Faced

* Small dataset size
* Handling text variations in input
* Model accuracy improvements

---

##  Future Improvements

* Larger dataset for better accuracy
* Integration with mobile apps
* Real-time expense tracking
* Advanced ML models (Deep Learning)

---

##  Author

Rushil

---

##  Conclusion

This project demonstrates how Machine Learning can be applied to solve real-world problems like expense tracking. It combines NLP, classification, and data analysis to deliver meaningful insights in a simple and efficient way.
