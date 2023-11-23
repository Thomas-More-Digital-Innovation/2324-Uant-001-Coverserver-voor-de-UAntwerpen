import sqlite3
import urllib.request
import os

# Pad naar de database file
conn = sqlite3.connect(
    r'C:\Users\Natha\OneDrive - Thomas More\vakken\jaar2\Digital Innovation\3 Uant Coverserver\cover.sqlite3')
cursor = conn.cursor()

# Locked covers query
locked_coversQ = """
SELECT ci.url
FROM cover_coverimage ci
WHERE ci.id IN (    
    SELECT cl.cover_number_id
    FROM cover_covernumberlocked cl
    WHERE cl.cover_number_id IN (
        SELECT ci.id
        FROM cover_coverimage ci
        WHERE ci.cover_client != "Cipal"
    )
)
LIMIT 10;
"""
cursor.execute(locked_coversQ)
locked_covers = cursor.fetchall()
# print(f"Dit zijn de locked covers: {locked_covers}")

# goede covers query
goede_coversQ = """
SELECT ci.url
FROM cover_coverimage ci
	WHERE ci.id NOT IN (
	SELECT cl.cover_number_id
    FROM cover_covernumberlocked cl
    WHERE cl.cover_number_id IN (
        SELECT ci.id
        FROM cover_coverimage ci)
	)
	AND
	ci.cover_client != "Cipal"
LIMIT 30;
"""
cursor.execute(goede_coversQ)
goede_covers = cursor.fetchall()
# print(f"Dit zijn de goede covers: {goede_covers}")

conn.close()


def downloadimages(covers, path):
    x = 1

    for cover in covers:
        url = cover[0]  # haal url uit tuple
        file_name = str(x)
        full_path = os.path.join(path, f"{file_name}.jpg")

        urllib.request.urlretrieve(url, full_path)
        #if x == 4:
        print(url)
        x += 1
        print(full_path)


path_goede_covers = r"C:\goede_covers"
path_slechte_covers = r"C:\slechte_covers"

downloadimages(goede_covers, path_goede_covers)
# downloadimages(locked_covers, path_slechte_covers)
