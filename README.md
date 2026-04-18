# 🏥 Healthcare Blockchain Record System
🚀 A secure and transparent web-based application to manage patient medical records using **Blockchain concepts**.
---
## 🌐 Live Demo
👉 Add your deployed link here (Render / Replit)
---
## 📌 Project Overview

This project is designed to simulate a **blockchain-based healthcare record system** where:

* Doctors can securely log in
* Patient records are stored as **blocks**
* Data integrity is maintained using **hashing**
* Any tampering is **detected instantly**

---

## 🧠 Key Features

✅ 🔐 User Authentication (Login & Signup)
✅ 🧱 Blockchain-based Data Storage
✅ 📊 Dashboard with Statistics
✅ 🔍 Search Patient Records
✅ ✏️ Edit / Update Records
✅ 🗑️ Delete Records *(for demo purposes)*
✅ 🔐 Blockchain Validation (Tamper Detection)
✅ 🌍 Web-based UI (Accessible Anywhere)

---

## 🧬 How Blockchain is Used

Each patient record is stored as a **block** containing:

* Patient ID
* Diagnosis
* Treatment
* Timestamp
* Previous Hash
* Current Hash

### 🔗 Chain Integrity

Each block is linked to the previous block using hashing, ensuring:

* ❌ No data tampering
* ✅ Data transparency
* 🔐 High security

---

## ⚠️ Note on Editing & Deletion

* In real blockchain systems, data is **immutable**
* In this project:

  * Edit/Delete is allowed for **demonstration**
  * Any modification will break the chain integrity
  * The system detects this using validation

---

## 🛠️ Tech Stack

* **Frontend:** HTML, Bootstrap
* **Backend:** Python (Flask)
* **Database:** JSON (File-based)
* **Concept Used:** Blockchain (Hash Linking)

---

## 📁 Project Structure

```
healthcare-blockchain/
│
├── app.py
├── requirements.txt
├── README.md
│
└── templates/
    ├── login.html
    ├── signup.html
    ├── dashboard.html
    ├── view.html
    ├── search.html
    └── edit.html
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/healthcare-blockchain.git
cd healthcare-blockchain
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the application

```
python app.py
```

### 4. Open in browser

```
http://127.0.0.1:5000
```

---

## 🌍 Deployment

This project can be deployed using:

* Render (Recommended)
* Replit
* Ngrok (for temporary public access)

---

## 🎯 Use Case

* Hospitals for secure patient record sharing
* Multi-doctor collaboration
* Data integrity verification

---

## 💬 Viva Explanation (Short)

> “This system uses blockchain concepts to ensure secure and tamper-proof storage of healthcare records, allowing authorized doctors to access and manage patient data efficiently.”

---

## 📸 Screenshots (Optional)

*Add screenshots of your UI here for better presentation*

---

## 👩‍💻 Author

* Your Name

---

## ⭐ Conclusion

This project demonstrates how blockchain principles can be applied to healthcare systems to improve **security, transparency, and accessibility** of patient records.

---
