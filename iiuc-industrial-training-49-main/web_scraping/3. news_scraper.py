from requests_html import HTMLSession

def single_news(url):
    session = HTMLSession()
    try:
        response = session.get(url)
        
        title = response.html.find('h1', first=True).text
        print(title)
        
        links = response.html.find('a')
        for link in links:
            print(link)
           
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()


single_news("https://www.prothomalo.com/bangladesh/capital/r8iju3rrq7")
