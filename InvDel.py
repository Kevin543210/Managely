import cur as cur
import pymysql
from numpy.core.defchararray import isnumeric #exception handling


def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="",
        db='Managely',
    )

    cur = conn.cursor()
#Pull Data from React command TBD
#Assuming that it will be button based
    """
    Such as 
    
    data 1                  Edit    Delete
    data 2                  Edit    Delete 
    
    If they were to click the delete for the first one, it would pull those variables upon click, which would then 
    place those variables in the back locally to then run the code below to delete that said option.
    
    As For admin Looking into how we want to do as if we were to cascade it, we need to be careful as it will delete 
    anything that is related to that variables 
        
    Such as, if I were to delete an inventory value, it would also delete from the positions table as well as it would 
    be a forign key for that table 
    """

# local values
    typeID = '5'
    invenID = '312'
    name = "works"
    brand = "idk"
    price = '29.99'
    amount = '7'

    # Insert Data
    # Create insert example (Will create pull information from text boxes further down the road
    #can create local values to store information from text boxes
    #makes it possible to do insert checks before they go through and relay information


    delete = "DELETE FROM `Inventory` WHERE typeID = %s AND `invenID` = %s AND name = %s AND `brand` = %s AND `price`  = %s AND `amount` = %s"

    #we want a try and catch block to prevent repeated primary keys
    try:
        # execute statement
        cur.execute(delete, (typeID, invenID, name, brand, price, amount))
    except:
        print("Error")
    # Commit Changes
    conn.commit()


# Driver Code
if __name__ == "__main__":
    mysqlconnect()