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











#Select inventory function with formatting for example output
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










#Original Inventory Select function without new formatting.

# def Select():
#     # To connect MySQL database
#     conn = pymysql.connect(
#         host='localhost',
#         user='root',
#         password="",
#         db='Managely',
#     )

#     cur = conn.cursor()

#     # Commit Changes
#     conn.commit()

#     # Select query
#     cur.execute("SELECT * FROM `Inventory` ")
#     output = cur.fetchall()


#  #For the value i in our output = select statement print it out to console for now
#     # If react references data then, it's a matter of figuring out on how to pull said data
#     for i in output:
#         print(i)

#     # To close the connection
#     conn.close()

    








# # Admin Add function

# def mysqlconnect():
#     # To connect MySQL database
#     conn = pymysql.connect(
#         host='localhost',
#         user='root',
#         password="",
#         db='Managely',
#     )

#     cur = conn.cursor()
#     # Pull Data from React command TBD

#     # local values that can be replaced from the text values
#     # Since we are the admin who will be entering the data, they should be the only ones who will have access to edit this for now
#     ID= '12425'
#     SSN = '122914372'
#     fName = "Po"
#     lName = "J"
#     gender = "M"
#     #For date its yyyy-mm-dd
#     DOB = '1976-10-01'
#     termInfo = "Q3"
#     job = "Engineer"
#     salary = '50000'
#     description = "This can be anything"
#     InvID = '0'
#     time = '01:00:00'
#     date = '2021-02-12'
#     username = "Default"
#     password = "nice"
#     email = "default@gmail.com"
#     #Exception checking




#     # Insert Data
#     # Create insert example (Will create pull information from text boxes further down the road
#     # can create local values to store information from text boxes
#     # makes it possible to do insert checks before they go through and relay information

#     insert = "INSERT INTO `EmployeeInfoAdmin`(`aID`, `SSN`, `aFName`, `aLName`, `agender`, `aDateOfBirth`, `aTermInfo`) VALUES (%s,%s,%s,%s,%s,%s,%s)"


#     #2nd insert statement for EmpInfo
#     insert2 = "INSERT INTO `EmployeeInfo`(`ID`, `fName`, `lName`, `gender`, `dateOfBirth`, `termInfo`, `salary`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
#     #3rd insert statement for Positions
#     insert3 = "INSERT INTO `Positions`(`employeeID`,`invenTypeID`, `job`, `salary`, `description`) VALUES (%s,%s,%s,%s,%s)"
#     #4th insert statement for Schedule ** INVESTGATING HOW **
#     insert4 = "INSERT INTO `Schedule`(`sID`, `sFName`, `sLName`,`date`,`dateTime`) VALUES (%s,%s,%s,%s,%s)"
#     #5th insert for login which will have default values for now
#     insert5 = "INSERT INTO `Login details`(`ID`, `username`, `password`, `email`) VALUES (%s,%s,%s,%s)"

#     # we want a try and catch block to prevent repeated primary keys
#     try:
#         # execute statement
#         cur.execute(insert,(ID,SSN,fName,lName,gender,DOB,termInfo))
#     except:
#         print("Error")

#     try:
#         # execute statement
#         cur.execute(insert2, (ID,fName,lName,gender,DOB,termInfo,salary))
#     except:
#         print("Error2")

#     try:
#         # execute statement
#         cur.execute(insert3, (ID,InvID,job,salary,description))
#     except:
#         print("Error3")

#     try:
#         # execute statement
#         cur.execute(insert4, (ID,fName,lName,date,time))
#     except:
#         print("Error4")

#     try:
#         # execute statement
#         cur.execute(insert5, (ID,username,password,email))
#     except:
#         print("Error5")

#     # Commit Changes
#     conn.commit()











# # Delete reference function


# def mysqlconnect():
#     # To connect MySQL database
#     conn = pymysql.connect(
#         host='localhost',
#         user='root',
#         password="",
#         db='Mangely',
#     )

#     cur = conn.cursor()

# # Insert Data
#     # Create insert example (Will create pull information from text boxes further down the road
#     #can create local values to store information from text boxes
#     #need to fix Price to ensure that it is also considered for validation
#     insert = "DELETE FROM `Inventory` WHERE `Brand`= 'John' && `Quantity` = '10' && 'Price'= 59.99 ;"
#     cur.execute(insert)


#     # Commit Changes
#     conn.commit()










# #Edit Reference function

# def mysqlconnect():
#     # To connect MySQL database
#     conn = pymysql.connect(
#         host='localhost',
#         user='root',
#         password="",
#         db='Mangely',
#     )

#     cur = conn.cursor()

# # Insert Data
#     # Create insert example (Will create pull infromation from text boxes further down the road
#     #can create local values to store information from text boxes
#     #makes it possible to do insert checks before they go through and relay information
#     Edit = "UPDATE `Inventory` SET `Brand`='Bra',`Quantity`='34', `Price`= '89.99' WHERE `Brand` = 'Brandon' && `Quantity` = '34' &&  `Price` = '79.99'"
#     cur.execute(Edit)


#     # Commit Changes
#     conn.commit()










# # Exception Handling Example

# Test = ''

# #Check for empty
# if Test =='':
#     print("Error Invalid input")
#     #check for integer
# elif Test.isnumeric():
#     print("Error its a integer")
#     #check for whitespaces (For login)
# elif ' ' in Test:
#     print("Sorry no whitespaces allowed")
# else:
#     print("Passed")










# Exception Examples

# #loop value
#     check  = 0
#     #Exception Handling if wanted to be done in the backend

