# *AI Hospital Management System 🚑🧠*

An AI-powered hospital management system with *disease prediction, patient management, and doctor-patient interaction* features using *Flask, MySQL, and Machine Learning*.

---

## 📌 *Features*
✔ *AI-Based Disease Prediction* (using Random Forest Model)  
✔ *Role-Based Authentication* (Patients, Doctors, Admins)  
✔ *Patient Medical History Management*  
✔ *Admin Dashboard for Doctor-Patient Management*  
✔ *Interactive Web UI* (HTML, CSS, JavaScript)  
✔ *Secure Database Storage (MySQL)*  
✔ *CSV-Based Disease Details Retrieval*  

---

## 📁 *Project Directory Structure*

/ai_hospital_management_project
│── app.py               # Main Flask app
│── authapp.py           # Authentication system
│── config.py            # Database configurations
│── models.py            # Database models
│── routes.py            # API routes for handling web requests
│── random_forest_model.pkl # Pre-trained AI model
│── templates/           # HTML UI files
│── static/              # CSS & JavaScript files
│── datasets/            # CSV files (disease-related data)
│── requirements.txt     # Dependencies
│── README.md            # Project documentation
│── Project Requirement.pdf # Detailed requirement doc


---

## 🚀 *Installation & Setup*
### 🔹 *Prerequisites*
- *Python 3.8+*
- *MySQL Database*
- *Virtual Environment* (recommended)

### 🔹 *Steps to Run*
1️⃣ *Clone the Repository*
bash
git clone https://github.com/yourusername/AI-Hospital-Management-System.git
cd AI-Hospital-Management-System

2️⃣ *Create & Activate Virtual Environment*
bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

### *3️⃣ Required Packages Installation*
Before running the project, install all required dependencies using:
bash
pip install -r requirements.txt


If you don’t have a requirements.txt file, create one using:
bash
pip freeze > requirements.txt


Or manually install the main packages used in the project:
bash
pip install flask flask-mysql flask-login pandas scikit-learn


If your project includes *Jupyter Notebook* for ML model training, also install:
bash
pip install jupyter notebook matplotlib seaborn


4️⃣ *Set Up MySQL Database*
- Update config.py with your MySQL credentials.
- Run database migrations:
bash
python manage.py migrate

5️⃣ *Run the Flask App*
bash
python app.py

6️⃣ *Access Web Interface*
- Open *http://127.0.0.1:5000* in a browser.

---

## 🎯 *Usage*
### ✅ *Patient Portal*
- Register/Login
- Input symptoms for AI-based disease prediction
- View suggested medications, diets, and precautions
- Save medical history

### ✅ *Doctor/Admin Portal*
- View & manage patient records
- Assign treatments & provide recommendations

### ✅ *AI-Based Prediction*
- Uses *Random Forest Model* to predict diseases
- Fetches disease details from *CSV datasets*

---

## 📊 *Datasets Used*
| *Dataset*       | *Purpose* |
|-------------------|------------|
| description.csv | Disease descriptions |
| diets.csv | Recommended diets |
| medications.csv | Suggested medicines |
| precautions.csv | Precautionary measures |

---

## 🤖 *Machine Learning Model*
- *Algorithm:* *Random Forest Classifier*
- *Trained on* symptom-disease dataset
- *Evaluated with* accuracy, precision, recall, and F1-score

---

## 🚀 *Future Enhancements*
📌 *Deep Learning integration for higher accuracy*  
📌 *Real-time doctor-patient chat system*  
📌 *Automated prescription generation*  
📌 *Mobile App for remote patient access*  

---

## 🤝 *Contributing*
Pull requests are welcome! Please follow these steps:  
1. *Fork the repository*  
2. *Create a new branch* (feature-xyz)  
3. *Commit changes*  
4. *Push & create a Pull Request*  

---

## 📜 *License*
This project is licensed under the *MIT License*.
