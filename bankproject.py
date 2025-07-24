import os
import sys
import firebase_admin
from firebase_admin import credentials, firestore, firestore_async
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QMainWindow, QVBoxLayout, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSignal

if not firebase_admin._apps:
    try:
        cred_path = r"C:\Users\Dell\OneDrive\Documents\SITC internship\firebasekey.json"
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
        print("Firebase Initialized Successfully.")
    except Exception as e:
        print(f"Error initializing Firebase: {e}")
        app = QApplication([])
        QMessageBox.critical(None, "Fatal Error", f"Could not initialize Firebase. The application will close.\nError: {e}")
        sys.exit(1)
db = firestore.client()
class UserSession:
    def __init__(self):
        self.account_id = None
        self.name = None
        self.balance = 0.0
    def login(self, account_id, user_data):
        self.account_id = account_id
        self.name = user_data.get('name', 'N/A')
        self.balance = user_data.get('balance', 0.0)
    def logout(self):
        self.name = None
        self.balance = 0.0
    def is_logged_in(self):
        return self.account_id is not None
    def update_balance(self, new_balance):
        self.balance = new_balance
class MainWindow(QMainWindow):
    def __init__(self, session):
        super().__init__()
        self.session = session
        self.setWindowTitle("🏦Bank of Tamil Nadu - Main Menu🏦")
        self.setGeometry(400, 400, 400, 400)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        vbox = QVBoxLayout()
        self.welcome_label = QLabel("🛕Welcome to the Bank of Tamil Nadu 🛕")
        self.welcome_label.setStyleSheet("background-color:green; font-weight: bold")
        self.status_label = QLabel("Please log in or create an account.")
        self.balance_label = QLabel()
        self.create_account_button = QPushButton("Create Account📚")
        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet("background-color:blue; font-weight: bold")
        self.deposit_button = QPushButton("Deposit📩")
        self.withdraw_button = QPushButton("Withdraw📤")
        self.transfer_button = QPushButton("Money Transfer💱")
        self.logout_button = QPushButton("Logout")
        vbox.addWidget(self.welcome_label)
        vbox.addWidget(self.status_label)
        vbox.addWidget(self.balance_label)
        vbox.addSpacing(20)
        vbox.addWidget(self.create_account_button)
        vbox.addWidget(self.login_button)
        vbox.addWidget(self.deposit_button)
        vbox.addWidget(self.withdraw_button)
        vbox.addWidget(self.transfer_button)
        vbox.addWidget(self.logout_button)
        self.central_widget.setLayout(vbox)
        self.create_account_button.clicked.connect(self.open_create_account_window)
        self.login_button.clicked.connect(self.open_login_window)
        self.logout_button.clicked.connect(self.handle_logout)
        self.deposit_button.clicked.connect(self.open_deposit_window)
        self.withdraw_button.clicked.connect(self.open_withdraw_window)
        self.transfer_button.clicked.connect(self.open_transfer_window)
        self.update_ui_for_logout()
    def update_ui_for_login(self):
        self.welcome_label.setText(f"Welcome, {self.session.name}!")
        self.status_label.setText(f"Account ID: {self.session.account_id}")
        self.balance_label.setText(f"Current Balance: ₹{self.session.balance:.2f}")
        self.login_button.setEnabled(False)
        self.create_account_button.setEnabled(False)
        self.logout_button.setEnabled(True)
        self.deposit_button.setEnabled(True)
        self.withdraw_button.setEnabled(True)
        self.transfer_button.setEnabled(True)
    def update_ui_for_logout(self):
        self.session.logout()
        self.welcome_label.setText("Welcome to the Bank of Tamil Nadu")
        self.status_label.setText("Please log in or create an account.")
        self.balance_label.setText("")
        self.login_button.setEnabled(True)
        self.create_account_button.setEnabled(True)
        self.logout_button.setEnabled(False)
        self.deposit_button.setEnabled(False)
        self.withdraw_button.setEnabled(False)
        self.transfer_button.setEnabled(False)
    def open_create_account_window(self):
        self.create_window = CreateAccountWindow(self.session)
        self.create_window.show()

    def open_login_window(self):
        self.login_window = LoginWindow(self.session)
        self.login_window.login_successful.connect(self.update_ui_for_login)
        self.login_window.show()

    def handle_logout(self):
        self.update_ui_for_logout()
        QMessageBox.information(self, "Logged Out", "You have been successfully logged out.")
        
    def refresh_balance_display(self):
        self.balance_label.setText(f"Current Balance: ₹{self.session.balance:.2f}")

    def open_deposit_window(self):
        self.deposit_win = DepositWindow(self.session)
        self.deposit_win.transaction_done.connect(self.refresh_balance_display)
        self.deposit_win.show()

    def open_withdraw_window(self):
        self.withdraw_win = WithdrawWindow(self.session)
        self.withdraw_win.transaction_done.connect(self.refresh_balance_display)
        self.withdraw_win.show()
        
    def open_transfer_window(self):
        self.transfer_win = MoneyTransferWindow(self.session)
        self.transfer_win.transaction_done.connect(self.refresh_balance_display)
        self.transfer_win.show()
