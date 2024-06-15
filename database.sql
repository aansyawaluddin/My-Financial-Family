CREATE DATABASE MyFinancialFamily;

USE MyFinancialFamily;

CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(255) NOT NULL,
    Fullname VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    Password VARCHAR(255) NOT NULL,
    Gender ENUM('male', 'female') NOT NULL,
    FamilyEmail VARCHAR(255) NOT NULL,
    Role VARCHAR(50) NOT NULL
    
);

CREATE TABLE ExpensesCategory (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,
    CategoryName VARCHAR(255) NOT NULL
);

CREATE TABLE PaymentMethods (
    MethodID INT AUTO_INCREMENT PRIMARY KEY,
    MethodName VARCHAR(255) NOT NULL
);

CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT NOT NULL,
    ExpensesCategoryID INT NOT NULL,
    Amount DECIMAL(10,2) NOT NULL,
    TransactionDate DATE NOT NULL,
    Description VARCHAR(255),
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (ExpensesCategoryID) REFERENCES ExpensesCategory(CategoryID)
);

CREATE TABLE DetailPayments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,
    TransactionID INT NOT NULL,
    PaymentMethodID INT NOT NULL,
    AmountPaid DECIMAL(10,2) NOT NULL,
    PaymentDate DATE NOT NULL,
    FOREIGN KEY (TransactionID) REFERENCES Transactions(TransactionID),
    FOREIGN KEY (PaymentMethodID) REFERENCES PaymentMethods(MethodID)
);


DROP DATABASE MyFinancialFamily;
