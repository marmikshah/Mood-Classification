## Usage
Create a virtual environment
```bash
virtualenv -p python3 venv
```

Activate the virtual environment
```bash
source venv/bin/activate
```

Install requirements
```bash
pip install -r requirements.txt
```

Run Server (without specifying filename)
```bash
python app.py
```
Run Server (with filename)
```bash
python app.py -f file_path.csv
```



## Classifier Information - V1
* Model : **Support Vector Machine**
  * Training F1 : 0.997
  * Validation F1 : 0.712

* Method : TFIDF - Vectorizer 
  * Stopwords : English
  * N-Gram Range : (1,5)
  