#     #check typeID
#     while check == 0:
#         if typeID == '':
#             print("Error Invalid input")
#             # check for whitespaces
#         elif ' ' in typeID:
#             print("Sorry no whitespaces allowed")

#             #check for length
#         elif  len(typeID) > 20:
#             print("Error invalid size")

#             # check for integer (if int exit while else invalid)
#         elif typeID.isnumeric():
#             check = 1
#         else:
#             print("Sorry Invalid integer")

#         # reset check value
#         check = 0
#         #invenID check
#         while check == 0:

#             if invenID == '':
#                 print("Error Invalid input")

#                 # check for whitespaces
#             elif ' ' in invenID:
#                 print("Sorry no whitespaces allowed")

#                 # check for length
#             elif len(invenID) > 20:
#                 print("Error invalid size")

#                 # check for integer
#             elif invenID.isnumeric():
#                 check = 1
#             else:
#                 print("Sorry invalid integer")

#             # reset check value
#         check = 0

#         #name check
#         while check == 0:

#             if name == '':
#                 print("Error invalid input")

#                 # check for integer
#             elif invenID.isnumeric():
#                 print("invalid name ")
#             else:
#                 check = 1

#                 # reset check value
#                 check = 0
#                 # brand check
#         while check == 0:

#                     if brand == '':
#                         print("Error invalid input")

#                         # check for integer
#                     elif brand.isnumeric():
#                         print("invalid brand ")
#                     else:
#                         check = 1

#         # reset check value
#         check = 0

#         # price check
#         while check == 0:

#             if price == '':
#                 print("Error Invalid input")

#                 # check for whitespaces
#             elif ' ' in price:
#                 print("Sorry no whitespaces allowed")

#                 # check for length
#             elif len(price) > 10:
#                 print("Error invalid size")

#                 # check for integer
#             elif price.isnumeric():
#                 continue
#             else:
#                 print("Sorry invalid integer")



#                 # reset check value
#                 check = 0
#                 # invenID check
#                 while check == 0:

#                     if amount == '':
#                         print("Error Invalid input")

#                         # check for whitespaces
#                     elif ' ' in amount:
#                         print("Sorry no whitespaces allowed")

#                         # check for length
#                     elif len(amount) > 11:
#                         print("Error invalid size")

#                         # check for integer
#                     elif amount.isnumeric():
#                         continue
#                     else:
#                         print("Sorry invalid integer")










# Insert Reference

# def mysqlconnect():
#     # To connect MySQL database
#     conn = pymysql.connect(
#         host='localhost',
#         user='root',
#         password="",
#         db='Managely',
#     )

#     cur = conn.cursor()
# #Pull Data from React command TBD

# #Test local values
#     Test1 = "BOB"
#     Test2 = '12'
#     Test3 = '29.99'

#     #Exception Handling
#     if Test1 == '':
#         print("Error Invalid input")
#         # check for integer
#     elif Test1.isnumeric():
#         print("Error its a integer")
#         # check for whitespaces (For login)
#     elif ' ' in Test1:
#         print("Sorry no whitespaces allowed")

#         # Exception Handling 2
#         if Test2 == '':
#             print("Error Invalid input")
#             # check for whitespaces
#         elif ' ' in Test2:
#             print("Sorry no whitespaces allowed")

#             # Exception Handling 3
#         if Test3 == '':
#             print("Error Invalid input")
#         elif Test3.isalpha():
#             print("Sorry invalid entry")
#         elif ' ' in Test3:
#             print("Sorry no whitespaces allowed")
#         else:
#             print("Passed")




# # Insert Data
#     # Create insert example (Will create pull information from text boxes further down the road
#     #can create local values to store information from text boxes
#     #makes it possible to do insert checks before they go through and relay information
#     insert = "INSERT INTO `Inventory` (`Brand`, `Quantity`, `Price`) VALUES ( %s, %s , %s );"
#     cur.execute(insert,(Test1,Test2,Test3))


#     # Commit Changes
#     conn.commit()










# # Inventory Add

# def mysqlconnect():
#     # To connect MySQL database
#     conn = pymysql.connect(
#         host='localhost',
#         user='root',
#         password="",
#         db='Managely',
#     )

#     cur = conn.cursor()
# #Pull Data from React command TBD

# # local values
#     typeID = '3'
#     invenID = '00312'
#     name = "nep"
#     brand = "idk"
#     price = '29.99'
#     amount = '7'

#     # Insert Data
#     # Create insert example (Will create pull information from text boxes further down the road
#     #can create local values to store information from text boxes
#     #makes it possible to do insert checks before they go through and relay information


#     insert = "INSERT INTO `Inventory`(`typeID`, `invenID`, `name`, `brand`, `price`, `amount`) VALUES (%s,%s,%s,%s,%s,%s)"

#     #we want a try and catch block to prevent repeated primary keys
#     try:
#         # execute statement
#         cur.execute(insert, (typeID, invenID, name, brand, price, amount))
#     except:
#         print("Error")
#         print("Check primary keys values for testing ")
#     # Commit Changes
#     conn.commit()










# Select employees information

# def Select():
#     # To connect MySQL database
#     conn = pymysql.connect(
#         host='localhost',
#         user='root',
#         password="",
#         db='Managely',
#     )

#     cur = conn.cursor()

#     # Commit Changes
#     conn.commit()

#     # Select query
#     cur.execute("SELECT * FROM `EmployeeInfoAdmin` ")
#     output = cur.fetchall()



#     # To close the connection
#     conn.close()









# Driver Code
if __name__ == "__main__":
    app.run(debug=True)