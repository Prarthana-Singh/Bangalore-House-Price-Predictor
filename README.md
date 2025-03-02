
# 🏠Bangalore House Price Prediction

## Live Demo
[Try Here](https://bangalore-house-price-predictor-8zg0.onrender.com)
## Project Overview
This project predicts house prices in Bangalore based on features such as location, square footage, number of bedrooms, and bathrooms. The model is built using **Linear Regression** and deployed with **Streamlit** for user-friendly interaction.

## Dataset
The dataset includes:
- **Location**
- **Total square feet**
- **BHK (Number of bedrooms)**
- **Bathrooms**
- **Price (Target variable)**

## Installation
Ensure you have the necessary dependencies installed:
```bash
pip install pandas numpy scikit-learn streamlit pickle-mixin
```

## Implementation Steps
1. **Data Preprocessing**: Handle missing values, remove outliers, and perform feature engineering.
2. **Model Training**: Train a Linear Regression model.
3. **Model Evaluation**: Evaluate the model using R² score.
4. **Deployment**: Deploy using Streamlit.

## How to Use the Repository
1. **Clone the repository**:
   ```bash
   git clone <repo-url>
   cd <repo-folder>
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application**:
   ```bash
   streamlit run app.py
   ```
4. **Interact with the application**:
   - Enter the total square feet, number of BHK, and bathrooms.
   - Click on **Predict Price** to get the estimated house price.

## Running the Application
To start the application, run the following command:
```bash
streamlit run app.py
```
Then, open the provided local URL in your browser.

## Demo Screenshots
![Screenshot 2025-03-03 020040](https://github.com/user-attachments/assets/a5c9b87a-d222-44db-9045-8068a5d0c958)
![Screenshot 2025-03-03 020055](https://github.com/user-attachments/assets/28fc5486-fec6-4f9d-9f62-9dc8412b1335)
![Screenshot 2025-03-03 020230](https://github.com/user-attachments/assets/0b9f0035-aa29-47f7-bdd4-2c52c6b811fc)



## Conclusion
This project successfully predicts Bangalore house prices using **Linear Regression** and deploys it with **Streamlit** for easy interaction. 🚀

