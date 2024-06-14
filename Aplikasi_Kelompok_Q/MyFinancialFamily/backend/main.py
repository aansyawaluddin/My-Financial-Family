from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
import mysql.connector
import bcrypt

app = FastAPI()

# Koneksi ke database
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    database="MyFinancialFamily"
)

mycursor = mydb.cursor()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ganti dengan daftar domain yang diperbolehkan jika perlu
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserLogin(BaseModel):
    Email: str
    Password: str

# Pydantic model untuk entitas Pengguna (Users)
class User(BaseModel):
    Username: str
    Fullname: str
    Password: str
    Gender: str
    Email: str
    Role: str

# Pydantic model untuk entitas Kategori Pengeluaran
class ExpenseCategory(BaseModel):
    CategoryName: str

# Pydantic model untuk entitas Metode Pembayaran
class PaymentMethod(BaseModel):
    MethodName: str

# Pydantic model untuk entitas Transaksi
class Transaction(BaseModel):
    UserID: int
    ExpensesCategoryID: int
    Amount: float
    TransactionDate: str
    Description: str

# Pydantic model untuk entitas DetailPayments
class DetailPayment(BaseModel):
    TransactionID: int
    PaymentMethodID: int
    AmountPaid: float
    PaymentDate: str

# Digunakan Untuk Verifikasi Login User
def verify_password(plain_password: str, hashed_password: str):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

@app.post("/login/")
async def login(user: UserLogin):
    mycursor.execute("SELECT UserID, Password FROM Users WHERE Email = %s", (user.Email,))
    result = mycursor.fetchone()
    if result:
        user_id, hashed_password = result
        if verify_password(user.Password, hashed_password):
            return {"message": "Login successful", "UserID": user_id}
        else:
            raise HTTPException(status_code=400, detail="Incorrect password")
    else:
        raise HTTPException(status_code=404, detail="User not found")


    
# CRUD Untuk Users
## Fungsi untuk hashing password menggunakan bcrypt
def hash_password_bcrypt(password: str):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

@app.post("/users/")
async def create_user(user: User):
    # Hash password sebelum disimpan
    hashed_password = hash_password_bcrypt(user.Password)
    
    # Periksa apakah email sudah ada
    mycursor.execute("SELECT * FROM Users WHERE Email = %s", (user.Email,))
    result = mycursor.fetchone()
    if result:
        raise HTTPException(status_code=400, detail="Email Is Already Taken")
    
    # Query SQL untuk menyimpan data pengguna
    sql = "INSERT INTO Users (Username, Fullname, Password, Gender, Email, Role) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (user.Username, user.Fullname, hashed_password, user.Gender, user.Email, user.Role)

    
    # Eksekusi query
    mycursor.execute(sql, val)
    mydb.commit()
    return {"message": "User created successfully"}

@app.get("/users/{UserID}")
async def read_user(UserID: int = Path(..., description="Input ID")):
    mycursor.execute("SELECT UserID, Username, Gender, Email, Role FROM Users WHERE UserID = %s", (UserID,))
    result = mycursor.fetchone()
    if result:
        return {"UserID": result[0], "Username": result[1], "Gender": result[2], "Email": result[3], "Role": result[4]}
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{UserID}")
async def update_user(UserID: int, user: User):
    # Jika password diubah, hash password baru
    if user.Password:
        hashed_password = hash_password_bcrypt(user.Password)
        sql = "UPDATE Users SET Username = %s, Password = %s, Gender = %s, Email = %s, Role = %s WHERE UserID = %s"
        val = (user.Username, hashed_password, user.Gender, user.Email, user.Role, UserID)
    else:
        # Jika password tidak diubah, gunakan password lama
        sql = "UPDATE Users SET Username = %s, Gender = %s, Email = %s, Role = %s WHERE UserID = %s"
        val = (user.Username, user.Gender, user.Email, user.Role, UserID)

    # Eksekusi query
    mycursor.execute(sql, val)
    mydb.commit()

    return {"message": "User updated successfully"}

@app.delete("/users/{UserID}")
async def delete_user(UserID: int):
    mycursor.execute("DELETE FROM Users WHERE UserID = %s", (UserID,))
    mydb.commit()
    return {"message": "User deleted successfully"}

# CRUD untuk Kategori Pengeluaran
@app.post("/categories/")
async def create_category(category: ExpenseCategory):
    sql = "INSERT INTO ExpensesCategory (CategoryName) VALUES (%s)"
    val = (category.CategoryName,)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"message": "Category created successfully"}

@app.get("/categories/{CategoryID}")
async def read_category(CategoryID: int = Path(..., description="Input ID")):
    mycursor.execute("SELECT * FROM ExpensesCategory WHERE CategoryID = %s", (CategoryID,))
    result = mycursor.fetchone()
    if result:
        return {"CategoryID": result[0], "CategoryName": result[1]}
    else:
        raise HTTPException(status_code=404, detail="Category not found")

@app.put("/categories/{CategoryID}")
async def update_category(CategoryID: int, category: ExpenseCategory):
    sql = "UPDATE ExpensesCategory SET CategoryName = %s WHERE CategoryID = %s"
    val = (category.CategoryName, CategoryID)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"message": "Category updated successfully"}

