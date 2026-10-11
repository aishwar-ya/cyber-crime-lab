import hashlib
import os

from datetime import datetime
from pathlib import Path

from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)

from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)

from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename

from models import db, User, Case, Evidence, ChainOfCustody


# ============================================================
# APPLICATION CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

UPLOAD_DIR = BASE_DIR / "evidence_uploads"

DATABASE_PATH = BASE_DIR / "cybercrime_lab.db"

UPLOAD_DIR.mkdir(exist_ok=True)


app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY",
    "cyber-crime-lab-dev-key-change-me"
)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"sqlite:///{DATABASE_PATH.as_posix()}"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Maximum upload size: 50 MB
app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024


# ============================================================
# DATABASE
# ============================================================

db.init_app(app)


# ============================================================
# LOGIN MANAGER
# ============================================================

login_manager = LoginManager()

login_manager.login_view = "login"

login_manager.login_message = "Please log in to continue."

login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


# ============================================================
# ALLOWED FILE TYPES
# ============================================================

ALLOWED_EXTENSIONS = {
    "txt",
    "log",
    "csv",
    "json",
    "xml",
    "html",
    "pdf",
    "jpg",
    "jpeg",
    "png",
    "gif",
    "zip",
    "doc",
    "docx",
    "xls",
    "xlsx",
    "pcap",
    "evtx",
    "db",
    "sqlite",
}


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )


# ============================================================
# HASH CALCULATION
# ============================================================

def calculate_hashes(path):
    md5 = hashlib.md5()
    sha256 = hashlib.sha256()

    with open(path, "rb") as file:
        while True:
            chunk = file.read(1024 * 1024)

            if not chunk:
                break

            md5.update(chunk)
            sha256.update(chunk)

    return md5.hexdigest(), sha256.hexdigest()


# ============================================================
# FILE CATEGORY
# ============================================================

def file_category(filename):
    ext = Path(filename).suffix.lower()

    if ext in {".jpg", ".jpeg", ".png", ".gif"}:
        return "Image"

    if ext in {
        ".pdf",
        ".doc",
        ".docx",
        ".txt",
        ".csv",
        ".xls",
        ".xlsx",
    }:
        return "Document"

    if ext in {".pcap", ".evtx", ".log"}:
        return "Forensic Log"

    if ext in {".json", ".xml", ".html"}:
        return "Data"

    if ext in {".zip", ".db", ".sqlite"}:
        return "Archive/Database"

    return "Other"


# ============================================================
# SEED DEMO ADMIN
# ============================================================

def seed_admin():
    """Create a local demo admin only when no users exist."""

    if User.query.count() == 0:

        admin = User(
            name="Lab Administrator",
            email="admin@cyberlab.local",
            password_hash=generate_password_hash("admin123"),
            role="admin",
        )

        db.session.add(admin)

        db.session.commit()


# ============================================================
# CREATE DATABASE TABLES
# ============================================================

with app.app_context():
    db.create_all()
    seed_admin()


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def index():

    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))

    return render_template("index.html")


# ============================================================
# REGISTER
# ============================================================

@app.route("/register", methods=["GET", "POST"])
def register():

    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))

    if request.method == "POST":

        name = request.form.get("name", "").strip()

        email = request.form.get("email", "").strip().lower()

        password = request.form.get("password", "")

        if not name or not email or not password:

            flash(
                "All fields are required.",
                "danger"
            )

            return render_template("register.html")

        if len(password) < 6:

            flash(
                "Password must contain at least 6 characters.",
                "danger"
            )

            return render_template("register.html")

        if User.query.filter_by(email=email).first():

            flash(
                "An account with that email already exists.",
                "warning"
            )

            return render_template("register.html")

        user = User(
            name=name,
            email=email,
            password_hash=generate_password_hash(password),
            role="investigator",
        )

        db.session.add(user)

        db.session.commit()

        flash(
            "Account created. You can now log in.",
            "success"
        )

        return redirect(url_for("login"))

    return render_template("register.html")


# ============================================================
# LOGIN
# ============================================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))

    if request.method == "POST":

        email = request.form.get("email", "").strip().lower()

        password = request.form.get("password", "")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(
            user.password_hash,
            password
        ):

            login_user(user)

            flash(
                f"Welcome back, {user.name}.",
                "success"
            )

            return redirect(url_for("dashboard"))

        flash(
            "Invalid email or password.",
            "danger"
        )

    return render_template("login.html")


