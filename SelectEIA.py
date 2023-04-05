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
    cur.execute("SELECT * FROM `EmployeeInfoAdmin` ")
    output = cur.fetchall()



    # To close the connection
    conn.close()


#@app.route('/')
#def homepage()



if __name__ == "__main__":
    Select()