class CreateAccountWindow(QWidget):
    def __init__(self, session):
        super().__init__()
        self.session = session
        self.setWindowTitle("Create New Account")
        
        vbox = QVBoxLayout()
        self.account_id_input = QLineEdit()
        self.account_id_input.setPlaceholderText("Enter a unique Account ID (e.g., user123)")
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter your full name")
        self.create_button = QPushButton("Create Account")
        
        vbox.addWidget(QLabel("Account ID:"))
        vbox.addWidget(self.account_id_input)
        vbox.addWidget(QLabel("Your Name:"))
        vbox.addWidget(self.name_input)
        vbox.addWidget(self.create_button)
        self.setLayout(vbox)
        
        self.create_button.clicked.connect(self.save_account_to_firestore)

    def save_account_to_firestore(self):
        account_id = self.account_id_input.text().strip()
        name = self.name_input.text().strip()

        if not account_id or not name:
            QMessageBox.warning(self, "Input Error", "Account ID and Name cannot be empty.")
            return

        user_ref = db.collection("users").document(account_id)
        
        if user_ref.get().exists:
            QMessageBox.warning(self, "Error", f"An account with the ID '{account_id}' already exists.")
            return

        
        user_data = {
            "name": name,
            "balance": 0.0,
            "transactions": []
        }

       
        try:
            user_ref.set(user_data)
            QMessageBox.information(self, "Success", f"Account for {name} created successfully!")
            self.close() 

        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Could not create account: {e}")


class LoginWindow(QWidget):
    
    login_successful = pyqtSignal()

    def __init__(self, session):
        super().__init__()
        self.session = session
        self.setWindowTitle("Login")

        vbox = QVBoxLayout()
        self.login_id_input = QLineEdit()
        self.login_id_input.setPlaceholderText("Enter your Account ID")
        self.login_button = QPushButton("Login")
        
        vbox.addWidget(QLabel("Account ID:"))
        vbox.addWidget(self.login_id_input)
        vbox.addWidget(self.login_button)
        self.setLayout(vbox)
        
        self.login_button.clicked.connect(self.attempt_login)

    def attempt_login(self):
        account_id = self.login_id_input.text().strip()
        if not account_id:
            QMessageBox.warning(self, "Input Error", "Please enter an Account ID.")
            return

        user_ref = db.collection("users").document(account_id)
        
        try:
            user_doc = user_ref.get()
            if user_doc.exists:
                user_data = user_doc.to_dict()
                
                self.session.login(account_id, user_data)
                QMessageBox.information(self, "Login Successful", f"Welcome back, {self.session.name}!")
                
                self.login_successful.emit()
                self.close()
            else:
                QMessageBox.warning(self, "Login Failed", "Account not found. Please check the ID.")
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred during login: {e}")


class DepositWindow(QWidget):
    transaction_done = pyqtSignal()
    
    def __init__(self, session):
        super().__init__()
        self.session = session
        self.setWindowTitle("Deposit Funds")
        
        vbox = QVBoxLayout()
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Enter amount to deposit")
        self.deposit_button = QPushButton("Deposit")
        
        vbox.addWidget(QLabel(f"Depositing to account: {self.session.account_id}"))
        vbox.addWidget(QLabel("Amount:"))
        vbox.addWidget(self.amount_input)
        vbox.addWidget(self.deposit_button)
        self.setLayout(vbox)
        
        self.deposit_button.clicked.connect(self.perform_deposit)

    def perform_deposit(self):
        try:
            amount = float(self.amount_input.text())
            if amount <= 0:
                raise ValueError("Deposit amount must be positive.")
        except ValueError as e:
            QMessageBox.warning(self, "Invalid Input", f"Please enter a valid positive number.\n{e}")
            return

        user_ref = db.collection("users").document(self.session.account_id)

        
        @firestore.transactional
        def update_in_transaction(transaction, doc_ref, deposit_amount):
            snapshot = doc_ref.get(transaction=transaction)
            old_balance = snapshot.get('balance')
            new_balance = old_balance + deposit_amount
            transaction.update(doc_ref, {'balance': new_balance})
            return new_balance

        try:
            transaction = db.transaction()
            final_balance = update_in_transaction(transaction, user_ref, amount)
            
            self.session.update_balance(final_balance)
            QMessageBox.information(self, "Success", f"Deposited ₹{amount:.2f}.\nNew balance: ₹{self.session.balance:.2f}")
            self.transaction_done.emit()
            self.close()

        except Exception as e:
            QMessageBox.critical(self, "Transaction Failed", f"Could not complete deposit: {e}")