# ============================================================
# LOGOUT
# ============================================================

@app.route("/logout")
@login_required
def logout():

    logout_user()

    flash(
        "You have been logged out.",
        "info"
    )

    return redirect(url_for("login"))


# ============================================================
# DASHBOARD
# ============================================================

@app.route("/dashboard")
@login_required
def dashboard():

    total_cases = Case.query.count()

    open_cases = Case.query.filter_by(
        status="Open"
    ).count()

    review_cases = Case.query.filter_by(
        status="Under Review"
    ).count()

    closed_cases = Case.query.filter_by(
        status="Closed"
    ).count()

    total_evidence = Evidence.query.count()

    recent_cases = (
        Case.query
        .order_by(Case.created_at.desc())
        .limit(5)
        .all()
    )

    recent_evidence = (
        Evidence.query
        .order_by(Evidence.uploaded_at.desc())
        .limit(5)
        .all()
    )

    return render_template(
        "dashboard.html",
        total_cases=total_cases,
        open_cases=open_cases,
        review_cases=review_cases,
        closed_cases=closed_cases,
        total_evidence=total_evidence,
        recent_cases=recent_cases,
        recent_evidence=recent_evidence,
    )


# ============================================================
# CASE LIST
# ============================================================

@app.route("/cases")
@login_required
def cases():

    case_list = (
        Case.query
        .order_by(Case.created_at.desc())
        .all()
    )

    return render_template(
        "cases.html",
        cases=case_list
    )


# ============================================================
# CREATE NEW CASE
# ============================================================

@app.route("/cases/new", methods=["GET", "POST"])
@login_required
def new_case():

    if request.method == "POST":

        title = request.form.get(
            "title",
            ""
        ).strip()

        description = request.form.get(
            "description",
            ""
        ).strip()

        if not title:

            flash(
                "Case title is required.",
                "danger"
            )

            return render_template(
                "case_form.html",
                case=None
            )

        case = Case(
            title=title,
            description=description,
            status="Open",
            created_by=current_user.id,
        )

        db.session.add(case)

        db.session.commit()

        flash(
            f"Case #{case.id} created successfully.",
            "success"
        )

        return redirect(
            url_for(
                "case_detail",
                case_id=case.id
            )
        )

    return render_template(
        "case_form.html",
        case=None
    )


# ============================================================
# CASE DETAIL
# ============================================================

@app.route("/cases/<int:case_id>")
@login_required
def case_detail(case_id):

    case = db.get_or_404(
        Case,
        case_id
    )

    evidence = (
        Evidence.query
        .filter_by(case_id=case.id)
        .order_by(Evidence.uploaded_at.desc())
        .all()
    )

    custody_records = (
        ChainOfCustody.query
        .filter_by(case_id=case.id)
        .order_by(ChainOfCustody.timestamp.desc())
        .all()
    )

    return render_template(
        "case_detail.html",
        case=case,
        evidence=evidence,
        custody_records=custody_records,
    )


# ============================================================
# UPDATE CASE STATUS
# ============================================================

@app.post("/cases/<int:case_id>/status")
@login_required
def update_case_status(case_id):

    case = db.get_or_404(
        Case,
        case_id
    )

    status = request.form.get("status")

    if status not in {
        "Open",
        "Under Review",
        "Closed"
    }:

        flash(
            "Invalid case status.",
            "danger"
        )

        return redirect(
            url_for(
                "case_detail",
                case_id=case.id
            )
        )

    case.status = status

    case.closed_at = (
        datetime.utcnow()
        if status == "Closed"
        else None
    )

    db.session.commit()

    flash(
        "Case status updated.",
        "success"
    )

    return redirect(
        url_for(
            "case_detail",
            case_id=case.id
        )
    )


# ============================================================
# DELETE CASE
# ============================================================

@app.post("/cases/<int:case_id>/delete")
@login_required
def delete_case(case_id):

    case = db.get_or_404(
        Case,
        case_id
    )

    for item in case.evidence_items:

        stored = Path(item.filepath)

        if stored.exists():
            stored.unlink()

    db.session.delete(case)

    db.session.commit()

    flash(
        "Case and its evidence records were deleted.",
        "info"
    )

    return redirect(
        url_for("cases")
    )


