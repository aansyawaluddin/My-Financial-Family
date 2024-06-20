CREATE DATABASE MyFinancialFamily;

USE MyFinancialFamily;

CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(255) DEFAULT NULL,
    Fullname VARCHAR(255) DEFAULT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    Password VARCHAR(255) NOT NULL,
    Gender ENUM('male', 'female') DEFAULT NULL,
    FamilyEmail VARCHAR(255) DEFAULT NULL,
    Role VARCHAR(255) DEFAULT NULL,
    is_admin BOOLEAN NOT NULL DEFAULT 0,
    CHECK ((is_admin = 1 AND Username = 'admin' AND Fullname IS NULL AND Gender IS NULL AND FamilyEmail IS NULL AND Role IS NULL) OR
           (is_admin = 0 AND Username IS NOT NULL AND Fullname IS NOT NULL AND Gender IS NOT NULL AND FamilyEmail IS NOT NULL))
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


-- Tambahkan akun admin
INSERT INTO Users (Username, Email, Password, is_admin) VALUES ('admin','admin@gmail.com', '123', 1);



DROP DATABASE MyFinancialFamily;
