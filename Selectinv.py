from flask import Flask
import pymysql

#app = Flask(__name__)


def Select():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="",
        db='Managely',
    )

    cur = conn.cursor()

    # Commit Changes
    conn.commit()

    # Select query
    cur.execute("SELECT * FROM `Inventory` ")
    output = cur.fetchall()


 #For the value i in our output = select statement print it out to console for now
    # If react references data then, it's a matter of figuring out on how to pull said data
    for i in output:
        print(i)

    # To close the connection
    conn.close()


#@app.route('/')
#def homepage()



if __name__ == "__main__":
    Select()

