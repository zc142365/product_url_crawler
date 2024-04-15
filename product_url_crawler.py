import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

opts = Options()
opts._binary_location = "chrome-win/chrome.exe"
svc = Service(executable_path="chrome-win/chromedriver.exe")

driver = webdriver.Chrome(service=svc, options=opts)
driver.maximize_window()

URL = 'https://www.dell.com/support/home/ko-kr'
driver.get(URL)

product_sel_btn = driver.find_element(By.CSS_SELECTOR, "#btn-homedashboard-browse-all-product")
product_sel_btn.click()

time.sleep(10)

c1 = 0
phProductUrl_list = []
sw1 = True

while True:
    try:
        if sw1:
            c1 += 1
            product_sel_btn2 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[1]/div[" + str(c1) + "]/a")
            product_sel_btn2.click()
            time.sleep(1)
        elif sw1==False:
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
                sw1 = False
                print("continue 작동")
                continue
        except:
            print("continue 작동 필요없음")
    except Exception as excep:
        print(excep)
        break
    try:
        productUrl = driver.find_element(By.CSS_SELECTOR, "#phProductUrl")
        phProductUrl_list.append(productUrl.get_attribute("href"))
    except Exception as excep:
        print(excep)
    
    c2 = 0

    while True:
        try:
            if sw1:
                c2 += 1
                product_sel_btn3 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/ul/li[" + str(c2) + "]/a")
                product_sel_btn3.click()
                time.sleep(1)
            elif sw1==False:
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
                    sw1 = False
                    print("continue 작동")
                    continue
            except:
                print("continue 작동 필요없음")
        except Exception as excep:
            print(excep)
            break

        try:
            productUrl = driver.find_element(By.CSS_SELECTOR, "#phProductUrl")
            phProductUrl_list.append(productUrl.get_attribute("href"))
        except Exception as excep:
            print(excep)
        
        c3 = 0
        while True:
            try:
                if sw1:
                    c3 += 1 
                    product_sel_btn4 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/ul/li[" + str(c3) + "]/a")
                    product_sel_btn4.click()
                    time.sleep(1)
                elif sw1==False:
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
                        sw1==False
                        print("continue 작동")
                        continue
                except:
                    print("continue 작동 필요없음")
                
            except Exception as excep:
                print(excep)
                break

            try:
                productUrl = driver.find_element(By.CSS_SELECTOR, "#phProductUrl")
                phProductUrl_list.append(productUrl.get_attribute("href"))
            except Exception as excep:
                print(excep)
            
            c4 = 0
            while True:
                try:
                    if sw1:
                        c4 += 1
                        product_sel_btn5 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[3]/div[2]/ul/li[" + str(c4) + "]/a")
                        product_sel_btn5.click()
                        time.sleep(1)
                    elif sw1==False:
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
                            sw1==False
                            print("continue 작동")
                            continue
                    except:
                        print("continue 작동 필요없음")
                    
                except Exception as excep:
                    print(excep)
                    break

                try:
                    productUrl = driver.find_element(By.CSS_SELECTOR, "#phProductUrl")
                    phProductUrl_list.append(productUrl.get_attribute("href"))
                except Exception as excep:
                    print(excep)
                
                c5 = 0
                while True:
                    try:
                        if sw1:
                            c5 += 1
                            product_sel_btn6 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[4]/div[2]/ul/li[" + str(c5) + "]/a")
                            product_sel_btn6.click()
                            time.sleep(1)
                        elif sw1==False:
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
                                sw1=False
                                print("continue 작동")
                                continue
                        except:
                            print("continue 작동 필요없음")
                        
                    except Exception as excep:
                        print(excep)
                        break

                    try:
                        productUrl = driver.find_element(By.CSS_SELECTOR, "#phProductUrl")
                        phProductUrl_list.append(productUrl.get_attribute("href"))
                    except Exception as excep:
                        print(excep)
                    
                    c6 = 0

                    while True:
                        try:
                            if sw1:
                                c6 += 1
                                product_sel_btn7 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[5]/div[2]/ul/li[" + str(c6) + "]/a")
                                product_sel_btn7.click()
                                time.sleep(1)
                            elif sw1==False:
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
                                    sw1=False
                                    print("continue 작동")
                                    continue
                            except:
                                print("continue 작동 필요없음")
                            
                        except Exception as excep:
                            print(excep)
                            break

                        try:
                            productUrl = driver.find_element(By.CSS_SELECTOR, "#phProductUrl")
                            phProductUrl_list.append(productUrl.get_attribute("href"))
                        except Exception as excep:
                            print(excep)
                        
                        c7 = 0

                        while True:
                            try:
                                if sw1:
                                    c7 += 1
                                    product_sel_btn8 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[5]/div/div/div/div/div/div[1]/span[4]/div/div/div/div/div[2]/div[2]/div[1]/div[6]/div[2]/ul/li[" + str(c7) + "]/a")
                                    product_sel_btn8.click()
                                    time.sleep(1)
                                elif sw1==False:
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
                                        sw1=False
                                        print("continue 작동")
                                        continue
                                except:
                                    print("continue 작동 필요없음")
                                
                            except Exception as excep:
                                print(excep)
                                break

                            try:
                                productUrl = driver.find_element(By.CSS_SELECTOR, "#phProductUrl")
                                phProductUrl_list.append(productUrl.get_attribute("href"))
                            except Exception as excep:
                                print(excep)

print(phProductUrl_list)