import sqlite3

# Pad naar de database file
conn = sqlite3.connect(r'C:\Users\Natha\OneDrive - Thomas More\vakken\jaar2\Digital Innovation\3 Uant Coverserver\cover.sqlite3')
cursor = conn.cursor()

# Locked covers query
locked_coversQ = """
    SELECT cl.cover_number_id
    FROM cover_covernumberlocked cl
    WHERE cl.cover_number_id IN (
        SELECT ci.id
        FROM cover_coverimage ci
        WHERE ci.cover_client != 'Cipal'
    )
    LIMIT 10;
"""
cursor.execute(locked_coversQ)
locked_covers = cursor.fetchall()
print(f"Dit zijn de locked covers: {locked_covers}")

#
goede_coversQ = """
    SELECT ci.id
    FROM cover_coverimage ci
    WHERE ci.id NOT IN (
        SELECT cl.cover_number_id
        FROM cover_covernumberlocked cl
        WHERE cl.cover_number_id IN (
            SELECT ci.id
            FROM cover_coverimage ci
            WHERE ci.cover_client != 'Cipal')
            AND
            ci.cover_client != 'Cipal'
)
LIMIT 10;

"""
cursor.execute(goede_coversQ)
goede_covers = cursor.fetchall()
print(f"Dit zijn de goede covers: {goede_covers}")

conn.close()