# ============================================================
# UPLOAD DIGITAL EVIDENCE
# ============================================================

@app.post("/cases/<int:case_id>/evidence")
@login_required
def upload_evidence(case_id):

    case = db.get_or_404(
        Case,
        case_id
    )

    uploaded = request.files.get(
        "evidence"
    )

    if not uploaded or not uploaded.filename:

        flash(
            "Please select an evidence file.",
            "danger"
        )

        return redirect(
            url_for(
                "case_detail",
                case_id=case.id
            )
        )

    original_name = secure_filename(
        uploaded.filename
    )

    if not original_name:

        flash(
            "The selected filename is not valid.",
            "danger"
        )

        return redirect(
            url_for(
                "case_detail",
                case_id=case.id
            )
        )

    if not allowed_file(original_name):

        flash(
            "This file type is not allowed in the lab.",
            "danger"
        )

        return redirect(
            url_for(
                "case_detail",
                case_id=case.id
            )
        )

    case_dir = (
        UPLOAD_DIR / f"case_{case.id}"
    )

    case_dir.mkdir(
        exist_ok=True
    )

    timestamp = datetime.utcnow().strftime(
        "%Y%m%d%H%M%S%f"
    )

    stored_name = (
        f"{timestamp}_{original_name}"
    )

    destination = (
        case_dir / stored_name
    )

    uploaded.save(destination)

    md5_hash, sha256_hash = calculate_hashes(
        destination
    )

    # --------------------------------------------------------
    # CREATE EVIDENCE RECORD
    # --------------------------------------------------------

    evidence = Evidence(
        case_id=case.id,
        filename=original_name,
        filepath=str(destination),
        file_type=file_category(original_name),
        md5_hash=md5_hash,
        sha256_hash=sha256_hash,
        uploaded_by=current_user.id,
    )

    db.session.add(evidence)

    # IMPORTANT:
    # Flush sends the INSERT to the database so that
    # evidence.id is generated before we create the
    # Chain of Custody record.
    db.session.flush()

    # --------------------------------------------------------
    # CREATE CHAIN OF CUSTODY RECORD
    # --------------------------------------------------------

    custody_record = ChainOfCustody(
        case_id=case.id,
        evidence_id=evidence.id,
        evidence_filename=evidence.filename,
        user_id=current_user.id,
        action="Evidence Uploaded",
        description=(
            f"Evidence file '{original_name}' "
            "was uploaded and hashed."
        ),
    )

    db.session.add(custody_record)

    # Automatically move an Open case to Under Review
    if case.status == "Open":
        case.status = "Under Review"

    db.session.commit()

    flash(
        "Evidence uploaded and cryptographic hashes calculated.",
        "success"
    )

    return redirect(
        url_for(
            "case_detail",
            case_id=case.id
        )
    )


# ============================================================
# DOWNLOAD EVIDENCE
# ============================================================

@app.route("/evidence/<int:evidence_id>/download")
@login_required
def download_evidence(evidence_id):

    evidence = db.get_or_404(
        Evidence,
        evidence_id
    )

    path = Path(
        evidence.filepath
    )

    if not path.exists():

        flash(
            "Stored evidence file could not be found.",
            "danger"
        )

        return redirect(
            url_for(
                "case_detail",
                case_id=evidence.case_id
            )
        )

    # --------------------------------------------------------
    # RECORD EVIDENCE DOWNLOAD IN CHAIN OF CUSTODY
    # --------------------------------------------------------

    custody_record = ChainOfCustody(
        case_id=evidence.case_id,
        evidence_id=evidence.id,
        evidence_filename=evidence.filename,
        user_id=current_user.id,
        action="Evidence Downloaded",
        description=(
            f"Evidence file '{evidence.filename}' "
            "was downloaded."
        )
    )

    db.session.add(custody_record)

    db.session.commit()

    # --------------------------------------------------------
    # SEND THE EVIDENCE FILE
    # --------------------------------------------------------

    return send_from_directory(
        path.parent,
        path.name,
        as_attachment=True
    )


# ============================================================
# DELETE EVIDENCE
# ============================================================

