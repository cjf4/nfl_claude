# Milestone 1: Shareable One-Off Analysis

**Goal:** Deploy a single analysis to a public URL. Build reusable infrastructure for future analyses.

**User provides:** A Jupyter notebook with the analysis content (after infrastructure is deployed)

---

## Tasks

### 1. Project Setup
- [ ] Create `app/` directory for Streamlit code
- [ ] Set up `requirements.txt` with core dependencies (streamlit, pandas, plotly, etc.)
- [ ] Create basic Streamlit app entry point (`app/main.py`) with placeholder content
- [ ] Verify local Streamlit runs (`streamlit run app/main.py`)

### 2. Deployment (Get Live First)
- [ ] Create `.streamlit/config.toml` with any needed settings
- [ ] Add `README.md` for the app (Streamlit Cloud needs this)
- [ ] Ensure repo structure works with Streamlit Cloud
- [ ] Deploy to Streamlit Cloud
- [ ] Verify public URL works with placeholder content

### 3. Analysis Rendering Infrastructure
- [ ] Create a pattern for translating notebook analysis into Streamlit pages
- [ ] Build helper functions for common viz patterns (context bars, league comparisons, etc.)
- [ ] Set up data connection to existing database (DuckDB/SQLite from nflfastR)

### 4. First Analysis Page
- [ ] **BLOCKED: Waiting for user to provide/identify notebook**
- [ ] Convert notebook content into Streamlit page
- [ ] Add any needed narrative/context text
- [ ] Test locally, then push to deploy

### 5. Blog/Narrative Pattern (Optional for M1)
- [ ] Decide: separate blog, or analyses live in the app itself?
- [ ] If blog: set up minimal blog infrastructure (could be as simple as markdown files rendered in Streamlit)

---

## Notes for Agent

- Keep it simple. No auth, no database writes, no fancy features.
- Use Plotly for interactive charts (works well with Streamlit).
- User prefers Python/SQL, minimal JS.
- Context is key - every stat should explain "is this good or bad?"
- Check existing notebooks in `analysis/` for patterns and data queries.

---

## Dependencies

- Existing data infrastructure in `data/` directory
- User input needed for Task 4 (which notebook/analysis to use)
