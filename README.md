## 🌸 Iris Flower Classification Web App


### 🧠 Overview
This is my *first end-to-end Machine Learning project, built using **Python, **Scikit-learn, and **Streamlit* in *PyCharm*.  
The goal of this project is to predict the *species of an Iris flower* — Setosa, Versicolor, or Virginica — based on four input parameters:  
*Sepal Length, Sepal Width, Petal Length, and Petal Width.*

This project demonstrates the complete *ML workflow*, from model training to deployment in a web application.


### 🚀 Features
- 🔹 *Random Forest Classifier* trained on the classic Iris dataset  
- 🔹 *Pickle integration* for saving and loading trained models  
- 🔹 *Streamlit web app* for real-time predictions  
- 🔹 Clean, responsive, and interactive UI  
- 🔹 Demonstrates the *end-to-end machine learning pipeline*


### 🧩 Tech Stack
| Category | Technologies Used |
|-----------|------------------|
| *Language* | Python 3 |
| *Libraries* | Pandas, NumPy, Scikit-learn, Streamlit, Pickle |
| *IDE* | PyCharm |
| *Model* | Random Forest Classifier |


### 🛠 Project Workflow

#### **1. Model Training (ML_API.py)**
- Loaded the Iris dataset from sklearn.datasets
- Split data using train_test_split (80% training, 20% testing)
- Trained a *Random Forest Classifier*
- Saved the trained model as iris_model.pkl using pickle

#### **2. Web App Development (app.py)**
- Created a Streamlit interface with 4 numeric input fields:
  - Sepal Length  
  - Sepal Width  
  - Petal Length  
  - Petal Width  
- Loaded the trained model to make predictions
- Displayed predicted flower species instantly upon button click



### 💻 How to Run Locally

1. *Clone this repository*
   ```bash
   git clone https://github.com/yourusername/iris-prediction-app.git
   cd iris-prediction-app

2. Install dependencies

pip install -r requirements.txt


3. Run the Streamlit app

streamlit run app.py


4. Open the app in your browser
Streamlit will automatically open a new tab (usually at http://localhost:8501/).


📊 Output

Input: Four numeric values (sepal/petal measurements)

Output: Predicted flower species (Setosa, Versicolor, or Virginica)


Example Interface:

<img width="1223" height="856" alt="app interface" src="https://github.com/user-attachments/assets/63b58385-5c37-4d2a-8e7e-a3773eac0a0c" />


## 🧠 Key Learnings

Through this project, I learned how to:

Train and evaluate an ML model using Scikit-learn

Save and reuse models using Pickle

Build and deploy an interactive Streamlit web application

Connect backend ML models with a user-facing frontend

Work with the complete ML development to deployment pipeline


## 📁 Repository Structure

iris-prediction-app/
│
├── app.py                # Streamlit web application
├── ML_API.py             # Model training and Pickle export
├── iris_model.pkl        # Saved ML model
├── requirements.txt      # Dependencies list
└── README.md             # Project documentation


## 🔗 Links

💻 Project Code: https://github.com/yourusername/iris-prediction-app

🌐 LinkedIn: www.linkedin.com/in/palagiri-reshma


## 🏁 Future Improvements

✅ Add model evaluation metrics and confusion matrix visualization

✅ Deploy the app on Streamlit Cloud or Hugging Face Spaces

✅ Add user interface styling and responsive layout


## 🏷 Tags

#MachineLearning #Python #Streamlit #DataScience #AI #ModelDeployment #RandomForest #ScikitLearn #PyCharm #FirstProject #GitHubProjects #LearningJourney


⭐ If you found this project useful, don’t forget to give it a star on GitHub!

“Every expert was once a beginner — this is where my ML journey begins.”
