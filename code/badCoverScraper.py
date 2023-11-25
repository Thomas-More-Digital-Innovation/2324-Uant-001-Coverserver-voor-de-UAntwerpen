import sqlite3
import urllib.request
import os

# Pad naar de database file
conn = sqlite3.connect(
    r'C:\Users\Natha\OneDrive - Thomas More\vakken\jaar2\Digital Innovation\3 Uant Coverserver\cover.sqlite3')
cursor = conn.cursor()

# locatie gescrapete covers
path_slechte_covers = r"C:\slechte_covers"

# slechte covers uit log files
slechte_cover_query = """
SELECT 
    JSON_EXTRACT(changes, '$.prev_cover_url') AS prev_cover_url,
    cn.number,
	cn.number_type
FROM 
    cover_covernumberlog cl
	JOIN cover_covernumber cn ON cl.id = cn.id
WHERE 
	JSON_EXTRACT(changes, '$.prev_cover_url') IS NOT NULL
    AND JSON_EXTRACT(changes, '$.prev_cover_url') NOT LIKE '%cipal%'
LIMIT 100;
"""
cursor.execute(slechte_cover_query)
slechte_covers = cursor.fetchall()
print(f"Dit zijn de goede covers: {slechte_covers}")

conn.close()


def downloadimages(covers, path):
    for cover in covers:
        url = cover[0]  # Extract de URL van de tuple
        number = cover[1]
        type = cover[2]
        file_name = f"{type}{number}.jpg"
        full_path = os.path.join(path, file_name)

        try:
            urllib.request.urlretrieve(url, full_path)
            print(f"Downloaded image {file_name}: {url}")
        except urllib.error.HTTPError as error:
            if error.code == 410:
                print(f"Image {file_name} is no longer available: {url}")
            else:
                print(f"Error downloading image {file_name}: {url}")
                print(f"Error details: {error}")


downloadimages(slechte_covers, path_slechte_covers)
