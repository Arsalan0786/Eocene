# 🌍 Ecosene: AI Waste Classifier

Ecosene is an AI-powered sustainability solution designed to classify waste materials (Plastic, Metal, Glass, Paper, Organic) using deep learning. The project includes a **FastAPI backend**, **PyTorch AI model**, and a **Gradio/Flask-based frontend**.

---

## 🚀 Features
- **AI-Powered Waste Classification** using a trained PyTorch model.
- **FastAPI Backend** for handling image uploads and predictions.
- **Frontend (Gradio + Flask)** for easy user interaction.
- **Hugging Face Deployment** for accessibility anywhere.

---

## 📂 Project Structure
```
Ecosene/
│── ai_chatbot/          # AI model & classifier
│   ├── waste_classifier.py  # Waste classification logic
│   ├── waste_model.py       # Model loading
│   ├── waste_model/         # Model storage folder
│   │   ├── data.pkl         # Trained AI model
│
│── backend/            # FastAPI backend
│   ├── server.py       # API server
│   ├── config.py       # Configuration settings
│   ├── utils.py        # Helper functions
│
│── frontend/           # Web Interface
│   ├── app.py          # Gradio-based UI
│   ├── templates/
│   │   ├── index.html  # Web UI (Flask-based)
│
│── venv/               # Virtual Environment
│── requirements.txt    # Dependencies
│── README.md           # Project documentation
│── Space.yaml          # Hugging Face config
│── .gitignore          # Files to ignore in Git
```

---

## 🛠 Installation & Setup
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/ecosene.git
cd ecosene
```

### **2️⃣ Create & Activate Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Run the Backend API (FastAPI)**
```bash
cd backend
uvicorn server:app --host 0.0.0.0 --port 7860
```

### **5️⃣ Run the Frontend (Gradio)**
```bash
cd frontend
python app.py
```

---

## 🚀 Deploy on Hugging Face
1. Push your code to GitHub:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```
2. Create a Hugging Face Space and set the SDK to `gradio` in `Space.yaml`.
3. Deploy your app and test it online!

---

## 📌 API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| `GET`  | `/` | Home endpoint |
| `POST` | `/predict/` | Upload an image & get waste classification |

---

## 🏆 Contributors
- **[Sheikh Arsalan](https://github.com/Arsalan0786)** - Backend & AI Model
- Team Members - Frontend & UI/UX

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 📢 Feedback & Support
If you have any questions or issues, feel free to open an **[issue](https://github.com/your-username/ecosene/issues)** on GitHub.

💡 Happy Coding & Let's Build a Sustainable Future! 🌱

