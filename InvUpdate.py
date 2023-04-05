import cur as cur
import pymysql
from numpy.core.defchararray import isnumeric  # exception handling


def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="",
        db='Managely',
    )

    cur = conn.cursor()
    # Pull Data from React command TBD

    # local values (For this case we need two types as we want the original values and the new values
    #Also we could get them locally as we can put those into the text boxes so the user can see the original data values

    #ORIGINAL VALUES (just in case you would like to pull them form the back to display for the front end
    # If not, we could do it by html link (the link sending the information on redirection (TBD)
    typeID = '32'
    invenID = '312'
    name = "nep"
    brand = "idk"
    price = '29.99'
    amount = '7'


    #NEW VALUES
    uTypeID = '52'
    uInvenID = '471'
    uName = "works2"
    uBrand = "idk"
    uPrice = '29.99'
    uAmount = '75'

 #EXCEPTION HANDLING for updated values



    # Insert Data
    # Create insert example (Will create pull information from text boxes further down the road
    # can create local values to store information from text boxes
    # makes it possible to do insert checks before they go through and relay information
    #In this case we would check the updated data as the data being pulled has already been validated

    update = "UPDATE `Inventory` SET `typeID`= %s,`invenID`= %s ,`name`=%s ,`brand`=%s ,`price`= %s,`amount`= %s WHERE `typeID`= %s AND `invenID`= %s AND`name`= %s AND`brand`= %s AND`price`= %s AND`amount`= %s "
    # we want a try and catch block to prevent repeated primary keys
    try:
        # execute statement
        cur.execute(update, (uTypeID, uInvenID, uName, uBrand, uPrice, uAmount,typeID, invenID, name, brand, price, amount))
    except:
        print("Error") #To see if it runs properly (Later can be used to send out and error message)

    # Commit Changes
    conn.commit()


# Driver Code
if __name__ == "__main__":
    mysqlconnect()