import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class TwitterBot:
    def __init__(self, login_username, login_password):
        self.login_username = login_username
        self.login_password = login_password
        self.driver = webdriver.Firefox()

    def login(self):
        try:
            self.driver.get("https://twitter.com")
            time.sleep(2)
            if self.driver.current_url == "https://twitter.com/home":
                    print("Zaten giriş yapılmış.")
                    return
            self.driver.get("https://twitter.com/login")
            username_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@name='text']")))
            username_input.send_keys(self.login_username)

            next_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Next')]")))
            next_button.click()

            password_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
            password_input.send_keys(self.login_password)

            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Log in')]")))
            login_button.click()

            print("Twitter'a başarıyla giriş yapıldı.")

        except Exception as e:
            print("Twitter'a giriş yapma işlemi başarısız oldu:", e)

    def logout(self):
        try:
            confirm = input("Twitter'dan çıkış yapmak istediğinizden emin misiniz? (c/E): ").lower()
            if confirm == 'c':
                self.driver.quit()
                print("Twitter'dan başarıyla çıkış yapıldı.")
            else:
                print("Çıkış işlemi iptal edildi.")

        except Exception as e:
            print("Twitter'dan çıkış yapma işlemi başarısız oldu:", e)

    def search_tweets_by_topic(self, topic):
        try:
            search_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Search query']")))
            search_box.send_keys(topic)
            search_box.send_keys(Keys.RETURN)
        
        except Exception as e:
            print("Tweet çekme işlemi başarısız oldu:", e)
    
    def search_user_by_username(self, username):
        try:
            profile_url = f"https://twitter.com/{username}"

            self.driver.get(profile_url)

            print(f"{username} kullanıcısının profil sayfası başarıyla bulundu.")
    
        except Exception as e:
            print("Kullanıcı profilini bulma işlemi başarısız oldu:", e)

    def compose_tweet(self, tweet_text):
        try:
            self.driver.get("https://twitter.com/compose/tweet")
            tweet_text_box = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div")))
            tweet_text_box.send_keys(tweet_text)

            send_tweet_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Post')]")))
            send_tweet_button.click()

            print("Tweet başarıyla gönderildi.")

        except Exception as e:
            print("Tweet gönderme işlemi başarısız oldu:", e)

    def __del__(self):
        self.driver.quit()
