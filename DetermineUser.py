#example on how we can check for user input

#create array (which is our json file datavalues)

test = ["Admin","random@managely.com",
        "Employee","Random@gmail.com",
        "New user", "Default@gmail.com"]

#check which types are users are in here

print(test)

#This part was completed in login instructions but is being mocked for testing purposes.
#Enter user Id
#enter password

#check if valid

#if so begin login process

#if not return

#check exception



#There is two way to approach this
#since we got the login to complete successfully, we now want to check which page they will be redirected to.
#Option 1: If The user enters the information correctly, we can look what data is stored on that index and save the
#email locally to determine choice
email = "default@gmail.com"


if "@managely.com" in email:
    print("This is an admin")
    #redirect to admin version of webpage

    #leave root access alone for admin as they should have root access

elif  "@managely.com" not in email and "default" not in email:
    print("this is an employee, with no default login details")

    #Redirect to user version of UI (which is just the same as the Admin but without employee details

    #since we are going to a new UI page we want to set certain restrictions so that the user cannot see all details in
    #our database

    #BY root

    #OR by just deleting other options aka, they will just have inventory access only.


#THIS IS OPTIONAL
elif "@managely.com" not in email and "default" in email:
    print("This is not an admin, so employee, but does not have a good login so redirect to username and email updated")

    #redirect to update page

    #once done, to employee UI with privlages update or webpage with no options
