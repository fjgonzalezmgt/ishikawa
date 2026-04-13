@echo off
cd /d "%~dp0"
conda run -n ishikawa streamlit run app.py
