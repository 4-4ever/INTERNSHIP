#!/usr/bin/env python
# coding: utf-8

# # SQL WORKSHEET
# 

# #### Created by VISHAL
# 

# In[2]:


import sqlite3


# In[3]:


#object

db=sqlite3.connect('Company_database.db')


# In[4]:


#creating cursor

cur=db.cursor()


# ## SQL query to create table Customers.
# 

# In[5]:


cur.execute("create table Customers (customerNumber int primary key,customerName text,contactLastName text,contactFirstName text,phone int,addressLine1 text,addressLine2 text,city text,state text,postalCode int,country text,salesRepEmployeeNumber int,creditLimit int)")


# ## SQL query to create table Orders.
# 

# In[6]:


cur.execute("create table Orders (orderNumber int primary key,orderDate date,requiredDate date,shippedDate date,status text,comments text,customerNumber int)")


# ## SQL query to show all the columns data from the Orders Table.
# 

# In[7]:


results=cur.execute("select * from Orders")
results.fetchall()


# ## SQL query to show all the comments from the Orders Table.
# 

# In[8]:


results=cur.execute('select comments from Orders')
results.fetchall()


# ## SQL query to show orderDate and Total number of orders placed on that date, from Orders table.
# 

# In[9]:


results=cur.execute("select orderDate,count(orderNumber) from Orders where orderDate='2022-03-25'")
results.fetchall()


# ## SQL query to show employeNumber, lastName, firstName of all the employees from employees table
# 

# In[10]:


cur.execute("create table Employees (employeeNumber int primary key,lastName text,firstName text,extension int,email text,officeCode int,reportsTo text,jobTitle text)")


# In[11]:


results=cur.execute('select employeeNumber,lastName,firstName from Employees')
results.fetchall()


# ## SQL query to show all orderNumber, customerName of the person who placed the respective order.
# 

# In[12]:


results=cur.execute('select Orders.orderNumber, Customers.customerName from Orders inner join Customers on Orders.customerNumber=Customers.customerNumber')
results.fetchall()


# ## SQL query to show name of all the customers in one column and salerepemployee name in another column.
# 

# In[13]:


results=cur.execute('select customerName,salesRepEmployeeNumber from Customers')
results.fetchall()


# ## SQL query to show Date in one column and total payment amount of the payments made on that date from the payments table.
# 

# In[14]:


cur.execute("create table Payments (customerNumber int primary key,checknumber int,paymentDate date,amount real)")


# In[15]:


results=cur.execute('select paymentDate,sum(amount) from Payments')
results.fetchall()


# ## SQL query to show all the products productName, MSRP, productDescription from the products table.
# 

# In[16]:


cur.execute("create table Products (productCode int primary key,productName text,productLine text,productScale text,productVendor text,productDescription text,quantityInStock int,buyPrice real,MSRP real)")


# In[17]:


results=cur.execute('select productName,MSRP,productDescription from Products')
results.fetchall()


# ## SQL query to print the productName, productDescription of the most ordered product.
# 

# In[18]:


cur.execute("create table Orderdetails (orderNumber int primary key,productCode int,quantityOrdered int,priceEach real,orderLineNumber int)")


# In[19]:


results=cur.execute('select Products.productName, Products.productDescription from Products inner join Orderdetails on Products.productCode=Orderdetails.productCode')
results.fetchall()


# ## SQL query to print the city name where maximum number of orders were placed.
# 

# In[20]:


results=cur.execute('select Orderdetails.orderNumber,Orders.customerNumber,Customers.city from Orderdetails join Orders on Orderdetails.orderNumber=Orders.orderNumber join Customers on Customers.customerNumber=Orders.customerNumber ')
results.fetchall()


# ## SQL query to get the name of the state having maximum number of customers.
# 

# In[21]:


results=cur.execute('select max(state),customerName from Customers')
results.fetchall()


# ## SQL query to print the employee number in one column and Full name of the employee in the second column for all the employees.
# 

# In[22]:


results=cur.execute('select employeeNumber,firstname+" "+lastName as "fullName" from Employees')
results.fetchall()


# ## SQL query to print the orderNumber, customer Name and total amount paid by the customer for that order (quantityOrdered × priceEach).
# 

# In[23]:


results=cur.execute('select Orders.orderNumber,Customers.customerName,Payments.amount from Orders join Customers on Orders.customerNumber=Customers.customerNumber join Payments on Payments.customerNumber=Customers.customerNumber ')
results.fetchall()


# In[ ]:




