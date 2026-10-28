# Signal Crew — Agentic Research Briefs

A compact multi-agent research app built with CrewAI. A search-enabled researcher assembles a linked evidence log; an editor turns it into an audience-specific brief with caveats and open questions.

## Requirements

- Python 3.10–3.13
- Google AI Studio API key for Gemini
- Serper API key for web search

## Setup

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Set `GOOGLE_API_KEY` and `SERPER_API_KEY` in your shell, then launch:

```bash
streamlit run app.py
```

Copy `.env.example` to `.env` only if you use a local environment loader; this project intentionally does not load `.env` automatically. Never commit real credentials.

## Workflow

```text
Question + audience → Search analyst (Serper) → Evidence log → Research editor → Linked Markdown brief
```

The editor receives the search agent's evidence as context, and is instructed not to invent references. Always open and verify citations independently: web results can be incomplete, stale, or misleading. Model output is a draft for review.

## Configuration

Set `CREWAI_MODEL` to a model identifier supported by your CrewAI installation and account. The default is `gemini/gemini-2.5-flash`. API use may incur provider charges under your own account.

## License

MIT. See [LICENSE](LICENSE).