@app.delete("/categories/{CategoryID}")
async def delete_category(CategoryID: int):
    mycursor.execute("DELETE FROM ExpensesCategory WHERE CategoryID = %s", (CategoryID,))
    mydb.commit()
    return {"message": "Category deleted successfully"}

# CRUD untuk Metode Pembayaran
@app.post("/payment_methods/")
async def create_payment_method(method: PaymentMethod):
    sql = "INSERT INTO PaymentMethods (MethodName) VALUES (%s)"
    val = (method.MethodName,)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"message": "Payment method created successfully"}

@app.get("/payment_methods/{MethodID}")
async def read_payment_method(MethodID: int = Path(..., description="Input ID")):
    mycursor.execute("SELECT * FROM PaymentMethods WHERE MethodID = %s", (MethodID,))
    result = mycursor.fetchone()
    if result:
        return {"MethodID": result[0], "MethodName": result[1]}
    else:
        raise HTTPException(status_code=404, detail="Payment method not found")

@app.put("/payment_methods/{MethodID}")
async def update_payment_method(MethodID: int, method: PaymentMethod):
    sql = "UPDATE PaymentMethods SET MethodName = %s WHERE MethodID = %s"
    val = (method.MethodName, MethodID)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"message": "Payment method updated successfully"}

@app.delete("/payment_methods/{MethodID}")
async def delete_payment_method(MethodID: int):
    mycursor.execute("DELETE FROM PaymentMethods WHERE MethodID = %s", (MethodID,))
    mydb.commit()
    return {"message": "Payment method deleted successfully"}

# CRUD untuk Transaksi
@app.post("/transactions/")
async def create_transaction(transaction: Transaction):
    sql = "INSERT INTO Transactions (UserID, ExpensesCategoryID, Amount, TransactionDate, Description) VALUES (%s, %s, %s, %s, %s)"
    val = (transaction.UserID, transaction.ExpensesCategoryID, transaction.Amount, transaction.TransactionDate, transaction.Description)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"message": "Transaction created successfully"}

@app.get("/transactions/{TransactionID}")
async def read_transaction(TransactionID: int = Path(..., description="Input ID")):
    mycursor.execute("SELECT * FROM Transactions WHERE TransactionID = %s", (TransactionID,))
    result = mycursor.fetchone()
    if result:
        return {
            "TransactionID": result[0],
            "UserID": result[1],
            "ExpensesCategoryID": result[2],
            "Amount": result[3],
            "TransactionDate": result[4],
            "Description": result[5]
        }
    else:
        raise HTTPException(status_code=404, detail="Transaction not found")

@app.put("/transactions/{TransactionID}")
async def update_transaction(TransactionID: int, transaction: Transaction):
    sql = "UPDATE Transactions SET UserID = %s, ExpensesCategoryID = %s, Amount = %s, TransactionDate = %s, Description = %s WHERE TransactionID = %s"
    val = (transaction.UserID, transaction.ExpensesCategoryID, transaction.Amount, transaction.TransactionDate, transaction.Description, TransactionID)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"message": "Transaction updated successfully"}

@app.delete("/transactions/{TransactionID}")
async def delete_transaction(TransactionID: int):
    mycursor.execute("DELETE FROM Transactions WHERE TransactionID = %s", (TransactionID,))
    mydb.commit()
    return {"message": "Transaction deleted successfully"}

# CRUD untuk DetailPayments
@app.post("/detail_payments/")
async def create_detail_payment(detail_payment: DetailPayment):
    sql = "INSERT INTO DetailPayments (TransactionID, PaymentMethodID, AmountPaid, PaymentDate) VALUES (%s, %s, %s, %s)"
    val = (detail_payment.TransactionID, detail_payment.PaymentMethodID, detail_payment.AmountPaid, detail_payment.PaymentDate)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"message": "Detail payment created successfully"}

@app.get("/detail_payments/{PaymentID}")
async def read_detail_payment(PaymentID: int = Path(..., description="Input ID")):
    mycursor.execute("SELECT * FROM DetailPayments WHERE PaymentID = %s", (PaymentID,))
    result = mycursor.fetchone()
    if result:
        return {
            "PaymentID": result[0],
            "TransactionID": result[1],
            "PaymentMethodID": result[2],
            "AmountPaid": result[3],
            "PaymentDate": result[4]
        }
    else:
        raise HTTPException(status_code=404, detail="Detail payment not found")

@app.put("/detail_payments/{PaymentID}")
async def update_detail_payment(PaymentID: int, detail_payment: DetailPayment):
    sql = "UPDATE DetailPayments SET TransactionID = %s, PaymentMethodID = %s, AmountPaid = %s, PaymentDate = %s WHERE PaymentID = %s"
    val = (detail_payment.TransactionID, detail_payment.PaymentMethodID, detail_payment.AmountPaid, detail_payment.PaymentDate, PaymentID)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"message": "Detail payment updated successfully"}

@app.delete("/detail_payments/{PaymentID}")
async def delete_detail_payment(PaymentID: int):
    mycursor.execute("DELETE FROM DetailPayments WHERE PaymentID = %s", (PaymentID,))
    mydb.commit()
    return {"message": "Detail payment deleted successfully"}
