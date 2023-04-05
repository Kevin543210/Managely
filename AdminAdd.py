import cur as cur
import pymysql
from numpy.core.defchararray import isnumeric


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

    # local values that can be replaced from the text values
    # Since we are the admin who will be entering the data, they should be the only ones who will have access to edit this for now
    ID= '7654'
    SSN = '122914372'
    fName = "Po"
    lName = "J"
    gender = "M"
    #For date its yyyy-mm-dd
    DOB = '1976-10-01'
    termInfo = "Q3"
    job = "Engineer"
    salary = '50000'
    description = "This can be anything"
    InvID = '0'
    time = '01:00:00'
    date = '2021-02-12'
    username = "Default"
    password = "nice"
    email = "default@gmail.com"
    #Exception checking




    # Insert Data
    # Create insert example (Will create pull information from text boxes further down the road
    # can create local values to store information from text boxes
    # makes it possible to do insert checks before they go through and relay information

    insert = "INSERT INTO `EmployeeInfoAdmin`(`aID`, `SSN`, `aFName`, `aLName`, `agender`, `aDateOfBirth`, `aTermInfo`) VALUES (%s,%s,%s,%s,%s,%s,%s)"


    #2nd insert statement for EmpInfo
    insert2 = "INSERT INTO `EmployeeInfo`(`ID`, `fName`, `lName`, `gender`, `dateOfBirth`, `termInfo`, `salary`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    #3rd insert statement for Positions
    insert3 = "INSERT INTO `Positions`(`employeeID`,`invenTypeID`, `job`, `salary`, `description`) VALUES (%s,%s,%s,%s,%s)"
    #4th insert statement for Schedule ** INVESTGATING HOW **
    insert4 = "INSERT INTO `Schedule`(`sID`, `sFName`, `sLName`,`date`,`dateTime`) VALUES (%s,%s,%s,%s,%s)"
    #5th insert for login which will have default values for now
    insert5 = "INSERT INTO `Login details`(`ID`, `username`, `password`, `email`) VALUES (%s,%s,%s,%s)"

    # we want a try and catch block to prevent repeated primary keys
    try:
        # execute statement
        cur.execute(insert,(ID,SSN,fName,lName,gender,DOB,termInfo))
    except:
        print("Error")

    try:
        # execute statement
        cur.execute(insert2, (ID,fName,lName,gender,DOB,termInfo,salary))
    except:
        print("Error2")

    try:
        # execute statement
        cur.execute(insert3, (ID,InvID,job,salary,description))
    except:
        print("Error3")

    try:
        # execute statement
        cur.execute(insert4, (ID,fName,lName,date,time))
    except:
        print("Error4")

    try:
        # execute statement
        cur.execute(insert5, (ID,username,password,email))
    except:
        print("Error5")

    # Commit Changes
    conn.commit()


# Driver Code
if __name__ == "__main__":
    mysqlconnect()