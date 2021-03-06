SELECT name as Customers FROM Customers 
LEFT JOIN Orders ON Customers.id = Orders.CustomerId 
WHERE Orders.CustomerId is NULL


SELECT Name as Customers from Customers 
WHERE Id NOT IN (SELECT CustomerId from Orders)

SELECT Name as Customers from Customers
WHERE NOT EXISTS (SELECT * FROM Orders WHERE Customers.Id = Orders.CustomerId)