# 🎵 AI-Powered Music Generator API

A simple FastAPI-based API that generates a basic music melody from a text prompt.
The API accepts a prompt and generates a small `.wav` audio file using Python tone synthesis.

This project demonstrates how text input can trigger automated music generation using lightweight logic.

---

# 🚀 Features

* FastAPI REST API
* Accepts text prompt
* Generates simple melody
* Outputs `.wav` audio file
* Lightweight implementation
* Easy to run locally

---

# 📁 Project Structure

```
ai-music-generator-api/

│
├── main.py                # FastAPI API server
├── music_generator.py     # Music generation logic
├── output/                # Generated audio files
│   └── generated_music.wav
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```
git clone https://github.com/yourusername/ai-music-generator-api.git
cd ai-music-generator-api
```

Install dependencies

```
pip install -r requirements.txt
```

Or manually install

```
pip install fastapi uvicorn numpy scipy
```

---

# ▶️ Run the API

Start the FastAPI server

```
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

# 📡 API Endpoint

### POST /generate-music

Generate a simple music melody based on text prompt.

---

## Request

```
POST /generate-music
Content-Type: application/json
```

Example request body:

```json
{
  "prompt": "happy birthday tune"
}
```

---

## Response

Example response:

```json
{
  "prompt": "happy birthday tune",
  "result": "output/generated_music.wav"
}
```

---

# 🎵 Generated Music Output

The API generates a `.wav` file and saves it inside the `output` folder.

Example output file:

```
output/generated_music.wav
```

You can open this file in any media player to listen to the generated melody.

---

# 🧪 Testing the API

You can test the API using:

* FastAPI Docs
  http://127.0.0.1:8000/docs

* Postman

* curl

Example curl command:

```
curl -X POST "http://127.0.0.1:8000/generate-music" \
-H "Content-Type: application/json" \
-d '{"prompt":"happy melody"}'
```

---

# 🧠 Music Generation Logic

The music is generated using:

* Predefined musical note frequencies
* Random melody generation
* Python sine wave tone synthesis
* `.wav` file generation

This keeps the implementation simple while demonstrating basic AI-driven music generation logic.

---

# 📦 Dependencies

* FastAPI
* Uvicorn
* NumPy
* SciPy

---

# 📌 Future Improvements (Optional)

* Prompt-based melody generation
* MIDI file generation
* Downloadable audio links
* Web UI for music generation
* AI model-based music generation

---

# 👨‍💻 Author

AI Music Generator API – Assessment Project