class WithdrawWindow(QWidget):
    transaction_done = pyqtSignal()

    def __init__(self, session):
        super().__init__()
        self.session = session
        self.setWindowTitle("Withdraw Funds")
        
        vbox = QVBoxLayout()
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Enter amount to withdraw")
        self.withdraw_button = QPushButton("Withdraw")
        
        vbox.addWidget(QLabel(f"Withdrawing from: {self.session.account_id}"))
        vbox.addWidget(QLabel(f"Current Balance: ₹{self.session.balance:.2f}"))
        vbox.addWidget(QLabel("Amount:"))
        vbox.addWidget(self.amount_input)
        vbox.addWidget(self.withdraw_button)
        self.setLayout(vbox)
        
        self.withdraw_button.clicked.connect(self.perform_withdrawal)

    def perform_withdrawal(self):
        try:
            amount = float(self.amount_input.text())
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive.")
        except ValueError as e:
            QMessageBox.warning(self, "Invalid Input", f"Please enter a valid positive number.\n{e}")
            return

        user_ref = db.collection("users").document(self.session.account_id)

        @firestore.transactional
        def update_in_transaction(transaction, doc_ref, withdraw_amount):
            snapshot = doc_ref.get(transaction=transaction)
            old_balance = snapshot.get('balance')
            
            if old_balance < withdraw_amount:
                
                raise ValueError("Insufficient funds for this withdrawal.")
                
            new_balance = old_balance - withdraw_amount
            transaction.update(doc_ref, {'balance': new_balance})
            return new_balance

        try:
            transaction = db.transaction()
            final_balance = update_in_transaction(transaction, user_ref, amount)
            
            self.session.update_balance(final_balance)
            QMessageBox.information(self, "Success", f"Withdrew ₹{amount:.2f}.\nNew balance: ₹{self.session.balance:.2f}")
            self.transaction_done.emit()
            self.close()

        except ValueError as e: 
             QMessageBox.critical(self, "Transaction Failed", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Transaction Failed", f"Could not complete withdrawal: {e}")


class MoneyTransferWindow(QWidget):
    transaction_done = pyqtSignal()

    def __init__(self, session):
        super().__init__()
        self.session = session
        self.setWindowTitle("Transfer Money")

        vbox = QVBoxLayout()
        self.recipient_input = QLineEdit()
        self.recipient_input.setPlaceholderText("Recipient's Account ID")
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Amount to transfer")
        self.transfer_button = QPushButton("Transfer")

        vbox.addWidget(QLabel(f"Your Account: {self.session.account_id}"))
        vbox.addWidget(QLabel(f"Current Balance: ₹{self.session.balance:.2f}"))
        vbox.addSpacing(10)
        vbox.addWidget(QLabel("Recipient ID:"))
        vbox.addWidget(self.recipient_input)
        vbox.addWidget(QLabel("Amount:"))
        vbox.addWidget(self.amount_input)
        vbox.addWidget(self.transfer_button)
        self.setLayout(vbox)

        self.transfer_button.clicked.connect(self.perform_transfer)

    def perform_transfer(self):
        recipient_id = self.recipient_input.text().strip()
        try:
            amount = float(self.amount_input.text())
            if amount <= 0:
                raise ValueError("Transfer amount must be positive.")
        except ValueError as e:
            QMessageBox.warning(self, "Invalid Input", f"Please enter a valid amount.\n{e}")
            return
        
        if not recipient_id:
            QMessageBox.warning(self, "Invalid Input", "Please enter a recipient ID.")
            return

        if recipient_id == self.session.account_id:
            QMessageBox.warning(self, "Invalid Operation", "You cannot transfer money to yourself.")
            return

        sender_ref = db.collection("users").document(self.session.account_id)
        recipient_ref = db.collection("users").document(recipient_id)

        @firestore.transactional
        def transfer_transaction(transaction, amount_to_transfer):
        
            sender_doc = sender_ref.get(transaction=transaction)
            if not sender_doc.exists:
                raise Exception("Your account could not be found.")
            
            sender_balance = sender_doc.get('balance')
            if sender_balance < amount_to_transfer:
                raise ValueError("Insufficient funds.")

            recipient_doc = recipient_ref.get(transaction=transaction)
            if not recipient_doc.exists:
                raise ValueError(f"Recipient account '{recipient_id}' not found.")
            
            recipient_balance = recipient_doc.get('balance')

            new_sender_balance = sender_balance - amount_to_transfer
            new_recipient_balance = recipient_balance + amount_to_transfer
            
            transaction.update(sender_ref, {'balance': new_sender_balance})
            transaction.update(recipient_ref, {'balance': new_recipient_balance})
            
            return new_sender_balance

        try:
            transaction = db.transaction()
            final_sender_balance = transfer_transaction(transaction, amount)
            
            self.session.update_balance(final_sender_balance)
            QMessageBox.information(self, "Success", f"Transferred ₹{amount:.2f} to {recipient_id}.\nYour new balance is ₹{self.session.balance:.2f}")
            self.transaction_done.emit()
            self.close()

        except (ValueError, Exception) as e:
            QMessageBox.critical(self, "Transfer Failed", str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    current_session = UserSession()
    main_app_window = MainWindow(current_session)
    main_app_window.show()
    sys.exit(app.exec_())