from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="investigator")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    cases = db.relationship("Case", backref="creator", lazy=True)

    def __repr__(self):
        return f"<User {self.email} ({self.role})>"


class Case(db.Model):
    __tablename__ = "cases"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), nullable=False, default="Open")
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    closed_at = db.Column(db.DateTime, nullable=True)

    evidence_items = db.relationship(
        "Evidence",
        backref="case",
        lazy=True,
        cascade="all, delete-orphan"
    )

    # Automatically remove Chain of Custody records
    # when a case is permanently deleted.
    custody_records = db.relationship(
        "ChainOfCustody",
        backref="case",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Case {self.id}: {self.title} [{self.status}]>"


class Evidence(db.Model):
    __tablename__ = "evidence"

    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, db.ForeignKey("cases.id"), nullable=False)
    filename = db.Column(db.String(255), nullable=False)
    filepath = db.Column(db.String(500), nullable=False)
    file_type = db.Column(db.String(50), nullable=True)
    md5_hash = db.Column(db.String(32), nullable=True)
    sha256_hash = db.Column(db.String(64), nullable=True)
    uploaded_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

    uploader = db.relationship(
        "User",
        foreign_keys=[uploaded_by]
    )

    def __repr__(self):
        return f"<Evidence {self.filename} (Case {self.case_id})>"


class ChainOfCustody(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    case_id = db.Column(
        db.Integer,
        db.ForeignKey("cases.id"),
        nullable=False
    )

    evidence_id = db.Column(
        db.Integer,
        db.ForeignKey("evidence.id"),
        nullable=True
    )

    # Stores the filename permanently so that
    # the custody history still knows the filename
    # even if the Evidence record is deleted.
    evidence_filename = db.Column(
        db.String(255),
        nullable=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    action = db.Column(
        db.String(100),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    timestamp = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    user = db.relationship(
        "User",
        foreign_keys=[user_id]
    )

    evidence = db.relationship(
        "Evidence",
        foreign_keys=[evidence_id]
    )

    def __repr__(self):
        return (
            f"<ChainOfCustody "
            f"{self.action} - "
            f"{self.evidence_filename}>"
        )