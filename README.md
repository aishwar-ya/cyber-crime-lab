<a name="top"></a>

<div align="center">

<h1>ðŸ•µï¸ Cyber Crime Lab</h1>

<h3>Digital Evidence Management &amp; Forensic Hash Verification</h3>

<p><i>ðŸ“ Create cases &nbsp;â€¢&nbsp; ðŸ” Hash evidence &nbsp;â€¢&nbsp; ðŸ”— Track custody &nbsp;â€¢&nbsp; ðŸ“„ Generate reports</i></p>

<br/>

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap%205-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)

![Type](https://img.shields.io/badge/Type-Academic%20Project-7E57C2?style=flat-square)
![Hashing](https://img.shields.io/badge/Hashing-MD5%20%2B%20SHA--256-2E7D32?style=flat-square)
![Reports](https://img.shields.io/badge/Reports-PDF-F5A623?style=flat-square)
![UI](https://img.shields.io/badge/UI-Cartoon%20Style-FF7AC6?style=flat-square)

<br/>

**[âœ¨ Features](#features)** &nbsp;|&nbsp;
**[ðŸ” Workflow](#workflow)** &nbsp;|&nbsp;
**[ðŸ”— Chain of Custody](#custody)** &nbsp;|&nbsp;
**[ðŸš€ Getting Started](#getting-started)** &nbsp;|&nbsp;
**[âš™ï¸ Configuration](#configuration)** &nbsp;|&nbsp;
**[âš ï¸ Academic Note](#academic-note)**

<br/>

| ðŸ”‘ **MD5 + SHA-256** | ðŸ”— **Chain of Custody** | ðŸ“„ **PDF Reports** | ðŸ“¦ **50 MB Uploads** | ðŸ—‚ï¸ **20 File Types** |
|:---:|:---:|:---:|:---:|:---:|
| Per evidence file | Upload, download, delete | One click per case | Per file limit | Auto-classified |

</div>

<br/>

<h2 align="center">ðŸ“– About</h2>

**Cyber Crime Lab** is a Flask-based academic digital forensics laboratory for managing cybercrime investigation cases and digital evidence.

It gives investigators a simple web environment to **create cases**, **upload evidence**, **calculate cryptographic hashes**, **keep a chain of custody**, and **generate forensic PDF reports**, all wrapped in a playful cartoon-style interface.

> [!NOTE]
> This is an educational prototype built for learning. See the [Academic Note](#academic-note) before using it for anything real.

<div align="right"><a href="#top">â¬† back to top</a></div>

---

<a name="features"></a>
<h2 align="center">âœ¨ Features</h2>

<table>
<tr>
<td width="33%" valign="top">

### ðŸ‘¤ Accounts
- ðŸ“ Investigator registration
- ðŸ”‘ Login and logout
- ðŸ” Passwords hashed with Werkzeug
- ðŸ›¡ï¸ Secure filenames and basic validation

</td>
<td width="33%" valign="top">

### ðŸ“ Cases
- âž• Create investigation cases
- ðŸ“ Add case descriptions
- ðŸ”„ Status: **Open**, **Under Review**, **Closed**
- ðŸ—‘ï¸ Permanently delete a case

</td>
<td width="33%" valign="top">

### ðŸ—ƒï¸ Evidence
- ðŸ“¤ Upload digital evidence
- ðŸ“‚ File type classification
- ðŸ”‘ MD5 and ðŸ” SHA-256 hashes
- ðŸ“‹ Evidence register
- â¬‡ï¸ Download and ðŸ—‘ï¸ delete

</td>
</tr>
<tr>
<td width="33%" valign="top">

### ðŸ”— Chain of Custody
- ðŸ“¤ Upload, ðŸ“¥ download and ðŸ—‘ï¸ delete are logged
- ðŸ§¾ Filenames preserved even after deletion
- ðŸ•’ Date, investigator, action, evidence, description

</td>
<td width="33%" valign="top">

### ðŸ“„ Reports
- ðŸ“‘ PDF forensic case report
- ðŸ”‘ Includes MD5 and SHA-256 hashes
- ðŸ”— Includes the Chain of Custody

</td>
<td width="33%" valign="top">

### ðŸŽ¨ Interface
- ðŸ•µï¸ Cartoon detective theme
- ðŸ“Š Investigation dashboard
- ðŸ”— Animated custody timeline
- ðŸ“± Responsive on desktop and mobile

</td>
</tr>
</table>

<div align="right"><a href="#top">â¬† back to top</a></div>

---

<a name="workflow"></a>
<h2 align="center">ðŸ” Investigation Workflow</h2>

```mermaid
flowchart LR
    A([ðŸ‘¤ Register / Login]) --> B[ðŸ“ Create case]
    B --> C[ðŸ“¤ Upload evidence]
    C --> D[ðŸ” MD5 + SHA-256 calculated]
    D --> E[ðŸ“‹ Evidence register]
    E --> F[ðŸ”— Chain of Custody updated]
    F --> G[ðŸ”„ Update case status]
    G --> H([ðŸ“„ Generate PDF report])

    style A fill:#E3F2FD,stroke:#1976D2,color:#0D47A1
    style D fill:#E8F5E9,stroke:#388E3C,color:#1B5E20
    style F fill:#F3E5F5,stroke:#7B1FA2,color:#4A148C
    style H fill:#FFF8E1,stroke:#F9A825,color:#E65100
```

1. ðŸ‘¤ Register or log in as an investigator.
2. ðŸ“ Create a new investigation case and describe what is known.
3. ðŸ“¤ Upload a digital evidence file.
4. ðŸ” The application calculates the **MD5** and **SHA-256** hashes.
5. ðŸ“‹ Review the evidence register and recorded hash values.
6. â¬‡ï¸ Download or ðŸ—‘ï¸ delete evidence when required. Every action is recorded.
7. ðŸ”„ Change the case status between *Open*, *Under Review* and *Closed*.
8. ðŸ“„ Generate the PDF forensic case report.
9. ðŸ—‘ï¸ Permanently delete a case when it is no longer needed.

<div align="right"><a href="#top">â¬† back to top</a></div>

---

<a name="custody"></a>
<h2 align="center">ðŸ”— Chain of Custody</h2>

The application keeps a record of important evidence activities.

| Icon | Action | Recorded when |
|:-:|:---|:---|
| ðŸ“¤ | **Evidence Uploaded** | A file is added to a case |
| ðŸ“¥ | **Evidence Downloaded** | A file is downloaded from a case |
| ðŸ—‘ï¸ | **Evidence Deleted** | A file is removed from a case |

Each record stores:

| Field | Description |
|:---|:---|
| ðŸ•’ **Date & Time** | When the action happened |
| ðŸ•µï¸ **Investigator** | Who performed it |
| ðŸŽ¬ **Action** | What was done |
| ðŸ“„ **Evidence** | The evidence filename |
| ðŸ’¬ **Description** | Extra details about the action |

> [!IMPORTANT]
> Evidence filenames are **permanently stored** in the custody records, so the history still names the file even after the evidence itself is deleted. When an entire case is deleted, its evidence and custody records are removed with it.

<div align="right"><a href="#top">â¬† back to top</a></div>

---

<h2 align="center">ðŸ” Digital Evidence Integrity</h2>

For every uploaded file, the application calculates two cryptographic hashes:

| Hash | Length | Purpose |
|:---|:---:|:---|
| ðŸ”‘ **MD5** | 32 characters | Quick fingerprint of the file content |
| ðŸ” **SHA-256** | 64 characters | Stronger fingerprint of the file content |

Both values are stored with the evidence record, shown in the evidence register, and included in the PDF report. They help check whether the stored file content has changed.

<details>
<summary><b>ðŸ—‚ï¸ Supported file types and classification</b></summary>

<br/>

| Category | Extensions |
|:---|:---|
| ðŸ–¼ï¸ **Image** | `jpg` `jpeg` `png` `gif` |
| ðŸ“„ **Document** | `pdf` `doc` `docx` `txt` `csv` `xls` `xlsx` |
| ðŸªµ **Forensic Log** | `pcap` `evtx` `log` |
| ðŸ§¾ **Data** | `json` `xml` `html` |
| ðŸ—„ï¸ **Archive / Database** | `zip` `db` `sqlite` |

Uploads are limited to **50 MB** per file.

</details>

<details>
<summary><b>ðŸ—„ï¸ Database structure</b></summary>

<br/>

```mermaid
erDiagram
    USER ||--o{ CASE : creates
    USER ||--o{ EVIDENCE : uploads
    USER ||--o{ CHAIN_OF_CUSTODY : performs
    CASE ||--o{ EVIDENCE : contains
    CASE ||--o{ CHAIN_OF_CUSTODY : logs
    EVIDENCE |o--o{ CHAIN_OF_CUSTODY : "referenced by"

    USER {
        int id
        string name
        string email
        string password_hash
        string role
    }
    CASE {
        int id
        string title
        text description
        string status
        datetime created_at
        datetime closed_at
    }
    EVIDENCE {
        int id
        string filename
        string file_type
        string md5_hash
        string sha256_hash
        datetime uploaded_at
    }
    CHAIN_OF_CUSTODY {
        int id
        string evidence_filename
        string action
        text description
        datetime timestamp
    }
```

</details>

<div align="right"><a href="#top">â¬† back to top</a></div>

---

<h2 align="center">ðŸ› ï¸ Technology Stack</h2>

| Technology | Purpose |
|:---|:---|
| ðŸ **Python 3.11+** | Programming language |
| ðŸŒ¶ï¸ **Flask** | Web application framework |
| ðŸ—„ï¸ **Flask-SQLAlchemy** | Database integration |
| ðŸ”‘ **Flask-Login** | Authentication and sessions |
| ðŸ’¾ **SQLite** | Database |
| ðŸ…±ï¸ **Bootstrap 5** | UI components |
| ðŸŽ¨ **HTML / CSS** | Frontend and cartoon theme |
| ðŸ“„ **ReportLab** | PDF report generation |
| ðŸ” **Werkzeug** | Password hashing and secure filenames |

---

<h2 align="center">ðŸ“‚ Project Structure</h2>

<details>
<summary><b>ðŸŒ³ Click to expand the project tree</b></summary>

```text
cyber-crime-lab/
â”‚
â”œâ”€â”€ app.py                 # Flask application and routes
â”œâ”€â”€ models.py              # Database models
â”œâ”€â”€ requirements.txt       # Python dependencies
â”œâ”€â”€ README.md
â”œâ”€â”€ .gitignore
â”‚
â”œâ”€â”€ static/
â”‚   â””â”€â”€ style.css          # Cartoon theme and animations
â”‚
â””â”€â”€ templates/
    â”œâ”€â”€ _macros.html       # Shared status badges
    â”œâ”€â”€ base.html          # Layout, navbar, footer, characters
    â”œâ”€â”€ index.html         # Home page
    â”œâ”€â”€ login.html
    â”œâ”€â”€ register.html
    â”œâ”€â”€ dashboard.html
    â”œâ”€â”€ cases.html
    â”œâ”€â”€ case_form.html
    â””â”€â”€ case_detail.html   # Evidence, hashes, custody timeline
```

These are created automatically when needed:

```text
evidence_uploads/          # Uploaded evidence files
reports/                   # Generated PDF reports
cybercrime_lab.db          # SQLite database
```

</details>

---

<a name="getting-started"></a>
<h2 align="center">ðŸš€ Getting Started</h2>

### âš™ï¸ Requirements

- âœ… [Python 3.11 or newer](https://www.python.org/downloads/)
- âœ… pip *(comes with Python)*
- âœ… A modern web browser
- âœ… Internet connection *(Bootstrap and fonts load from a CDN)*

### ðŸ“¥ Installation

**1ï¸âƒ£ Open the project folder**

```bash
cd path/to/cyber-crime-lab
```

**2ï¸âƒ£ Create a virtual environment**

```bash
python -m venv venv
```

**3ï¸âƒ£ Activate it**

```powershell
# Windows PowerShell
.\venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source venv/bin/activate
```

> ðŸ’¡ If PowerShell blocks activation, skip it and use the environment's Python directly:
> `.\venv\Scripts\python.exe -m pip install -r requirements.txt`

**4ï¸âƒ£ Install the dependencies**

```bash
python -m pip install -r requirements.txt
```

**5ï¸âƒ£ Start the application**

```bash
python app.py
```

**6ï¸âƒ£ Open it in your browser**

```text
http://127.0.0.1:5000
```

### ðŸ”‘ Demo administrator

A demo account is created automatically **only when the database has no users**.

| Email | Password |
|:---|:---|
| `admin@cyberlab.local` | `admin123` |

> [!WARNING]
> Change the demo password before using the application anywhere beyond a classroom or demonstration.

<div align="right"><a href="#top">â¬† back to top</a></div>

---

<a name="configuration"></a>
<h2 align="center">âš™ï¸ Configuration</h2>

| Setting | How to change it | Default |
|:---|:---|:---|
| ðŸ” `SECRET_KEY` | Environment variable | A built-in development key |
| ðŸ“¦ Upload limit | `MAX_CONTENT_LENGTH` in `app.py` | 50 MB |
| ðŸ—„ï¸ Database file | `DATABASE_PATH` in `app.py` | `cybercrime_lab.db` |

Set your own secret key before sharing the app:

```powershell
# Windows PowerShell
$env:SECRET_KEY = "put-a-long-random-value-here"
```

```bash
# macOS / Linux
export SECRET_KEY="put-a-long-random-value-here"
```

> [!CAUTION]
> The app starts with `debug=True`, which is meant for development only. Do not run it that way on a public server.

The `.gitignore` already excludes `*.db`, `evidence_uploads/`, `reports/`, `venv/` and `.env`, so your database and evidence files are not uploaded to GitHub by accident.

---

<h2 align="center">ðŸ“„ Forensic Case Reports</h2>

The PDF report is a summary of the investigation and contains:

| Section | Included |
|:---|:---|
| ðŸ“ **Case details** | Case ID, title, status, investigator, description |
| ðŸ—ƒï¸ **Evidence register** | Filenames and file types |
| ðŸ” **Hashes** | MD5 and SHA-256 for each evidence file |
| ðŸ”— **Chain of Custody** | The recorded custody history |

Reports are saved in the `reports/` folder.

---



<a name="academic-note"></a>
<h2 align="center">âš ï¸ Important Academic Note</h2>

> [!WARNING]
> This project is an **educational** digital-forensics and evidence-management prototype. It is **not** a replacement for professional forensic tools or procedures.

Hashes help show whether stored file content has changed, but a real forensic workflow also needs:

- âœ”ï¸ Proper evidence acquisition procedures
- âœ”ï¸ Write-blocking where appropriate
- âœ”ï¸ Secure evidence storage and access controls
- âœ”ï¸ Detailed audit logging
- âœ”ï¸ Evidence preservation procedures
- âœ”ï¸ Validated forensic tools
- âœ”ï¸ Appropriate legal authorization

---

<h2 align="center">ðŸ“š Purpose</h2>

The project was developed as a learning application to demonstrate:

`ðŸ•µï¸ Cybercrime investigation` Â· `ðŸ—ƒï¸ Digital evidence management` Â· `ðŸ” Cryptographic hashing` Â· `ðŸ”— Chain of custody` Â· `ðŸ›¡ï¸ Evidence preservation` Â· `ðŸŒ Web-based case management` Â· `ðŸ“„ Forensic reporting`

---

<h2 align="center">ðŸ”® Future Enhancement Ideas</h2>

- [ ] ðŸ” Search and filter cases
- [ ] âœ… A "verify hash" button to re-check a stored file
- [ ] ðŸ‘¥ Role-based access (admin and investigator)
- [ ] ðŸ“Š Export custody history as CSV
- [ ] ðŸ”” Notifications for status changes

---

<h2 align="center">ðŸ‘©â€ðŸ’» Author</h2>

<div align="center">

**Aiswarya**

[![GitHub](https://img.shields.io/badge/GitHub-aishwar--ya-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/aishwar-ya)

</div>

---

<div align="center">

### ðŸ›¡ï¸ Investigate â€¢ Verify â€¢ Protect

If you like this project, please consider giving it a â­

**[â¬† Back to top](#top)**

</div>
