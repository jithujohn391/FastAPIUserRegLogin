import psycopg2

hostname='localhost'
database='postgres'
username='postgres'
pwd='Global12$'
port_id=5432
print("hi")
conn=None
print(conn)
cur=None
print(cur)
try:
    conn=psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
    )
    
    cur=conn.cursor()
    print(cur)
    
except Exception as error:
    print(error)
