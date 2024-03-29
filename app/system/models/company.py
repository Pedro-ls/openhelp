from app.system.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class Company(db.Model):
    __tablename__ = "companies"
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String)
    email = db.Column(db.Text, unique=True)
    password = db.Column(db.String)
    cnpj = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(2))
    photo_profile = db.Column(db.String(125))

    def __init__(self, company_name: str, email: str, password: str, city: str, state: str, photo_profile: str):
        self.company_name = company_name

        self.email = email
        self.password = generate_password_hash(password)

        self.city = city.lower()
        self.state = state.strip()
        self.photo_profile = photo_profile

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete_object(self):
        db.delete(self)
        db.session.commit()

    @classmethod
    def update_company(cls, old, new: dict):

        company_name = new.get("company_name", None)
        email = new.get("email", None)
        password = new.get("password", None)
        city = new.get("city", None)
        state = new.get("state", None)

        if company_name != None:
            old.company_name = company_name
        if email != None:
            old.email = email
        if password != None:
            old.password = generate_password_hash(password)
        if city != None:
            old.city = city
        if state != None:
            old.state = state

        old.update(new)
        db.session.commit()

    @classmethod
    def sign(cls, email: str, password: str):
        company = cls.query.filter_by(email=email).first()
        if company != None:
            if check_password_hash(company.password,  password) == True:
                return company
            return None
        else:
            return None

    @classmethod
    def getAll(cls, page=None, city="são miguel arcanjo", state="SP"):
        return cls.query.filter_by(city=city, state=state).paginate(page=page, per_page=5).items

    @classmethod
    def find(cls, company_id):
        company = cls.query.filter_by(id=company_id).first()
        return company

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self) -> str:
        return f"""
        Company<ID: {self.id}, Company name: {self.company_name}>
        """
