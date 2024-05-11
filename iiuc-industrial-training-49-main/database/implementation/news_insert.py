import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

def create_db_connection():
    """
    Create a database connection to the MySQL database specified by the db_name.

    Returns
    -------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    """
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            passwd=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME")
        )
        print("MySQL Database connection successful")
        return connection
    except Error as e:
        print(f"The error '{e}' occurred")
        return None

def execute_query(connection, query, data=None):
    """
    Execute a given SQL query on the provided database connection.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    query : str
        The SQL query to execute.
    data : tuple, optional
        The data tuple to pass to the query, for parameterized queries.

    Returns
    -------
    None
    """
    cursor = connection.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_category(connection, name, description):
    """
    Inserts a new category into the categories table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    name : str
        The name of the category.
    description : str
        The description of the category.

    Returns
    -------
    None
    """
    query = """
    INSERT INTO categories (name, description)
    VALUES (%s, %s)
    """
    data = (name, description)
    execute_query(connection, query, data)

def insert_author(connection, name, email):
    """
    Inserts a new author into the authors table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    name : str
        The name of the author.
    email : str
        The email of the author.

    Returns
    -------
    None
    """
    query = """
    INSERT INTO authors (name, email)
    VALUES (%s, %s)
    """
    data = (name, email)
    execute_query(connection, query, data)

def insert_editor(connection, name, email):
    """
    Inserts a new editor into the editors table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    name : str
        The name of the editor.
    email : str
        The email of the editor.

    Returns
    -------
    None
    """
    query = """
    INSERT INTO editors (name, email)
    VALUES (%s, %s)
    """
    data = (name, email)
    execute_query(connection, query, data)

