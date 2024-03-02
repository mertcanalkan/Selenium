from twitter_bot import TwitterBot

def main():
    print("scraping.py çalışıyor")
    login_username = input("Twitter kullanıcı adınızı girin: ")
    login_password = input("Twitter şifrenizi girin: ")

    bot = TwitterBot(login_username, login_password)
    bot.login()

    search_option = input("Kullanıcı adına göre arama yapmak için y, konu başlığına göre arama yapmak için n'ye basın ! (y/n): ").lower()
    
    if search_option == 'y':
        username = input("Aramak istediğiniz kullanıcının adını girin: ")
        bot.search_user_by_username(username)
    elif search_option == 'n':
        topic = input("Aramak istediğiniz konu başlığını girin: ")
        bot.search_tweets_by_topic(topic)
    else:
        print("Geçersiz seçenek. Lütfen 'y' veya 'n' girin.")
    
    bot.logout()

if __name__ == "__main__":
    main()
