# 🎓 Neural Network Predicting Chances of Admission at UCLA

This project builds a machine learning application that predicts the chances of a student's admission to UCLA using a neural network. It includes data preprocessing, model training, evaluation, and a user-friendly Streamlit app for deployment.

---

## 📁 Project Structure

```
├── data/                 
    ├── Admission(in).csv
├── models/  
    ├──admission_nn_model.pkl              
├── src/                                 
│   ├── data_preprocessing.py
│   ├── evaluate_model.py
│   ├── train_model.py
│   └── visualize.py
├── app.py             
├── main.py 
├── README.md              
└── requirements.txt       
```

---

## 🚀 Features

- Data cleaning and preprocessing
- Neural network model training 
- Model evaluation  
- Streamlit app 
- Visualizations

---

## 🧠 Model Details

- **Algorithm**: Multi-layer Perceptron (MLP)
- **Libraries Used**:
  - `scikit-learn`
  - `pandas`, `numpy`
  - `matplotlib`, `seaborn`
  - `joblib`
  - `streamlit`

---

## 📊 Streamlit App

The app allows users to input their profile and predicts their chance of admission at UCLA.

To run:

```
[Streamlit App](https://ucla-admission-predictor-jafmzcfy32df8lnakqowsp.streamlit.app/)
```

---

## 🛠 How to Use

1. Clone the repository:

```bash
git clone https://github.com/allenecstadam/ucla-admission-predictor.git
cd ucla-admission-predictor
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the model training and evaluation:

```bash
python src/main.py
```

4. Launch the Streamlit app:

```bash
streamlit run app.py
```

---

## 📦 Requirements

See `requirements.txt` for full dependencies. Example contents:

```
streamlit
pandas
numpy
scikit-learn
matplotlib
seaborn
joblib
```

---

## 📌 Notes

- Ensure the model file (`model.pkl`) is saved inside the `models/` directory.
- Ensure `data/Admission.csv` exists or is uploaded via the Streamlit interface.
- The project is compatible with deployment on [Streamlit Cloud](https://streamlit.io/cloud).

---

## 📚 License

This project is open-source and free to use under the MIT License.

---

## 🙌 Author

Made with ❤️ by **Allen Adam**  
📍 [GitHub Profile](https://github.com/allenecstadam)
