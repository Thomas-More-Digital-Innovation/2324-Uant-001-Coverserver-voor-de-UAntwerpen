import sqlite3
import urllib.request
import os

# Pad naar de database file
conn = sqlite3.connect(
    r'C:\Users\Natha\OneDrive - Thomas More\vakken\jaar2\Digital Innovation\3 Uant Coverserver\cover.sqlite3')
cursor = conn.cursor()

# locatie gescrapete covers
path_goede_covers = r"C:\goede_covers"

# goede covers query
goede_covers_query = """
SELECT 
    JSON_EXTRACT(changes, '$.new_cover_url') AS new_cover_url
FROM 
    cover_covernumberlog
WHERE 
	JSON_EXTRACT(changes, '$.new_cover_url') IS NOT NULL
    AND JSON_EXTRACT(changes, '$.new_cover_url') NOT LIKE '%cipal%'
LIMIT 100;
"""
cursor.execute(goede_covers_query)
goede_covers = cursor.fetchall()
print(f"Dit zijn de goede covers: {goede_covers}")

conn.close()


def downloadimages(covers, path):
    i = 1
    for cover in covers:
        url = cover[0]  # Extract de URL van de tuple
        file_name = f"{i}.jpg"
        full_path = os.path.join(path, file_name)

        try:
            urllib.request.urlretrieve(url, full_path)
            print(f"Downloaded image {i}: {url}")
        except urllib.error.HTTPError as error:
            if error.code == 410:
                print(f"Image {i} is no longer available: {url}")
            else:
                print(f"Error downloading image {i}: {url}")
                print(f"Error details: {error}")
        i += 1


downloadimages(goede_covers, path_goede_covers)
