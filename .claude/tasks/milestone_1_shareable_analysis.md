# Milestone 1: Shareable One-Off Analysis

**Goal:** Deploy a single analysis to a public URL. Build reusable infrastructure for future analyses.

**User provides:** A Jupyter notebook with the analysis content (after infrastructure is deployed)

---

## Tasks

### 1. Project Setup
- [x] Create `app/` directory for Streamlit code
- [x] Set up `requirements.txt` with core dependencies (streamlit, pandas, plotly, etc.)
- [x] Create basic Streamlit app entry point (`app/main.py`) with placeholder content
- [x] Verify local Streamlit runs
- [x] Fix local Python environment (recreated .venv)

### 2. Deployment (Get Live First)
- [x] Create `.streamlit/config.toml` with any needed settings
- [x] Add `README.md` for the app (Streamlit Cloud needs this)
- [x] Ensure repo structure works with Streamlit Cloud
- [x] Deploy to Streamlit Cloud
- [x] Verify public URL works with placeholder content

### 3. Analysis Rendering Infrastructure
- [ ] Create `analyses/` directory structure for self-contained analyses
- [ ] Create a pattern for translating notebook analysis into Streamlit pages
- [ ] Build helper functions for common viz patterns (context bars, league comparisons, etc.)
- [x] **Decision:** Use static data files per analysis, not live database queries (for reliability/reproducibility)

### 4. First Analysis Page
- [ ] **BLOCKED: Waiting for user to provide/identify notebook**
- [ ] Export static data from notebook to `analyses/<name>/data/`
- [ ] Convert notebook content into Streamlit page in `app/pages/`
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
- Check existing notebooks in `explorations/` for patterns and data queries.

## Data Architecture

- `explorations/` - scratch/exploration notebooks
- `analyses/` - publishable analyses, self-contained with static data

Each publishable analysis:
```
analyses/
  <analysis-name>/
    notebook.ipynb      # Polished notebook
    data/               # Static data exported from notebook
app/
  pages/
    <analysis-name>.py  # Published Streamlit page, loads from analyses/<name>/data/
```

**Why static data:** Analyses are snapshots. No live database queries in Streamlit means:
- No database credentials needed in production
- Faster page loads
- Analysis still works if database changes
- Reproducible results

---

## Dependencies

- Existing data infrastructure in `data/` directory
- User input needed for Task 4 (which notebook/analysis to use)
