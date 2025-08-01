# Recipe Maker Agent using LangGraph

A conversational AI application that suggests dinner recipes based on user input using LangGraph for workflow orchestration and Groq for fast LLM inference.

## 🍽️ Features

- 🤖 **AI-Powered Recipe Suggestions**: Get personalized dinner ideas based on ingredients or mood
- 🔄 **LangGraph Workflow**: Structured conversation flow with state management
- ⚡ **Fast Inference**: Uses Groq's high-performance LLM API
- 💬 **Interactive Web Interface**: Clean Streamlit-based user interface
- 🎯 **Context-Aware**: Considers user preferences and available ingredients

## 🏗️ Project Structure

```
ReceipeMaker_Agent_using_LangGraph/
├── src/
│   ├── routers/
│   │   └── router.py          # Streamlit web interface
│   └── services/
│       ├── graph.py           # LangGraph workflow definition
│       └── service1.py        # Main service layer
├── data/                      # Data storage (currently empty)
├── database/                  # Database storage (currently empty)
├── main.py                    # Application entry point
├── requirements.txt           # Python dependencies
└── README.md                 # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Groq API key (get it from [Groq Console](https://console.groq.com/))

### Installation

1. **Clone and navigate to the project:**
   ```bash
   cd ReceipeMaker_Agent_using_LangGraph
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Create a `.env` file in the project root
   - Add your Groq API key:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```

4. **Run the application:**
   ```bash
   python main.py
   ```

5. **Open your browser** and go to the URL shown in the terminal (usually `http://localhost:8501`)

## 🎯 How to Use

1. **Enter your preferences** in the text input field:
   - Available ingredients (e.g., "chicken, rice, vegetables")
   - Mood or cuisine preference (e.g., "I want something spicy")
   - Dietary restrictions (e.g., "vegetarian, gluten-free")

2. **Click "Get Dinner Idea"** to receive AI-generated recipe suggestions

3. **Get personalized recommendations** based on your input

## 🧠 How It Works

### Architecture Overview

The application uses a **LangGraph workflow** with the following components:

1. **User Interface Layer** (`src/routers/router.py`)
   - Streamlit web interface
   - Handles user input and displays results

2. **Service Layer** (`src/services/service1.py`)
   - Orchestrates the LangGraph workflow
   - Manages data flow between components

3. **Graph Workflow** (`src/services/graph.py`)
   - Defines the conversation flow using LangGraph
   - State management with `GraphState`
   - LLM integration with Groq

### Workflow Process

```
User Input → LangGraph State → LLM Processing → Recipe Suggestion → Display
```

1. **Input Processing**: User text is captured and passed to the graph
2. **State Management**: LangGraph maintains conversation state
3. **LLM Processing**: Groq LLM generates recipe suggestions
4. **Response Generation**: Structured response is returned
5. **Display**: Results are shown in the web interface

### State Schema

```python
class GraphState(TypedDict):
    input: str      # User's original input
    suggestion: str  # Generated recipe suggestion
```

## 📦 Dependencies

- **`streamlit`** - Web application framework
- **`langchain`** - LLM orchestration framework
- **`langgraph`** - Workflow and state management
- **`langchain-groq`** - Groq LLM integration
- **`langchain-community`** - Community integrations
- **`langchain-core`** - Core LangChain functionality
- **`python-dotenv`** - Environment variable management
- **`typing-extensions`** - Type hints support
- **`pydantic`** - Data validation

## 🔧 Technologies Used

- **LangGraph**: Workflow orchestration and state management
- **LangChain**: LLM framework and prompt management
- **Groq**: High-performance LLM inference
- **Streamlit**: Interactive web interface
- **Python TypedDict**: Type-safe state management

## 🎨 Key Features

### LangGraph Integration
- **Stateful Conversations**: Maintains context across interactions
- **Workflow Orchestration**: Structured processing pipeline
- **Extensible Architecture**: Easy to add new nodes and edges

### AI-Powered Suggestions
- **Context-Aware**: Considers user preferences and constraints
- **Creative Recipes**: Generates unique and personalized suggestions
- **Fast Response**: Leverages Groq's optimized inference

### User Experience
- **Simple Interface**: Clean, intuitive web UI
- **Real-time Processing**: Immediate feedback with loading indicators
- **Error Handling**: Graceful handling of edge cases

## 🔮 Future Enhancements

- **Recipe Database Integration**: Store and retrieve saved recipes
- **Multi-step Conversations**: Complex recipe planning workflows
- **Image Generation**: Visual recipe representations
- **Nutritional Information**: Calorie and macro tracking
- **Shopping Lists**: Automatic ingredient lists
- **User Preferences**: Personalized recipe recommendations

## 📝 Configuration

### Environment Variables

Create a `.env` file with:
```
GROQ_API_KEY=your_groq_api_key_here
```

### Model Configuration

The application uses:
- **Model**: `llama3-8b-8192`
- **Temperature**: `0.7` (balanced creativity)
- **Provider**: Groq (fast inference)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is part of the AI-ML-Internship-Eminds-feature-initial-setup.

## ⚠️ Notes

- Ensure you have sufficient Groq API credits
- The application requires an active internet connection
- Recipe suggestions are AI-generated and should be verified before cooking
- Consider dietary restrictions and allergies when following suggestions 