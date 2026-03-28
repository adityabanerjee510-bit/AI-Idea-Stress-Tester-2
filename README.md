# 🚀 AI Startup War Simulator

> Stress-test your startup idea before the real world does.

A multi-agent AI system that analyzes, attacks, and evaluates startup ideas from different real-world perspectives — helping founders identify risks, predict failures, and improve their ideas early.

---

## 🧠 About the Project

Most startup ideas fail not because they are bad, but because they are **never challenged properly**.

This project simulates a real-world environment where your idea is:

* Criticized
* Attacked
* Evaluated
* Improved

It combines multiple AI roles to produce a **comprehensive breakdown of your idea’s survival chances**.

---

## ✨ Key Features

* 🔍 **Idea Stress Testing**
  Detects weaknesses, risks, and feasibility issues.

* 💣 **AI Attack Engine**
  Simulates pressure from competitors, investors, customers, and threats.

* ⏳ **Failure Timeline Generator**
  Predicts how the idea may fail over time.

* 🧠 **Survival Strategy Generator**
  Suggests pivots, improvements, and better approaches.

* 📊 **Success Probability Score**
  Estimates the likelihood of success based on multiple factors.

* 🧑‍⚖️ **AI Jury Panel**
  Combines multiple perspectives (Investor, Engineer, User, Critic).

---

## 🏗️ Tech Stack

**Frontend**

* HTML, CSS, JavaScript
* Custom UI with animated canvas background

**Backend**

* FastAPI (Python)
* REST API architecture

**AI System**

* Multi-agent LLM pipeline
* Role-based prompt engineering
* Output aggregation via a “judge” model

**Database**

* JSON-based storage (current)
* MongoDB (planned)

---

## ⚙️ How It Works

```text
User Input → API Request → AI Agents → Aggregation → Response → UI Display
```

1. User submits a startup idea
2. Backend runs multiple AI agents:

   * Risk Analyst
   * Attack Simulator
   * Judge
3. Outputs are combined into a structured result
4. Frontend displays insights (score, risks, timeline, strategies)

---

## 🔌 API Endpoints

### `POST /analyze`

Analyzes a startup idea.

**Request Body**

```json
{
  "idea": "Your startup idea here"
}
```

**Response**

```json
{
  "risk_analysis": "...",
  "attack_analysis": "...",
  "final_result": "..."
}
```

---

## 🖥️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-startup-war-simulator.git
cd ai-startup-war-simulator
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add environment variables

Create a `.env` file:

```env
OPENROUTER_API_KEY_1=your_key
OPENROUTER_API_KEY_2=your_key
OPENROUTER_API_KEY_3=your_key
```

### 5. Run backend

```bash
uvicorn main:app --reload
```

### 6. Open frontend

Open `index.html` or `simulator.html` in your browser.

---

## 🚧 Current Limitations

* Responses may overlap across agents
* No persistent user history
* Basic authentication (in progress)
* AI cost optimization not implemented

---

## 🔮 Roadmap

* [ ] JWT Authentication
* [ ] User Dashboard
* [ ] Save & Track Ideas
* [ ] Graph-based Timeline Visualization
* [ ] Voice Input Support
* [ ] More Diverse AI Agents

---

## 🎯 Use Case

* Startup founders validating ideas
* Hackathon projects
* Product managers exploring concepts
* Students learning about business risk

---

## ⚠️ Disclaimer

This tool provides **analytical insights**, not guarantees.
Decisions should not rely solely on AI output.

---

## 👨‍💻 Author

Built as a hands-on project exploring:

* Multi-agent AI systems
* Startup validation workflows
* Practical product development

---

## ⭐ Final Thought

If your idea survives this system,
it has a better chance of surviving reality.
