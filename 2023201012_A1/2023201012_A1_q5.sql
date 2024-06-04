--Create database assignment;
--use assignment;
--ALTER TABLE userDetails ADD PRIMARY KEY (`User ID`);
--ALTER TABLE orderDetails ADD PRIMARY KEY (`Order ID`);
--ALTER TABLE brandDetails ADD PRIMARY KEY (`Brand ID`);
--ALTER TABLE orderDetails ADD FOREIGN KEY(`Buyer ID`) references userDetails(`User ID`); 
--ALTER TABLE orderDetails ADD FOREIGN KEY(`Seller ID`) references userDetails(`User ID`); 
--ALTER TABLE orderDetails ADD FOREIGN KEY(`Brand ID`) references brandDetails(`Brand ID`);
create table report (
UserID int,
UserName varchar(30),
Result varchar(4) 
);
Alter table report Drop column Result;
Insert into report select `User ID`,`Name` from userDetails;
Alter table report add column Result Varchar(5);
-- set all the values to no initially
UPDATE report SET Result="No";
-- set all the values which are greater than 2 to "yes" initially
UPDATE report SET Result ="Yes" WHERE `UserID` IN (SELECT `Seller ID` FROM orderDetails GROUP BY `Seller ID` HAVING count(`Seller ID`)>2);
-- need to findout which are actually yes, so just changed all the ones with no which are not matching
UPDATE report SET Result ="No" where `UserID` NOT IN (
WITH RankedItems AS (
SELECT `Seller ID`,`Brand ID`,`Order Date`,
ROW_NUMBER() OVER(PARTITION BY `Seller ID` ORDER BY `Order Date` Asc) as rankk
FROM orderDetails WHERE `Seller ID` IN (SELECT `UserID` FROM report WHERE Result="Yes") 
)
,Brands AS (
SELECT `Seller ID`,`Brand ID` AS brandID
FROM RankedItems
WHERE rankk= 2)
SELECT `Seller ID` FROM Brands br,userDetails u,brandDetails b WHERE u.`User ID`=br.`Seller ID` AND br.brandID=b.`Brand ID` AND u.`Favorite Laptop Brand`=b.`Laptop Brand`);
SELECT * FROM report;
