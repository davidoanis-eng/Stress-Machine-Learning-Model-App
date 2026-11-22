# Stress Check

A small Flask web app for testing the saved text-classification model. Enter text in the browser to receive a prediction of `stressed` or `not stressed`.

The saved model is a scikit-learn pipeline that uses TF-IDF text features and logistic regression. This demo is for model testing only and is not a clinical assessment.

## Project files

- `app.py` — Flask application and prediction endpoint.
- `stress_model.pkl` — trained model loaded by the application.
- `templates/index.html` — web interface with inline CSS and JavaScript.
- `Stress.csv` — dataset used by the notebook.
- `stressmodel.ipynb` — model exploration and training notebook.

## Requirements

- Python
- The packages listed in `requirements.txt`

The model file must remain in the project root next to `app.py`.

## Install and run on Windows

Open PowerShell in the project directory. If `python` or `conda` is not recognized, use the full path to your Python executable. For example, with Anaconda installed at `C:\Users\hp\anaconda3`:

```powershell
& "C:\Users\hp\anaconda3\python.exe" -m pip install -r requirements.txt
& "C:\Users\hp\anaconda3\python.exe" .\app.py
```

Keep the terminal open while the server is running, then open <http://127.0.0.1:5000> in a browser. Stop the server with `Ctrl+C`.

## Prediction endpoint

`POST /predict` accepts form data with a `text` field and returns JSON:

```json
{"prediction": "stressed"}
```

An empty or whitespace-only `text` value returns HTTP 400 with a JSON error message.
