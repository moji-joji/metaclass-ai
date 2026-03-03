# 🎓 MetaClass: Attentiveness Detection in a Metaverse Classroom

> An AI-powered metaverse classroom that detects and enhances student attentiveness using real-time sensor data, AI models, and immersive 3D learning environments.

---

## 🧠 Overview

**MetaClass** is an innovative virtual reality learning platform designed to make online education immersive and intelligent.
It uses **sensor data from Meta Quest headsets** combined with **machine learning models** to measure and enhance student attentiveness in real-time.

This project bridges the gap between traditional and online learning, empowering teachers to adapt their lectures dynamically based on live feedback from student attentiveness data.

---

## 🎥 Project Report

👉 [MetaClass Project Report and Demo](https://drive.google.com/drive/folders/1Um9HThjMoAsndiawDfsPynn0y3UsOhzq?usp=sharing)

---

## 🧩 Key Features

* **🧭 Real-Time Attentiveness Detection** – Monitors head and hand movements from Meta Quest 2 and predicts focus level.
* **🤖 AI Teacher & NPC Interactions** – Simulated classmates and instructors powered by NLP and voice synthesis.
* **⚠️ Low Attention Alerts** – Automatic notifications or camera recentering when engagement drops.
* **🧪 Continuous Performance Test (CPT)** – Measures attention through task-based interaction.
* **📊 Analytics Dashboard** – Provides educators with live attention insights and historical data.
* **🎮 Fully Immersive VR Environment** – Interactive classroom experience built with Unity 3D.

---

## 🛠️ Tech Stack

| Component                         | Technology                        |
| --------------------------------- | --------------------------------- |
| **VR Development**                | Unity 3D, C#                      |
| **Headset Integration**           | Meta Quest 2 + Oculus SDK         |
| **Machine Learning**              | TensorFlow, Keras, scikit-learn   |
| **Model Hosting / API**           | FastAPI, AWS EC2                  |
| **AI NPCs & Voice**               | HuggingFace, OpenAI, Amazon Polly |
| **Visualization & Data Handling** | Python (pandas, matplotlib)       |
| **Version Control**               | GitHub                            |

---

## 💻 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/moji-joji/metaclass-ai.git
cd metaclass-ai
```

### 2. Access the Unity Project

📦 **Download Unity Project:**
[Unity Build Files (Google Drive)](https://drive.google.com/file/d/1Yz7zKEcFfL2oYNpsqv6oR3WSBBnaARYN/view?usp=sharing)

Open the project in **Unity 2022.1+** with the **Oculus Integration SDK** installed.

### 3. ML Model Setup

📂 **Random Forest Regressor Weights:**
[Download Model Weights (.pkl)](https://drive.google.com/file/d/12iVARFTSgeMRapzTIYI3IQDZkJGH7Pfo/view?usp=sharing)

Place the weights file in the `/model` directory, then run:

```bash
python app.py
```

to start the **FastAPI** server for attentiveness predictions.

---

## 🧮 System Architecture

1. **Meta Quest Sensors** – capture head & hand motion data
2. **Unity Environment** – transmits real-time sensor data
3. **FastAPI Server (AWS)** – processes data & predicts attentiveness
4. **ML Model (Random Forest Regressor)** – outputs engagement score
5. **Teacher Dashboard** – displays student focus levels

```
Meta Quest Sensors → Unity VR Client → FastAPI API → ML Model → Dashboard Feedback
```

---

## 👨‍🏫 User Roles

* **Students:** Attend VR lectures and receive engagement feedback.
* **Teachers:** View live attentiveness and adjust teaching style accordingly.
* **Administrators:** Manage users, system metrics, and model configurations.

---

## 🧠 Machine Learning

* **Algorithm:** Random Forest Regressor
* **Input Features:** Head pitch, yaw, roll; hand movement vectors; body orientation
* **Output:** Real-time attentiveness score (0–100%)
* **Deployment:** Hosted on AWS EC2 with a RESTful FastAPI endpoint

---

## 🚀 Future Enhancements

* Integrate **eye-tracking** for precise focus estimation
* Expand API for **cross-platform EdTech integration**
* Enhance **body language interpretation** (pose estimation)
* Add **gamified attentiveness training**
* Deploy lightweight mobile/AR version