@app.post("/evidence/<int:evidence_id>/delete")
@login_required
def delete_evidence(evidence_id):

    evidence = db.get_or_404(
        Evidence,
        evidence_id
    )

    case_id = evidence.case_id

    path = Path(
        evidence.filepath
    )

    # --------------------------------------------------------
    # RECORD DELETION IN CHAIN OF CUSTODY
    # --------------------------------------------------------

    custody_record = ChainOfCustody(
        case_id=evidence.case_id,
        evidence_id=evidence.id,
        evidence_filename=evidence.filename,
        user_id=current_user.id,
        action="Evidence Deleted",
        description=(
            f"Evidence file '{evidence.filename}' "
            "was deleted from the case."
        )
    )

    db.session.add(custody_record)

    # --------------------------------------------------------
    # DELETE THE STORED FILE
    # --------------------------------------------------------

    if path.exists():
        path.unlink()

    # --------------------------------------------------------
    # DELETE THE EVIDENCE DATABASE RECORD
    # --------------------------------------------------------

    db.session.delete(evidence)

    db.session.commit()

    flash(
        "Evidence item removed.",
        "info"
    )

    return redirect(
        url_for(
            "case_detail",
            case_id=case_id
        )
    )


# ============================================================
# GENERATE CASE PDF REPORT
# ============================================================

