import pymysql


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

# local values
    typeID = '3'
    name = "nep"
    brand = "idk"
    price = '29.99'
    amount = '7'

    #Exception checking


    #typeID
    if typeID == '':
        print("Error Invalid input")
        # check for whitespaces
    elif ' ' in typeID:
        print("Sorry no whitespaces allowed")

        # check for length
    elif len(typeID) > 20:
        print("Error invalid size")

        # check for integer (if int exit while else invalid)
    elif typeID.isnumeric():
        check = 1
    else:
        print("Sorry Invalid integer")

    #name
    if name == '':
        print("Error invalid input")

        # check for integer
    elif name.isnumeric():
        print("invalid name ")


    #brand
    if brand == '':
        print("Error invalid input")

        # check for integer
    elif brand.isnumeric():
        print("invalid brand ")




    #price
    if price == '':
        print("Error Invalid input")

        # check for whitespaces
    elif ' ' in price:
        print("Sorry no whitespaces allowed")

        # check for length
    elif len(price) > 10:
        print("Error invalid size")

        # check for integer
    elif price.isnumeric():
        check = 1
    else:
        print("Sorry invalid integer")

    #amount
        # invenID check
        while check == 0:

            if amount == '':
                print("Error Invalid input")

                # check for whitespaces
            elif ' ' in amount:
                print("Sorry no whitespaces allowed")

                # check for length
            elif len(amount) > 11:
                print("Error invalid size")

                # check for integer
            elif amount.isnumeric():
                check = 1
            else:
                print("Sorry invalid integer")


    # Insert Data
    insert = "INSERT INTO `Inventory`(`typeID`, `name`, `brand`, `price`, `amount`) VALUES (%s,%s,%s,%s,%s)"

    #we want a try and catch block to prevent repeated primary keys
    try:
        # execute statement
        cur.execute(insert, (typeID, name, brand, price, amount))
    except:
        print("Error")
        print("Check primary keys values for testing ")
    # Commit Changes
    conn.commit()


# Driver Code
if __name__ == "__main__":
    mysqlconnect()