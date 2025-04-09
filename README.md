🚀 Smart Meeting Assistant

🧠 An AI-powered assistant that helps automate meeting tasks like transcribing audio to text, summarizing discussions, and saving organized notes for future reference.

📁 Project Structure
- main.py : the entry point for running the application
- doc.py : handles text summarization functionality
- speech_to_text.py : converts meeting audio to text using speech recognition
- merge.py : merges multiple inputs into one document
- requirements.txt : contains all Python package dependencies
- web/ : folder for UI-related assets
- meet.wav : sample audio used for testing

💡 Features
- 🗣️ Speech-to-text conversion for meeting recordings
- ✍️ Auto-generated meeting summaries
- 📄 Document merge for clean and concise outputs
- 🌐 Basic web interface (planned or in progress)
- 💾 Saves outputs in structured text format

🧠 PageRank Usage
- PageRank is used to identify the most important sentences in the meeting transcript.
- Each sentence is treated as a node in a graph, with edges representing similarity.
- Sentences that are more central (referenced or related to many others) get a higher rank.
- The top-ranked sentences are selected to create a concise and meaningful summary.

🛠️ Technologies Used
- Python
- SpeechRecognition
- PyDub
- Transformers (for summarization using HuggingFace models)
- Streamlit or Flask (optional frontend)
- NLTK

📦 How to Install
- Clone the repository:
  - git clone https://github.com/shreya-mangade/Smart-Meeting-Assistant.git
- Navigate to the project folder:
  - cd Smart-Meeting-Assistant
- Create a virtual environment and activate it
- Install dependencies:
  - pip install -r requirements.txt

▶️ How to Use
- Place a .wav meeting file named meet.wav in the root directory
- Run main.py to start the assistant:
  - python main.py
- The assistant will:
  - Convert speech to text
  - Generate a summary
  - Save results to a file

✅ Future Enhancements
- Add user authentication and session saving
- Upload UI with drag & drop audio
- Real-time transcription during live calls
- Export options: PDF, Google Docs, Markdown
