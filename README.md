# SMS Spam Classifier

An end-to-end Machine Learning project that classifies SMS messages as **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP) techniques and a Multinomial Naive Bayes classifier. The project includes data preprocessing, feature extraction, model training, evaluation, and deployment through a Streamlit web application.

## Live Demo

Demo: https://sms-spam-classifier-vley.onrender.com

> Note: The application is hosted on Render's free tier. The first request may take 30–60 seconds to load if the service has been inactive.

## Features

* SMS Spam/Ham classification
* Text preprocessing using NLTK
* TF-IDF feature extraction
* Machine Learning model training and evaluation
* Real-time prediction through a Streamlit interface
* Interactive and user-friendly web application

## Dataset

**SMS Spam Collection Dataset**

* Approximately 5,500 labeled SMS messages
* Classes:

  * Spam
  * Ham (Legitimate Messages)

Dataset Source:
https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

## Project Workflow

1. Data Collection and Loading
2. Data Cleaning and Preprocessing
3. Text Normalization
4. Tokenization
5. Stop-word Removal
6. Feature Extraction using TF-IDF Vectorization
7. Model Training
8. Model Evaluation
9. Model Deployment using Streamlit

## Technologies Used

### Programming Language

* Python

### Libraries and Tools

* Scikit-learn
* Pandas
* NumPy
* NLTK
* Streamlit
* Jupyter Notebook

## Machine Learning Model

**Multinomial Naive Bayes**

The model was trained on TF-IDF transformed SMS messages and evaluated using a held-out test dataset.

## Performance Metrics

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 97.1% |
| Precision | 100%  |

### Confusion Matrix

|             | Predicted Ham | Predicted Spam |
| ----------- | ------------- | -------------- |
| Actual Ham  | 896           | 0              |
| Actual Spam | 30            | 108            |

The model achieved **100% precision**, meaning no legitimate SMS message was incorrectly classified as spam.

## Project Structure

```text
SMS-Spam-Classifier/
│
├── sms_spam_classifier.ipynb
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/pandeyAnjali491/SMS-Spam-Classifier.git
cd SMS-Spam-Classifier
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```
