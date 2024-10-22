
# Old Phone Price Prediction Project

## Description
This project aims to build a model for predicting the prices of old phones based on information such as phone name, RAM size, ROM size, and other technical specifications. Data is collected from e-commerce websites, cleaned, and standardized before being used in the prediction model.

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - **Web Scraping**: Selenium, WebDriver Manager, BeautifulSoup, Requests, PyAutoGUI
  - **Data Processing**: Pandas, NumPy
  - **Machine Learning**: Scikit-learn, XGBoost, LightGBM
  - **Database Connection**: PyODBC
  - **Visualization**: Matplotlib, Seaborn
- **Development Environment**: Jupyter Notebook

## Data
- **Data Source**: Data is scraped from e-commerce websites.
- **Data Columns**: 
  - `phonename`: Phone name
  - `price`: Phone price (can be missing)
  - `ram`: RAM size (can be missing)
  - `rom`: ROM size (can be missing)
  - `brand`: Phone brand
  - `release_year`: Year of phone release
  - `camera`: Camera specifications
  - `battery`: Battery capacity
  - `condition`: Phone condition (new, used, refurbished)
  - `rating`: Customer ratings (if available)
  - `storage`: Total internal storage (can be missing)

## Steps to Implement
1. **Scrape data**: Collect data from e-commerce websites.
2. **Preprocess data**: Clean data, handle missing values, and normalize the data.
3. **Data analysis**: Perform data analysis to identify factors influencing phone prices.
4. **Build model**: Use machine learning algorithms like Linear Regression, Random Forest, or XGBoost to predict prices.
5. **Evaluate model**: Measure the accuracy of the model and optimize it for the best performance.

## Installation

### Step 1: Clone the repository
   ```bash
   git clone https://github.com/manhmitcf/Used_Phone_Price_Prediction.git
   ```

### Step 2: Create `requirements.txt`
Create a file named `requirements.txt` with the following content:

```txt
# Web Scraping
selenium==4.10.0
webdriver-manager==4.0.0
beautifulsoup4==4.12.0
requests==2.31.0
pyautogui==0.9.53

# Data Processing
pandas==2.0.3
numpy==1.25.2

# Database connection (ODBC)
pyodbc==4.0.34

# Machine Learning Frameworks
scikit-learn==1.3.0
xgboost==1.7.6
lightgbm==3.3.5

# Other utilities
re  # included in Python standard library, no need to install
time  # included in Python standard library
```

### Step 3: Install dependencies
To install all necessary libraries, run:

```bash
pip install -r requirements.txt
```

### Step 4: Run the project
- Open `Jupyter Notebook` and run the file `phone_price_prediction.ipynb`.
- Follow the steps outlined in the notebook.

## Results
- Charts analyzing the relationships between technical specifications and phone prices.
- A price prediction model with high accuracy.
- A set of sample predicted prices for phones without price information.

## Contributions
If you want to contribute to the project, please create a pull request or open an issue to discuss new improvements.

## License
This project is released under the MIT License.
