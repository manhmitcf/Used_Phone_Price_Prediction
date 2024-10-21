import time as tm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains

# Initialize data storage
products_data = []
all_hardware_titles = set()  # To track all hardware titles across products

# Set Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')

# Automatically download and use the correct version of chromedriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Access the webpage
url = 'https://fptshop.com.vn/may-doi-tra/dien-thoai-cu-gia-re'
driver.get(url)

# Load and click "Xem thêm" until all products are displayed
tm.sleep(3)
while True:
        try:
            tm.sleep(1)
            # Tìm nút "Xem thêm"
            button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="Button_root__LQsbl Button_btnSmall__aXxTy Button_whitePrimary__nkoMI Button_btnIconRight__4VSUO border border-iconDividerOnWhite px-4 py-2"]')))
            # Cuộn đến nút
            ActionChains(driver).move_to_element(button).perform()
            # Nhấn nút
            button.click()
            tm.sleep(3)
            print("Click 'Xem thêm' DONE")
            
        except Exception as e:
            print("Không tìm thấy nút 'Xem thêm' hoặc đã tải hết sản phẩm")
            break  # Thêm câu lệnh break để thoát khỏi vòng lặp khi không còn nút


# Find product URLs
products = driver.find_elements(By.XPATH, '//div[@class="ProductCard_cardInfo__r8zG4"]/h3/a')
product_urls = [product.get_attribute('href') for product in products]

# Loop through each product URL to scrape details
for url1 in product_urls:
    driver.get(url1)
    tm.sleep(3)

    try:
        product_name = driver.find_element(By.XPATH, '//div[@class="w-full pc:w-[507px]"]/div/div/h1').text.strip()
        price = driver.find_element(By.XPATH, '//div[@class="flex flex-col"]/p').text
        location = driver.find_element(By.XPATH, '//span[@class="text-nowrap"]').text
        new_price = driver.find_element(By.XPATH, '//div[@class="flex flex-1 items-center gap-3"]/div/p[2]').text
        warranty = driver.find_element(By.XPATH, '//span[contains(text(),"Thời gian bảo hành")]/following-sibling::span').text.strip()
        condition = driver.find_element(By.XPATH, '//span[contains(text(),"Tình trạng sản phẩm")]/following-sibling::span').text.strip()
    except NoSuchElementException:
        new_price, location, warranty, condition = "Not available", "Not available", "Not available", "Not available"

    # Scrape hardware details
    try:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@class="flex items-center text-blue-blue-7 b2-medium"]'))
        )
        # Cuộn đến nút và nhấn
        ActionChains(driver).move_to_element(button).perform()
        button.click()
        tm.sleep(3)
        print("Click 'Xem thêm' DONE")
    except:
        pass


    # Extracting specification data
    title=[]
    detail=[]
    try:
        sections = driver.find_elements(By.XPATH, '//div[@class="flex gap-2 border-b border-dashed border-b-iconDividerOnWhite py-1.5"]')
        for section in sections:
            label = section.find_element(By.XPATH, './div[@class="w-2/5 text-textOnWhiteSecondary b2-regular"]').text.strip()
            value = section.find_element(By.XPATH, './div[@class="flex flex-1 flex-col py-0.5"] | ./span').text.strip()
            title.append(label)
            detail.append(value)
    except Exception as e:
        print(f"Error occurred: {e}")
def save_to_csv(data, feature_names):
    df = pd.DataFrame(data, columns=feature_names)
    df.to_csv("products_Click_buy.csv", index=False, encoding='utf-8-sig')

def prepare_data(data_raw):
    data = {"Tên sản phẩm": data_raw[0], "Giá bán cũ": data_raw[1], "Giá mới": data_raw[2]}
    details = data_raw[3]
    titles = data_raw[4]
    for title, detail in zip(titles, details):
        data[title] = detail
    return data