@app.route("/reports/case/<int:case_id>")
@login_required
def case_report(case_id):

    case = db.get_or_404(
        Case,
        case_id
    )

    # --------------------------------------------------------
    # GET EVIDENCE
    # --------------------------------------------------------

    evidence = (
        Evidence.query
        .filter_by(case_id=case.id)
        .order_by(Evidence.uploaded_at.asc())
        .all()
    )

    # --------------------------------------------------------
    # GET CHAIN OF CUSTODY RECORDS
    # --------------------------------------------------------

    custody_records = (
        ChainOfCustody.query
        .filter_by(case_id=case.id)
        .order_by(ChainOfCustody.timestamp.asc())
        .all()
    )

    # --------------------------------------------------------
    # REPORTLAB IMPORTS
    # --------------------------------------------------------

    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.units import mm
    from reportlab.platypus import (
        SimpleDocTemplate,
        Paragraph,
        Spacer,
        Table,
        TableStyle,
    )

    from xml.sax.saxutils import escape

    # --------------------------------------------------------
    # REPORT LOCATION
    # --------------------------------------------------------

    report_dir = BASE_DIR / "reports"

    report_dir.mkdir(
        exist_ok=True
    )

    report_path = (
        report_dir /
        f"case_{case.id}_report.pdf"
    )

    # --------------------------------------------------------
    # PDF STYLES
    # --------------------------------------------------------

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(
        str(report_path),
        pagesize=A4,
        rightMargin=15 * mm,
        leftMargin=15 * mm,
        topMargin=15 * mm,
        bottomMargin=15 * mm,
    )

    story = []

    # ========================================================
    # CASE INFORMATION
    # ========================================================

    story.append(
        Paragraph(
            "Cyber Crime Lab - Forensic Case Report",
            styles["Title"]
        )
    )

    story.append(
        Spacer(1, 8)
    )

    story.append(
        Paragraph(
            f"<b>Case ID:</b> {escape(str(case.id))}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Title:</b> {escape(case.title)}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Status:</b> {escape(case.status)}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Created:</b> "
            f"{case.created_at.strftime('%Y-%m-%d %H:%M UTC')}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Investigator:</b> "
            f"{escape(case.creator.name)}",
            styles["Normal"]
        )
    )

    story.append(
        Spacer(1, 8)
    )

    # ========================================================
    # DESCRIPTION
    # ========================================================

    story.append(
        Paragraph(
            "<b>Description</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            escape(
                case.description
                or "No description provided."
            ),
            styles["Normal"]
        )
    )

    story.append(
        Spacer(1, 10)
    )

    # ========================================================
    # EVIDENCE REGISTER
    # ========================================================

    story.append(
        Paragraph(
            "<b>Evidence Register</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Spacer(1, 5)
    )

    evidence_data = [
        [
            "ID",
            "Filename",
            "Type",
            "MD5",
            "SHA-256",
        ]
    ]

    for item in evidence:

        evidence_data.append(
            [
                Paragraph(
                    escape(str(item.id)),
                    styles["Normal"]
                ),

                Paragraph(
                    escape(item.filename),
                    styles["Normal"]
                ),

                Paragraph(
                    escape(item.file_type or "Other"),
                    styles["Normal"]
                ),

                Paragraph(
                    escape(item.md5_hash or "-"),
                    styles["Normal"]
                ),

                Paragraph(
                    escape(item.sha256_hash or "-"),
                    styles["Normal"]
                ),
            ]
        )

    if len(evidence_data) == 1:

        evidence_data.append(
            [
                "-",
                "No evidence",
                "-",
                "-",
                "-"
            ]
        )

    evidence_table = Table(
        evidence_data,
        repeatRows=1,
        colWidths=[
            10 * mm,
            38 * mm,
            25 * mm,
            42 * mm,
            65 * mm,
        ],
    )

    evidence_table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#172033"),
                ),

                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white,
                ),

                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold",
                ),

                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    6.5,
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey,
                ),

                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "TOP",
                ),

                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    4,
                ),

                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    4,
                ),

                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    4,
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    4,
                ),

                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [
                        colors.white,
                        colors.HexColor("#f3f6fa"),
                    ],
                ),
            ]
        )
    )

    story.append(
        evidence_table
    )

    story.append(
        Spacer(1, 12)
    )

    story.append(
        Paragraph(
            "Hash values are recorded for integrity "
            "verification of the stored evidence files.",
            styles["Italic"]
        )
    )

    story.append(
        Spacer(1, 15)
    )

    # ========================================================
    # CHAIN OF CUSTODY
    # ========================================================

    story.append(
        Paragraph(
            "<b>Chain of Custody</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Spacer(1, 5)
    )

    custody_data = [
        [
            "Date & Time",
            "Investigator",
            "Action",
            "Evidence",
            "Description",
        ]
    ]

    for record in custody_records:

        # Get investigator name
        if record.user:
            investigator_name = record.user.name
        else:
            investigator_name = "Unknown"

        # Get evidence filename.
        # The stored filename remains available even
        # after the Evidence record is deleted.
        if record.evidence_filename:
            evidence_name = record.evidence_filename
        elif record.evidence:
            evidence_name = record.evidence.filename
        else:
            evidence_name = "Unknown"

        custody_data.append(
            [
                Paragraph(
                    record.timestamp.strftime(
                        "%d %b %Y<br/>%H:%M"
                    ),
                    styles["Normal"]
                ),

                Paragraph(
                    escape(investigator_name),
                    styles["Normal"]
                ),

                Paragraph(
                    escape(record.action),
                    styles["Normal"]
                ),

                Paragraph(
                    escape(evidence_name),
                    styles["Normal"]
                ),

                Paragraph(
                    escape(
                        record.description
                        or "No description."
                    ),
                    styles["Normal"]
                ),
            ]
        )

    if len(custody_data) == 1:

        custody_data.append(
            [
                "-",
                "-",
                "-",
                "-",
                "No chain-of-custody records."
            ]
        )

    custody_table = Table(
        custody_data,
        repeatRows=1,
        colWidths=[
            27 * mm,
            28 * mm,
            32 * mm,
            30 * mm,
            63 * mm,
        ],
    )

    custody_table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#172033"),
                ),

                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white,
                ),

                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold",
                ),

                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    7,
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey,
                ),

                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "TOP",
                ),

                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    4,
                ),

                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    4,
                ),

                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    4,
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    4,
                ),

                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [
                        colors.white,
                        colors.HexColor("#f3f6fa"),
                    ],
                ),
            ]
        )
    )

    story.append(
        custody_table
    )

    story.append(
        Spacer(1, 12)
    )

    # ========================================================
    # FINAL REPORT NOTE
    # ========================================================

    story.append(
        Paragraph(
            "This report contains the recorded evidence "
            "information, cryptographic hashes, and "
            "chain-of-custody events associated with this case.",
            styles["Italic"]
        )
    )

    # ========================================================
    # BUILD PDF
    # ========================================================

    doc.build(
        story
    )

    return send_from_directory(
        report_dir,
        report_path.name,
        as_attachment=True
    )


# ============================================================
# FILE TOO LARGE ERROR
# ============================================================

@app.errorhandler(413)
def too_large(_error):

    flash(
        "File is too large. Maximum upload size is 50 MB.",
        "danger"
    )

    return redirect(
        request.referrer or url_for("dashboard")
    )


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":
    app.run(debug=True)