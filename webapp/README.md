# NFL Analytics Web App

Placeholder for the future web application that will make NFL insights publicly viewable.

## Future Framework Options

Consider these when ready to build:

- **Streamlit** - Quick dashboards, minimal setup
- **FastAPI + React** - More flexible, production-ready
- **Django** - Full-featured, if you need user accounts/admin
- **Flask** - Lightweight, simple

## Structure Ideas

```
webapp/
├── app/           # Main application code
├── templates/     # HTML templates  
├── static/        # CSS, JS, images
├── api/           # API endpoints
└── requirements.txt
```

## Data Connection

Will connect to the same DuckDB database that the analysis notebooks use, ensuring consistency across the project.