from flask import Flask
import pymysql
import json

app = Flask(__name__)

#Members API Route

#test members route that works with react
@app.route("/members")
def members():
    output = Select()
    return {"members": output}

@app.route("/SelectInventory")
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
    cur.execute("SELECT * FROM `Inventory` WHERE typeID = 5")
    output = cur.fetchall()
    newOutput = output[0]
 #For the value i in our output = select statement print it out to console for now
    # If react references data then, it's a matter of figuring out on how to pull said data
    for i in output:
        print(i)

    print(list(newOutput))
    # To close the connection
    conn.close()

    return (list(newOutput))

    


if __name__ == "__main__":
    app.run(debug=True)