import mysql.connector

try:
    # establish connection
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="root",
        database="iot_data",
        use_pure=True
    )

    cursor = connection.cursor()

    # user input
    sensor_id = int(input("Enter id: "))
    temperature = float(input("Enter temperature: "))
    humidity = float(input("Enter humidity: "))
    timestamp = input("Enter timestamp (YYYY-MM-DD HH:MM:SS): ")

    # parameterized query (SAFE)
    query = """
        INSERT INTO sensor_readings (id, temperature, humidity, timestamp)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (sensor_id, temperature, humidity, timestamp))
    connection.commit()

    print("Data inserted successfully ✅")

except mysql.connector.Error as err:
    print("Error:", err)

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
