from feed_reader import fetch_news
from classifier import classify_news
#from user_db import get_users
#from openai_formatter import format_news
#from email_sender import send_email


def admin_listClassifiedNotices(news_data):
    classified = classify_news(news_data)
    genders = classified.keys()
    
    for gender in genders:
        print(f"\nNoticias do genero {gender}")

        cont = 1
        noticias = classified[gender]

        if (not noticias):
            print("   Não há noticias desse gênero")

        for noticia in noticias:
            print(f"   {cont}. {noticia.title}")
            cont += 1

        input("enter para prosseguir")

def admin_listAllNotices(news_data):
    sites = news_data.keys()

    for site in sites:
        print(f"\n\nSITE: {site}\n\n"
                "Titulo das noticias:")
        
        cont = 1
        noticias = news_data[site]

        for noticia in noticias:
            print(f"{cont}. {noticia.title}")
            cont += 1

        input("enter para prosseguir")

def admin_listAllUsers():
    pass

def main():
    print("Buscando noticias...")
    news_data = fetch_news()

    print("Classificando noticias...")
    admin_listClassifiedNotices(news_data)

    print("Agrupando noticias...")
    admin_listAllNotices(news_data)




#    print("🔄 Buscando notícias...")
#    news_data = fetch_news()
    
#    print("🧠 Classificando notícias...")
#    classified = classify_news(news_data)
    
#    users = get_users()
#    for user in users:
#        genre = user['preference']
#        if not classified[genre]:
#            print(f"⚠️ Nenhuma notícia para {genre} hoje.")
#            continue
#        entry = random.choice(classified[genre])
#        summary = format_news(entry)

#        email_body = f"""
#Olá {user['email']},

#Aqui está uma notícia sobre {genre} que pode te interessar:

#Título: {entry.title}
#Link: {entry.link}

#Resumo:
#{summary}

#Abraços,
#Seu bot de notícias
#        """

#        print(f"📨 Enviando email para {user['email']}...")
#        send_email(user['email'], f"📰 Sua notícia diária de {genre}", email_body)

if __name__ == "__main__":
    main()
