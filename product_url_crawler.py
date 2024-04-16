import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

opts = Options()
opts._binary_location = "D:/project/Win_x64_1134294_chrome-win/chrome-win/chrome.exe"
opts.add_experimental_option('prefs', {
"download.default_directory": "D:\\project\\product_url_crawler\\download", #Change default directory for downloads
"download.prompt_for_download": False, #To auto download the file
"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
})
svc = Service(executable_path="D:/project/Win_x64_1134294_chrome-win/chrome-win/chromedriver.exe")

driver = webdriver.Chrome(service=svc, options=opts)
driver.maximize_window()

URL = 'https://www.dell.com/support/home/ko-kr'
driver.get(URL)

time.sleep(10)

product_sel_btn = driver.find_element(By.CSS_SELECTOR, "#btn-homedashboard-browse-all-product")
product_sel_btn.click()

time.sleep(10)

c1 = 0

product_dict = {}
product_dict2 = {}
product_dict3 = {}
product_dict4 = {}

while True:
    try:
        c1 += 1
        product_sel_btn2 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[1]/div[" + str(c1) + "]/a")
        product_sel_btn2.click()
        time.sleep(1)

        try:
            product_error = driver.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[1]/div")
            if str(product_error.text)=="이 범주에는 제품이 없습니다. 다른 범주 또는 제품을 선택하시기 바랍니다.":
                product_error_button = driver.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[1]/button")
                product_error_button.click()
                time.sleep(2)
                product_sel_btn2 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[" + str(c1) + "]/a")
                product_sel_btn2.click()
                time.sleep(1)
                print("continue 작동")
                continue
        except:
            print("continue 작동 필요없음")
    except Exception as excep:
        print(excep)
        break
    try:
        productUrl = driver.find_element(By.CSS_SELECTOR, "#phProductUrl")
        product_name = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/ul/li[" + str(c2) + "]/a")
        
        if c1 == 1:
            product_dict[str(product_name.get_attribute("data-descr"))] = []
            product_dict[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))

        elif c1 == 2:
            product_dict2[str(product_name.get_attribute("data-descr"))] = []
            product_dict2[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))

        elif c1 == 3:
            product_dict3[str(product_name.get_attribute("data-descr"))] = []
            product_dict3[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))

        elif c1 == 4:
            product_dict4[str(product_name.get_attribute("data-descr"))] = []
            product_dict4[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))

    except Exception as excep:
        print(excep)
    
    c2 = 0

    while True:
        try:
            c2 += 1
            product_sel_btn3 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/ul/li[" + str(c2) + "]/a")
            product_sel_btn3.click()
            time.sleep(1)

            try:
                product_error = driver.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[1]/div")
                if str(product_error.text)=="이 범주에는 제품이 없습니다. 다른 범주 또는 제품을 선택하시기 바랍니다.":
                    product_error_button = driver.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[1]/button")
                    product_error_button.click()
                    time.sleep(2)
                    product_sel_btn2 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[" + str(c1) + "]/a")
                    product_sel_btn2.click()
                    time.sleep(1)
                    print("continue 작동")
                    continue
            except:
                print("continue 작동 필요없음")
        except Exception as excep:
            print(excep)
            break

        try:
            productUrl = driver.find_element(By.CSS_SELECTOR, "#phProductUrl")
            product_name = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/ul/li[" + str(c2) + "]/a")
            
            if c1 == 1:
                product_dict[str(product_name.get_attribute("data-descr"))] = []
                product_dict[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))

            elif c1 == 2:
                product_dict2[str(product_name.get_attribute("data-descr"))] = []
                product_dict2[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))

            elif c1 == 3:
                product_dict3[str(product_name.get_attribute("data-descr"))] = []
                product_dict3[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))

            elif c1 == 4:
                product_dict4[str(product_name.get_attribute("data-descr"))] = []
                product_dict4[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))


        except Exception as excep:
            print(excep)
        
        c3 = 0
        while True:
            try:
                c3 += 1 
                product_sel_btn4 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/ul/li[" + str(c3) + "]/a")
                product_sel_btn4.click()
                time.sleep(1)

                try:
                    product_error = driver.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[1]/div")
                    if str(product_error.text)=="이 범주에는 제품이 없습니다. 다른 범주 또는 제품을 선택하시기 바랍니다.":
                        product_error_button = driver.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[1]/button")
                        product_error_button.click()
                        time.sleep(2)
                        product_sel_btn2 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[" + str(c1) + "]/a")
                        product_sel_btn2.click()
                        time.sleep(1)
                        product_sel_btn3 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/ul/li[" + str(c2) + "]/a")
                        product_sel_btn3.click()
                        time.sleep(1)
                        print("continue 작동")
                        continue
                except:
                    print("continue 작동 필요없음")
                
            except Exception as excep:
                print(excep)
                break

            try:
                productUrl = driver.find_element(By.CSS_SELECTOR, "#phProductUrl")
                product_name = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/ul/li[" + str(c2) + "]/a")
                
                if c1 == 1:
                    product_dict[str(product_name.get_attribute("data-descr"))] = []
                    product_dict[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))

                elif c1 == 2:
                    product_dict2[str(product_name.get_attribute("data-descr"))] = []
                    product_dict2[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))

                elif c1 == 3:
                    product_dict3[str(product_name.get_attribute("data-descr"))] = []
                    product_dict3[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))

                elif c1 == 4:
                    product_dict4[str(product_name.get_attribute("data-descr"))] = []
                    product_dict4[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))

            except Exception as excep:
                print(excep)
            
            c4 = 0
            while True:
                try:
                    c4 += 1
                    product_sel_btn5 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[3]/div[2]/ul/li[" + str(c4) + "]/a")
                    product_sel_btn5.click()
                    time.sleep(1)
                    
                    try:
                        product_error = driver.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[1]/div")
                        if str(product_error.text)=="이 범주에는 제품이 없습니다. 다른 범주 또는 제품을 선택하시기 바랍니다.":
                            product_error_button = driver.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[1]/button")
                            product_error_button.click()
                            time.sleep(2)
                            product_sel_btn2 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[" + str(c1) + "]/a")
                            product_sel_btn2.click()
                            time.sleep(1)
                            product_sel_btn3 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/ul/li[" + str(c2) + "]/a")
                            product_sel_btn3.click()
                            time.sleep(1)
                            product_sel_btn4 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/ul/li[" + str(c3) + "]/a")
                            product_sel_btn4.click()
                            time.sleep(1)
                            print("continue 작동")
                            continue
                    except:
                        print("continue 작동 필요없음")
                    
                except Exception as excep:
                    print(excep)
                    break

                try:
                    productUrl = driver.find_element(By.CSS_SELECTOR, "#phProductUrl")
                    product_name = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/ul/li[" + str(c2) + "]/a")
                    
                    if c1 == 1:
                        product_dict[str(product_name.get_attribute("data-descr"))] = []
                        product_dict[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))

                    elif c1 == 2:
                        product_dict2[str(product_name.get_attribute("data-descr"))] = []
                        product_dict2[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))

                    elif c1 == 3:
                        product_dict3[str(product_name.get_attribute("data-descr"))] = []
                        product_dict3[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))

                    elif c1 == 4:
                        product_dict4[str(product_name.get_attribute("data-descr"))] = []
                        product_dict4[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))

                except Exception as excep:
                    print(excep)
                
                c5 = 0
                while True:
                    try:
                        c5 += 1
                        product_sel_btn6 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[4]/div[2]/ul/li[" + str(c5) + "]/a")
                        product_sel_btn6.click()
                        time.sleep(1)

                        try:
                            product_error = driver.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[1]/div")
                            if str(product_error.text)=="이 범주에는 제품이 없습니다. 다른 범주 또는 제품을 선택하시기 바랍니다.":
                                product_error_button = driver.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[1]/button")
                                product_error_button.click()
                                time.sleep(2)
                                product_sel_btn2 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[" + str(c1) + "]/a")
                                product_sel_btn2.click()
                                time.sleep(1)
                                product_sel_btn3 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/ul/li[" + str(c2) + "]/a")
                                product_sel_btn3.click()
                                time.sleep(1)
                                product_sel_btn4 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/ul/li[" + str(c3) + "]/a")
                                product_sel_btn4.click()
                                time.sleep(1)
                                product_sel_btn5 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[3]/div[2]/ul/li[" + str(c4) + "]/a")
                                product_sel_btn5.click()
                                time.sleep(1)
                                print("continue 작동")
                                continue
                        except:
                            print("continue 작동 필요없음")
                        
                    except Exception as excep:
                        print(excep)
                        break

                    try:
                        productUrl = driver.find_element(By.CSS_SELECTOR, "#phProductUrl")
                        product_name = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/ul/li[" + str(c2) + "]/a")
                        
                        if c1 == 1:
                            product_dict[str(product_name.get_attribute("data-descr"))] = []
                            product_dict[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))

                        elif c1 == 2:
                            product_dict2[str(product_name.get_attribute("data-descr"))] = []
                            product_dict2[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))

                        elif c1 == 3:
                            product_dict3[str(product_name.get_attribute("data-descr"))] = []
                            product_dict3[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))

                        elif c1 == 4:
                            product_dict4[str(product_name.get_attribute("data-descr"))] = []
                            product_dict4[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))
                    except Exception as excep:
                        print(excep)
                    
                    c6 = 0

                    while True:
                        try:
                            c6 += 1
                            product_sel_btn7 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[5]/div[2]/ul/li[" + str(c6) + "]/a")
                            product_sel_btn7.click()
                            time.sleep(1)

                            try:
                                product_error = driver.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[1]/div")
                                if str(product_error.text)=="이 범주에는 제품이 없습니다. 다른 범주 또는 제품을 선택하시기 바랍니다.":
                                    product_error_button = driver.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[1]/button")
                                    product_error_button.click()
                                    time.sleep(2)
                                    product_sel_btn2 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[" + str(c1) + "]/a")
                                    product_sel_btn2.click()
                                    time.sleep(1)
                                    product_sel_btn3 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/ul/li[" + str(c2) + "]/a")
                                    product_sel_btn3.click()
                                    time.sleep(1)
                                    product_sel_btn4 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/ul/li[" + str(c3) + "]/a")
                                    product_sel_btn4.click()
                                    time.sleep(1)
                                    product_sel_btn5 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[3]/div[2]/ul/li[" + str(c4) + "]/a")
                                    product_sel_btn5.click()
                                    time.sleep(1)
                                    product_sel_btn6 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[4]/div[2]/ul/li[" + str(c5) + "]/a")
                                    product_sel_btn6.click()
                                    time.sleep(1)
                                    print("continue 작동")
                                    continue
                            except:
                                print("continue 작동 필요없음")
                            
                        except Exception as excep:
                            print(excep)
                            break

                        try:
                            productUrl = driver.find_element(By.CSS_SELECTOR, "#phProductUrl")
                            product_name = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/ul/li[" + str(c2) + "]/a")
                            
                            if c1 == 1:
                                product_dict[str(product_name.get_attribute("data-descr"))] = []
                                product_dict[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))

                            elif c1 == 2:
                                product_dict2[str(product_name.get_attribute("data-descr"))] = []
                                product_dict2[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))

                            elif c1 == 3:
                                product_dict3[str(product_name.get_attribute("data-descr"))] = []
                                product_dict3[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))

                            elif c1 == 4:
                                product_dict4[str(product_name.get_attribute("data-descr"))] = []
                                product_dict4[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))
                        except Exception as excep:
                            print(excep)
                        
                        c7 = 0

                        while True:
                            try:
                                c7 += 1
                                product_sel_btn8 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[6]/div[2]/ul/li[" + str(c7) + "]/a")
                                product_sel_btn8.click()
                                time.sleep(1)
                                try:
                                    product_error = driver.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[1]/div")
                                    if str(product_error.text)=="이 범주에는 제품이 없습니다. 다른 범주 또는 제품을 선택하시기 바랍니다.":
                                        product_error_button = driver.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[1]/button")
                                        product_error_button.click()
                                        time.sleep(2)
                                        product_sel_btn2 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[" + str(c1) + "]/a")
                                        product_sel_btn2.click()
                                        time.sleep(1)
                                        product_sel_btn3 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/ul/li[" + str(c2) + "]/a")
                                        product_sel_btn3.click()
                                        time.sleep(1)
                                        product_sel_btn4 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/ul/li[" + str(c3) + "]/a")
                                        product_sel_btn4.click()
                                        time.sleep(1)
                                        product_sel_btn5 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[3]/div[2]/ul/li[" + str(c4) + "]/a")
                                        product_sel_btn5.click()
                                        time.sleep(1)
                                        product_sel_btn6 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[4]/div[2]/ul/li[" + str(c5) + "]/a")
                                        product_sel_btn6.click()
                                        time.sleep(1)
                                        product_sel_btn7 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[5]/div[2]/ul/li[" + str(c6) + "]/a")
                                        product_sel_btn7.click()
                                        time.sleep(1)
                                        print("continue 작동")
                                        continue
                                except:
                                    print("continue 작동 필요없음")
                                
                            except Exception as excep:
                                print(excep)
                                break

                            try:
                                productUrl = driver.find_element(By.CSS_SELECTOR, "#phProductUrl")
                                product_name = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/ul/li[" + str(c2) + "]/a")
                                
                                if c1 == 1:
                                    product_dict[str(product_name.get_attribute("data-descr"))] = []
                                    product_dict[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))

                                elif c1 == 2:
                                    product_dict2[str(product_name.get_attribute("data-descr"))] = []
                                    product_dict2[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))

                                elif c1 == 3:
                                    product_dict3[str(product_name.get_attribute("data-descr"))] = []
                                    product_dict3[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))

                                elif c1 == 4:
                                    product_dict4[str(product_name.get_attribute("data-descr"))] = []
                                    product_dict4[str(product_name.get_attribute("data-descr"))].append(str(productUrl.get_attribute("href")))
                            except Exception as excep:
                                print(excep)


