# Chatbot Pro SaaS

AI-powered chatbot dengan dukungan multi-format file dan vision capabilities.

## 🚀 Features

- **Multi-Model Support**: Llama 3.3 70B (text), Llama 4 Maverick (vision)
- **File Upload dengan RAG**: PDF, DOCX, CSV, XLSX, HTML, JSON, MD, TXT
- **Vision Analysis**: PNG, JPG, JPEG, GIF, WEBP
- **Message Editing**: Edit dan regenerate pesan sebelumnya
- **User Management**: Login, Register, Guest mode
- **Usage Limits**: Free (5/day) vs Premium (unlimited)
- **Custom System Prompt**: Personalisasi AI behavior

## 📦 Installation

```bash
pip install -r requirements.txt
pip install python-docx openpyxl
```

## 🔧 Configuration

Create `.streamlit/secrets.toml`:
```toml
GROQ_API_KEY = "your-api-key-here"
```

## 🏃 Run

```bash
streamlit run main.py
```

---

# Development Log (16 Jan 2026)

## Session Summary

### 🔄 Migration to Groq Native Client
- Migrated from OpenAI client wrapper to native `groq` library
- Updated `src/llm_engine.py` to use `from groq import Groq`
- Fixed streaming output: Added content generator wrapper for `st.write_stream`

### 🖼️ Vision Fixes
- **Data URI Format**: Fixed image payload to include `data:image/xxx;base64,...` prefix
- **Vision Detection**: Made robust by checking MIME type AND file extension
- **Vision Model Check**: Added `maverick`, `scout`, `llama-4` keywords for proper model detection
- **Image Support**: Expanded to include GIF and WEBP formats

### 📄 Multi-Format RAG Implementation
Added extraction functions and RAG for:
| Format | Function |
|--------|----------|
| PDF | `extract_text_from_pdf()` |
| DOCX | `extract_text_from_docx()` |
| CSV | `extract_text_from_csv()` |
| XLSX | `extract_text_from_xlsx()` |
| HTML | `extract_text_from_html()` |
| JSON | `extract_text_from_json()` |
| MD/TXT | Direct text read |

All text files use `get_smart_pdf_context()` for lightweight RAG:
- Takes first 2000 chars (intro)
- Finds paragraphs matching query keywords
- Limits to 10,000 chars total

### ✏️ Message Editing
- Added edit button (✏️) untuk setiap user message
- Edit dialog supports text + file replacement
- Regeneration updates message in-place (no duplication)

### 🐛 Bugs Fixed
1. Stream output showing raw `ChatCompletionChunk` objects
2. Vision model claiming "I can't see images"
3. `max_tok` check not recognizing Maverick as vision model
4. Image payload missing Data URI prefix
5. Vision detection relying only on MIME type
6. File uploader not accepting new formats
7. GIF/WEBP images not being processed

### 📁 Files Modified
- `main.py` (584 lines) - Main application
- `src/llm_engine.py` (82 lines) - LLM integration
- `src/utils.py` (120 lines) - File extraction utilities
- `src/database.py` (159 lines) - User/usage management

### ✅ Final Status
All bugs fixed. System production-ready.
