import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS mcc")
cursor.execute("USE mcc")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS sybscit(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), roll_number INT, address VARCHAR(255), phone_number VARCHAR(255), email VARCHAR(255))"
)
insert_query = "INSERT INTO sybscit(name, roll_number, address, phone_number, email) VALUES (%s, %s, %s, %s, %s)"
data = [
    ('john doe', 1, '123 main st', '555-5555', 'john@example.com'),
    ('jane smith', 2, '456 oak st', '555-1234', 'jane@example.com'),
    ('alice johnson', 3, '789 pine st', '555-9876', 'alice@example.com'),
    ('bob brown', 4, '321 maple st', '555-6543', 'bob@example.com'),
    ('admin', 5, '999 elm st', '555-0000', 'admin123@gmail.com'),
]
cursor.executemany(insert_query, data)
db.commit()
update_query = "UPDATE sybscit SET email = 'admin@gmail.com' WHERE email = 'admin123@gmail.com'"
cursor.execute(update_query)
db.commit()
delete_query = "DELETE FROM sybscit WHERE roll_number = 5"
db.execute(delete_query)
db.cursor()
cursor.execute("SELECT * FROM sybscit")
rows.cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
db.close()