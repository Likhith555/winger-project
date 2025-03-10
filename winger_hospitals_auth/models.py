from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_bcrypt import Bcrypt
from sqlalchemy.sql import func

db = SQLAlchemy()
bcrypt = Bcrypt()

# =================== USER TABLE ===================
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(10), nullable=False)  # "admin", "doctor", "patient"

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

# =================== DOCTORS TABLE ===================
class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    mobile = db.Column(db.String(15), nullable=False)
    specialization = db.Column(db.String(100), nullable=False)
    
    consultations = db.relationship("ConsultationRequest", backref="doctor", lazy=True)

# =================== PATIENTS TABLE ===================
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    mobile = db.Column(db.String(15), nullable=False)
    blood_group = db.Column(db.String(10), nullable=False)
    
    consultations = db.relationship("ConsultationRequest", backref="patient", lazy=True)

# =================== CONSULTATION REQUEST TABLE ===================
class ConsultationRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.id"), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctor.id"), nullable=True)
    status = db.Column(db.String(20), default="Pending")  # Pending, Assigned, Completed
    disease_info = db.Column(db.Text, nullable=False)
    mobile = db.Column(db.String(15), nullable=False)
    created_at = db.Column(db.DateTime, default=func.now())

    comments = db.relationship("Comment", backref="consultation", lazy=True, cascade="all, delete")

# =================== CONSULTATION COMMENTS TABLE ===================
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    consultation_id = db.Column(db.Integer, db.ForeignKey("consultation_request.id"), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctor.id"), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=func.now())
    doctor = db.relationship("Doctor", backref="comments",lazy=True)
# =================== DATABASE INITIALIZATION ===================
def init_db(app):
    with app.app_context():
        db.init_app(app)
        db.create_all()