def insert_news(connection, category_id, author_id, editor_id, datetime, title, body, link):
    """
    Inserts a new news article into the news table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    category_id : int
        The ID of the category.
    author_id : int
        The ID of the author.
    editor_id : int
        The ID of the editor.
    datetime : datetime
        The publication date and time of the news article.
    title : str
        The title of the news article.
    body : str
        The body text of the news article.
    link : str
        The URL link to the full news article.

    Returns
    -------
    None
    """
    query = """
    INSERT INTO news (category_id, author_id, editor_id, datetime, title, body, link)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    data = (category_id, author_id, editor_id, datetime, title, body, link)
    execute_query(connection, query, data)

def insert_image(connection, news_id, image_url):
    """
    Inserts a new image into the images table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    news_id : int
        The ID of the news article associated with the image.
    image_url : str
        The URL of the image.

    Returns
    -------
    None
    """
    query = """
    INSERT INTO images (news_id, image_url)
    VALUES (%s, %s)
    """
    data = (news_id, image_url)
    execute_query(connection, query, data)

def insert_summary(connection, news_id, summary_text):
    """
    Inserts a new summary into the summaries table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    news_id : int
        The ID of the news article associated with the summary.
    summary_text : str
        The text of the summary.

    Returns
    -------
    None
    """
    query = """
    INSERT INTO summaries (news_id, summary_text)
    VALUES (%s, %s)
    """
    data = (news_id, summary_text)
    execute_query(connection, query, data)

# Example usage
if __name__ == "__main__":
    conn = create_db_connection()
    if conn is not None:
        insert_category(conn, "Politics", "All news related to politics")
        insert_category(conn, "Weather", "All news related to weather")
        insert_category(conn, "Entertainment", "All news related to Entertainment")
        insert_category(conn, "Sports", "All news related to Sports")



        insert_author(conn, "John Doe", "john@gmail.com")
        insert_author(conn, "Alice Brown", "alice@gmail.com")
        insert_author(conn, "Bob Marley", "bob.m@yahoo.com")
        insert_author(conn, "Selina Gomez", "s_gomez@gmail.com")


        insert_editor(conn,"Maria B", "maria@gmail.com" )
        insert_editor(conn,"Stacey Hollan", "stacey_h@gmail.com" )
        insert_editor(conn,"Justin Mark", "justin@hotmail.com" )
        insert_editor(conn,"Christina Red", "chris_r@gmail.com" )
        

        insert_news(conn, "1","1","3", "2024-05-08 20:00","A former governors unpleasant truths about the banking sector",
                    """Economists are always noted for telling unpleasant truths because they go by numbers, 
                    research, theory, and judgement. Rarely do politicians—who can manufacture arguments to 
                    suit their purpose—endorse economists who are objective. """, 
                    "https://www.thedailystar.net/opinion/views/news/former-governors-unpleasant-truths-about-the-banking-sector-3605066")
        



        insert_news(conn, "2","3","2", "2024-05-08 13:02","Rain likely in all divisions: Met office",
                    """#Rain and thundershowers, accompanied by temporary gusty or squally wind, is likely to occur at many places over Rangpur, Rajshahi, Dhaka, Khulna, Barishal and Chattogram divisions and 
                    at a few places over Mymensingh and Sylhet divisions, 
                    the forecast said. """, 
                    "https://www.thedailystar.net/environment/weather/news/rain-likely-all-divisions-met-office-3604836")
        

        insert_news(conn, "3","2","4", "2024-05-08 20:04","Robert Downey Jr set for Broadway debut in new play 'McNeal'",
                    """#Hollywood superstar Robert Downey Jr is all set to play the role of Jacob McNeal in the upcoming play 'McNeal', penned by Ayad Akhtar and helmed by Bartlett Sher ("To Kill a Mockingbird"). 
                    The play is about a gifted author grappling with familial challenges while working on his latest novel. """, 
                    "https://www.thedailystar.net/entertainment/tv-film/news/robert-downey-jr-set-broadway-debut-new-play-mcneal-3605116")
        


        
        insert_news(conn, "4","4","1", "2024-05-08 23:29","Head, Abishek power Hyderabad to victory over Lucknow inside 10 overs",
                    """Openers Travis Head and Abhishek Sharma smoked half-centuries as Sunrisers Hyderabad crushed Lucknow Super Giants by 10 wickets on Wednesday 
                    to boost their play-off hopes in the IPL.""", 
                    "https://www.thedailystar.net/sports/cricket/news/head-abishek-power-hyderabad-victory-over-lucknow-inside-10-overs-3605301")
        
        



        insert_image(conn, "1","https://tds-images.thedailystar.net/sites/default/files/styles/big_202/public/media/api_images/2024/05/08/ED%201%20-%20A%20former%20governors%20unpleasant%20truths%20and%20the%20cancerous%20future%20of%20banking.jpg")   
        insert_image(conn, "2","https://tds-images.thedailystar.net/sites/default/files/styles/big_202/public/images/2024/05/08/rain_3.jpg")
        insert_image(conn,"3","https://tds-images.thedailystar.net/sites/default/files/styles/big_202/public/images/2024/05/08/robert_downey_jr-t2.jpg")
        insert_image(conn,"4", "https://tds-images.thedailystar.net/sites/default/files/styles/big_202/public/images/2024/05/08/afp_20240508_34r89pa_v1_preview_cricketindiplt20hyderabadlucknow.jpg")

        

        insert_summary(conn,"1","This must be stopped for the sake of the nation where income inequality has been on an unbroken crescendo of unsustainability, defying any sensible records of peer nations. Putting a farmer in jail for defaulting on loans by Tk 1,000, while letting a bank looter sit beside government officials, signal a cancerous future for the financial industry, and Farashuddin's artistic portrayal of the injustice and asymmetry in this regard warrants serious attention from the government.")
        insert_summary(conn,"2","'Day temperature may fall slightly and night temperature may remain nearly unchanged over the country,' said a weather bulletin issued this morning.The country's maximum temperature yesterday was recorded at 35 degrees Celsius at Khepupara in Patuakhali, and the minimum temperature today was 20 degrees Celsius at Hatiya in Noakhali.")
        insert_summary(conn,"3","His directorial prowess extends beyond Lincoln Center, with notable contributions to Broadway and the West End, including 'Pictures From Home', 'The Bridges of Madison County', and 'Fiddler on the Roof'.")

        insert_summary(conn,"4","Lucknow lost regular wickets until Nicholas Pooran, who hit 48, and Ayush Badoni, who smashed 55, put on an unbeaten stand of 99 in 52 balls to boost the team total.But the score proved too little against a team which posted record totals of 277 and 287 in this high-scoring edition of the T20 tournament.")

        # Add more insert calls for other tables
