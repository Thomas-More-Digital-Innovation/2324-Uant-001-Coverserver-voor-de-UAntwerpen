import sqlite3
import urllib.request
import os
import ssl

# Pad naar de database file
conn = sqlite3.connect(
    r'C:\Users\Natha\OneDrive - Thomas More\vakken\jaar2\Digital Innovation\3 Uant Coverserver\cover.sqlite3')
cursor = conn.cursor()

# locatie gescrapete covers
path_slechte_covers = r"C:\slechte_covers"

# slechte covers uit log files → aantal = 3065 → 3015 gedownload (50 niet werkende urls)
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
    AND JSON_EXTRACT(changes, '$.prev_cover_url') NOT LIKE '%cipal%';
"""
cursor.execute(slechte_cover_query)
slechte_covers = cursor.fetchall()
# print(f"Dit zijn de goede covers: {slechte_covers}")

conn.close()


def downloadimages(covers, path):
    for cover in covers:
        url = cover[0]  # Extract de URL van de tuple
        print(f"URL: {url}")  # debugging

        if not url:  # checken of de url leeg is
            print("Skipping empty URL")
            continue

        number = cover[1]
        type = cover[2]
        file_name = f"{type}{number}.jpg"
        full_path = os.path.join(path, file_name)

        try:
            # SSL context om verificatie te skippen
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE

            with urllib.request.urlopen(url, context=ssl_context) as response:
                with open(full_path, 'wb') as output_file:
                    output_file.write(response.read())

            print(f"Downloaded image {file_name}: {url}")

        except (urllib.error.HTTPError, urllib.error.URLError, ssl.SSLCertVerificationError) as error:
            print(f"Error downloading image {file_name}: {url}")
            print(f"Error details: {error}")


downloadimages(slechte_covers, path_slechte_covers)
