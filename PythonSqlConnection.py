#!/usr/bin/env python
# coding: utf-8

# # Fetched data from MySQL database & display table's content(using select)

# In[3]:


import mysql.connector

mydb = mysql.connector.connect( host="localhost", user="Samrudhi", passwd="Samnil7@", database="data" )

print(mydb)

mycursor = mydb.cursor()

sql = "SELECT * FROM Employees"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


# # Insert Values

# In[4]:


sql = "Insert into Employees values (1,'Alan Smith','19890101',1)"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record inserted.")


# # Delete Record

# In[8]:


sql = "DELETE FROM Employees WHERE Employee_name = 'Alan Smith'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted.")


# # Update Record

# In[11]:


sql = "UPDATE Employees SET Department_ID  = 7 WHERE Employee_name = 'Peter Hilton'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record updated.")


# # Joins
# ### JOINS are used to retrieve data from multiple tables. 
# ### Department table is already craeted on MySQL database

# In[13]:


sql = "SELECT * FROM Departments"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


# ## <u>Inner Join</u>
# ### INNER JOIN Returns records that have matching values in both tables

# In[16]:


# if Department ID in Employees table matches Department_id  from Department table

sql = "SELECT Employee_id,Employee_name, Employee_DOB, Department_Name        FROM Departments INNER JOIN Employees       ON Departments.Department_id = Employees.Department_ID"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


# ## <u>Outer join</u>
# ### LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table

# In[17]:


sql = "SELECT Employee_id,Employee_name, Employee_DOB, Department_Name       FROM Employees LEFT JOIN Departments       ON Departments.Department_id = Employees.Department_ID"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


# ### RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table

# In[18]:


sql = "SELECT Employee_id,Employee_name, Employee_DOB, Department_Name       FROM Employees RIGHT JOIN Departments       ON Departments.Department_id = Employees.Department_ID"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


# ## <u>CROSS Join</u>
# ### CROSS JOIN which is a bit different from the other Join operations. It is used to create a combination of two different sets without have mutual columns. 

# In[19]:


#As an example, if we need to create a combination of all departments with all employees.

sql = "SELECT Employee_id, Employee_name, Employee_DOB, Department_Name        FROM Employees CROSS JOIN Departments"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


# In[ ]:




