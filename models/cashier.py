import db_models
from db_models import *

class Cashier_Models:
    def __init__(self, first_name, last_name, phone_number,password,email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.password = password

    def create(self):
        cashier = db_models.Cashier(firstname=self.first_name,lastname=self.last_name,phone=self.phone_number
                                    ,password=self.password,email=self.email)
        session.add(cashier)
        session.commit()

    def __repr__(self) -> str:
            return f"""
        First Name: {self.first_name}
        Last Name: {self.last_name}
        Phone Number: 09{self.phone_number}
        Email Address: {self.email if self.email else '-'}
    """
    @classmethod
    def delete(cls,phone):
        session.query(Cashier).filter(Cashier.phone == phone).delete()
        session.commit()

    def all_cashiers(self):
        cashiers = Cashier.query.all()
        for c in cashiers:
            return c.firstname + c.lastname

    @classmethod
    def check_user(cls, phone_number: str, password: str) :
        if session.query(Cashier).fliter(Cashier.phone == phone_number and Cashier.password == password):
            return True
        return False


c = Cashier_Models('ali','reza','09376051315','ali','ali')
c.create()