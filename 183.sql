SELECT name as Customers FROM Customers 
LEFT JOIN Orders ON Customers.id = Orders.CustomerId 
WHERE Orders.CustomerId is NULL
