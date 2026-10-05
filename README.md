<a name="top"></a>

<div align="center">

<h1>&#x1F575;&#xFE0F; Cyber Crime Lab</h1>

<h3>Digital Evidence Management &amp; Forensic Hash Verification</h3>

<p><i>&#x1F4C1; Create cases &nbsp;&#x2022;&nbsp; &#x1F510; Hash evidence &nbsp;&#x2022;&nbsp; &#x1F517; Track custody &nbsp;&#x2022;&nbsp; &#x1F4C4; Generate reports</i></p>

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

**[&#x2728; Features](#features)** &nbsp;|&nbsp;
**[&#x1F50D; Workflow](#workflow)** &nbsp;|&nbsp;
**[&#x1F517; Chain of Custody](#custody)** &nbsp;|&nbsp;
**[&#x1F680; Getting Started](#getting-started)** &nbsp;|&nbsp;
**[&#x2699;&#xFE0F; Configuration](#configuration)** &nbsp;|&nbsp;
**[&#x1F4F8; Screenshots](#screenshots)** &nbsp;|&nbsp;
**[&#x26A0;&#xFE0F; Academic Note](#academic-note)**

<br/>

| &#x1F511; **MD5 + SHA-256** | &#x1F517; **Chain of Custody** | &#x1F4C4; **PDF Reports** | &#x1F4E6; **50 MB Uploads** | &#x1F5C2;&#xFE0F; **20 File Types** |
|:---:|:---:|:---:|:---:|:---:|
| Per evidence file | Upload, download, delete | One click per case | Per file limit | Auto-classified |

</div>

<br/>

<h2 align="center">&#x1F4D6; About</h2>

**Cyber Crime Lab** is a Flask-based academic digital forensics laboratory for managing cybercrime investigation cases and digital evidence.

It gives investigators a simple web environment to **create cases**, **upload evidence**, **calculate cryptographic hashes**, **keep a chain of custody**, and **generate forensic PDF reports**, all wrapped in a playful cartoon-style interface.

> [!NOTE]
> This is an educational prototype built for learning. See the [Academic Note](#academic-note) before using it for anything real.

<div align="right"><a href="#top">&#x2B06; back to top</a></div>

---

<a name="features"></a>
<h2 align="center">&#x2728; Features</h2>

<table>
<tr>
<td width="33%" valign="top">

### &#x1F464; Accounts

- &#x1F4DD; Investigator registration
- &#x1F511; Login and logout
- &#x1F510; Passwords hashed with Werkzeug
- &#x1F6E1;&#xFE0F; Secure filenames and basic validation

</td>
<td width="33%" valign="top">

### &#x1F4C1; Cases

- &#x2795; Create investigation cases
- &#x1F4DD; Add case descriptions
- &#x1F504; Status: **Open**, **Under Review**, **Closed**
- &#x1F5D1;&#xFE0F; Permanently delete a case

</td>
<td width="33%" valign="top">

### &#x1F5C3;&#xFE0F; Evidence

- &#x1F4E4; Upload digital evidence
- &#x1F4C2; File type classification
- &#x1F511; MD5 and &#x1F510; SHA-256 hashes
- &#x1F4CB; Evidence register
- &#x2B07;&#xFE0F; Download and &#x1F5D1;&#xFE0F; delete

</td>
</tr>
<tr>
<td width="33%" valign="top">

### &#x1F517; Chain of Custody

- &#x1F4E4; Upload, &#x1F4E5; download and &#x1F5D1;&#xFE0F; delete are logged
- &#x1F9FE; Filenames preserved even after deletion
- &#x1F552; Date, investigator, action, evidence, description

</td>
<td width="33%" valign="top">

### &#x1F4C4; Reports

- &#x1F4D1; PDF forensic case report
- &#x1F511; Includes MD5 and SHA-256 hashes
- &#x1F517; Includes the Chain of Custody

</td>
<td width="33%" valign="top">

### &#x1F3A8; Interface

- &#x1F575;&#xFE0F; Cartoon detective theme
- &#x1F4CA; Investigation dashboard
- &#x1F517; Animated custody timeline
- &#x1F4F1; Responsive on desktop and mobile

</td>
</tr>
</table>

<div align="right"><a href="#top">&#x2B06; back to top</a></div>

---

<a name="workflow"></a>
<h2 align="center">&#x1F50D; Investigation Workflow</h2>

```mermaid
flowchart LR
    A(["#128100; Register / Login"]) --> B["#128193; Create case"]
    B --> C["#128228; Upload evidence"]
    C --> D["#128272; MD5 + SHA-256 calculated"]
    D --> E["#128203; Evidence register"]
    E --> F["#128279; Chain of Custody updated"]
    F --> G["#128260; Update case status"]
    G --> H(["#128196; Generate PDF report"])

    style A fill:#E3F2FD,stroke:#1976D2,color:#0D47A1
    style D fill:#E8F5E9,stroke:#388E3C,color:#1B5E20
    style F fill:#F3E5F5,stroke:#7B1FA2,color:#4A148C
    style H fill:#FFF8E1,stroke:#F9A825,color:#E65100
```

### Investigation Steps

1. &#x1F464; Register or log in as an investigator.
2. &#x1F4C1; Create a new investigation case and describe what is known.
3. &#x1F4E4; Upload a digital evidence file.
4. &#x1F510; The application calculates the **MD5** and **SHA-256** hashes.
5. &#x1F4CB; Review the evidence register and recorded hash values.
6. &#x2B07;&#xFE0F; Download or &#x1F5D1;&#xFE0F; delete evidence when required. Every action is recorded.
7. &#x1F504; Change the case status between **Open**, **Under Review** and **Closed**.
8. &#x1F4C4; Generate the PDF forensic case report.
9. &#x1F5D1;&#xFE0F; Permanently delete a case when it is no longer needed.

<div align="right"><a href="#top">&#x2B06; back to top</a></div>

---

<a name="custody"></a>
<h2 align="center">&#x1F517; Chain of Custody</h2>

The application keeps a record of important evidence activities.

| Icon | Action | Recorded when |
|:-:|:---|:---|
| &#x1F4E4; | **Evidence Uploaded** | A file is added to a case |
| &#x1F4E5; | **Evidence Downloaded** | A file is downloaded from a case |
| &#x1F5D1;&#xFE0F; | **Evidence Deleted** | A file is removed from a case |

### Custody Information

Each record stores:

| Field | Description |
|:---|:---|
| &#x1F552; **Date & Time** | When the action happened |
| &#x1F575;&#xFE0F; **Investigator** | Who performed it |
| &#x1F3AC; **Action** | What was done |
| &#x1F4C4; **Evidence** | The evidence filename |
| &#x1F4AC; **Description** | Extra details about the action |

> [!IMPORTANT]
> Evidence filenames are **permanently stored** in the custody records, so the history still names the file even after the evidence itself is deleted. When an entire case is deleted, its evidence and custody records are removed with it.

<div align="right"><a href="#top">&#x2B06; back to top</a></div>

---

<h2 align="center">&#x1F510; Digital Evidence Integrity</h2>

For every uploaded file, the application calculates two cryptographic hashes:

| Hash | Length | Purpose |
|:---|:---:|:---|
| &#x1F511; **MD5** | 32 characters | Quick fingerprint of the file content |
| &#x1F510; **SHA-256** | 64 characters | Stronger fingerprint of the file content |

Both values are stored with the evidence record, shown in the evidence register, and included in the PDF report. They help check whether the stored file content has changed.

<details>
<summary><b>&#x1F5C2;&#xFE0F; Supported file types and classification</b></summary>

<br/>

| Category | Extensions |
|:---|:---|
| &#x1F5BC;&#xFE0F; **Image** | `jpg` `jpeg` `png` `gif` |
| &#x1F4C4; **Document** | `pdf` `doc` `docx` `txt` `csv` `xls` `xlsx` |
| &#x1FAB5; **Forensic Log** | `pcap` `evtx` `log` |
| &#x1F9FE; **Data** | `json` `xml` `html` |
| &#x1F5C4;&#xFE0F; **Archive / Database** | `zip` `db` `sqlite` |

Uploads are limited to **50 MB** per file.

</details>

<details>
<summary><b>&#x1F5C4;&#xFE0F; Database structure</b></summary>

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
        datetime created_at
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

<div align="right"><a href="#top">&#x2B06; back to top</a></div>

---

<h2 align="center">&#x1F6E0;&#xFE0F; Technology Stack</h2>

| Technology | Purpose |
|:---|:---|
| &#x1F40D; **Python 3.11+** | Programming language |
| &#x1F336;&#xFE0F; **Flask** | Web application framework |
| &#x1F5C4;&#xFE0F; **Flask-SQLAlchemy** | Database integration |
| &#x1F511; **Flask-Login** | Authentication and sessions |
| &#x1F4BE; **SQLite** | Database |
| &#x1F171;&#xFE0F; **Bootstrap 5** | UI components |
| &#x1F3A8; **HTML / CSS** | Frontend and cartoon theme |
| &#x1F4C4; **ReportLab** | PDF report generation |
| &#x1F510; **Werkzeug** | Password hashing and secure filenames |

---

<h2 align="center">&#x1F4C2; Project Structure</h2>

<details>
<summary><b>&#x1F333; Click to expand the project tree</b></summary>

```text
cyber-crime-lab/
|
|-- app.py                 # Flask application and routes
|-- models.py              # Database models
|-- requirements.txt       # Python dependencies
|-- README.md
|-- .gitignore
|
|-- static/
|   `-- style.css          # Cartoon theme and animations
|
|-- screenshots/
|   |-- 01_home.png
|   |-- 02_login.png
|   |-- 03_dashboard.png
|   |-- 04_cases.png
|   |-- 05_case_detail.png
|   `-- 06_custody.png
|
`-- templates/
    |-- _macros.html       # Shared status badges
    |-- base.html          # Layout, navbar, footer, characters
    |-- index.html
    |-- login.html
    |-- register.html
    |-- dashboard.html
    |-- cases.html
    |-- case_form.html
    `-- case_detail.html   # Evidence, hashes, custody timeline
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
<h2 align="center">&#x1F680; Getting Started</h2>

### &#x2699;&#xFE0F; Requirements

- &#x2705; [Python 3.11 or newer](https://www.python.org/downloads/)
- &#x2705; pip *(comes with Python)*
- &#x2705; A modern web browser
- &#x2705; Internet connection *(Bootstrap and fonts load from a CDN)*

### &#x1F4E5; Installation

**1&#xFE0F;&#x20E3; Open the project folder**

```bash
cd path/to/cyber-crime-lab
```

**2&#xFE0F;&#x20E3; Create a virtual environment**

```bash
python -m venv venv
```

**3&#xFE0F;&#x20E3; Activate the virtual environment**

```powershell
# Windows PowerShell
.\venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source venv/bin/activate
```

> [!TIP]
> If PowerShell blocks activation, skip it and run pip through the environment's Python instead:
> `.\venv\Scripts\python.exe -m pip install -r requirements.txt`

**4&#xFE0F;&#x20E3; Install the dependencies**

```bash
python -m pip install -r requirements.txt
```

**5&#xFE0F;&#x20E3; Start the application**

```bash
python app.py
```

**6&#xFE0F;&#x20E3; Open it in your browser**

```text
http://127.0.0.1:5000
```

### &#x1F511; Demo Administrator

A demo account is created automatically **only when the database has no users**.

| Email | Password |
|:---|:---|
| `admin@cyberlab.local` | `admin123` |

> [!WARNING]
> Change the demo password before using the application anywhere beyond a classroom or demonstration.

<div align="right"><a href="#top">&#x2B06; back to top</a></div>

---

<a name="configuration"></a>
<h2 align="center">&#x2699;&#xFE0F; Configuration</h2>

| Setting | How to change it | Default |
|:---|:---|:---|
| &#x1F510; `SECRET_KEY` | Environment variable | Built-in development key |
| &#x1F4E6; Upload limit | `MAX_CONTENT_LENGTH` in `app.py` | 50 MB |
| &#x1F5C4;&#xFE0F; Database file | `DATABASE_PATH` in `app.py` | `cybercrime_lab.db` |

Set your own secret key before sharing the application:

```powershell
# Windows PowerShell
$env:SECRET_KEY = "put-a-long-random-value-here"
```

```bash
# macOS / Linux
export SECRET_KEY="put-a-long-random-value-here"
```

> [!CAUTION]
> The application starts with `debug=True`, which is intended for development only. Do not run it this way on a public server.

The `.gitignore` excludes database files, uploaded evidence, reports, virtual environments and environment files, so they are not uploaded to GitHub by accident.

---

<h2 align="center">&#x1F4C4; Forensic Case Reports</h2>

The generated PDF report contains:

| Section | Included |
|:---|:---|
| &#x1F4C1; **Case details** | Case ID, title, status, investigator and description |
| &#x1F5C3;&#xFE0F; **Evidence register** | Evidence filenames and file types |
| &#x1F510; **Hashes** | MD5 and SHA-256 values |
| &#x1F517; **Chain of Custody** | Recorded custody history |

Reports are saved in the `reports/` folder.

---

<a name="screenshots"></a>
<h2 align="center">&#x1F4F8; Screenshots</h2>

<table>
<tr>
<td align="center">
<img src="screenshots/01_home.png" width="420" alt="Home page"/>
<br/><b>&#x1F3E0; Home Page</b>
</td>
<td align="center">
<img src="screenshots/02_login.png" width="420" alt="Login page"/>
<br/><b>&#x1F510; Login Page</b>
</td>
</tr>
<tr>
<td align="center">
<img src="screenshots/03_dashboard.png" width="420" alt="Investigation dashboard"/>
<br/><b>&#x1F4CA; Investigation Dashboard</b>
</td>
<td align="center">
<img src="screenshots/04_cases.png" width="420" alt="Investigation cases"/>
<br/><b>&#x1F4C1; Investigation Cases</b>
</td>
</tr>
<tr>
<td align="center">
<img src="screenshots/05_case_detail.png" width="420" alt="Case details and digital evidence"/>
<br/><b>&#x1F50E; Case Details &amp; Digital Evidence</b>
</td>
<td align="center">
<img src="screenshots/06_custody.png" width="420" alt="Chain of custody timeline"/>
<br/><b>&#x1F517; Chain of Custody</b>
</td>
</tr>
</table>

<div align="right"><a href="#top">&#x2B06; back to top</a></div>

---

<a name="academic-note"></a>
<h2 align="center">&#x26A0;&#xFE0F; Important Academic Note</h2>

> [!WARNING]
> This project is an **educational** digital-forensics and evidence-management prototype. It is **not** a replacement for professional forensic tools or procedures.

Hashes help show whether stored file content has changed, but a real forensic workflow also needs:

- &#x2714;&#xFE0F; Proper evidence acquisition procedures
- &#x2714;&#xFE0F; Write-blocking where appropriate
- &#x2714;&#xFE0F; Secure evidence storage and access controls
- &#x2714;&#xFE0F; Detailed audit logging
- &#x2714;&#xFE0F; Evidence preservation procedures
- &#x2714;&#xFE0F; Validated forensic tools
- &#x2714;&#xFE0F; Appropriate legal authorization

---

<h2 align="center">&#x1F4DA; Purpose</h2>

The project was developed as a learning application to demonstrate:

&#x1F575;&#xFE0F; `Cybercrime investigation` &#xB7; &#x1F5C3;&#xFE0F; `Digital evidence management` &#xB7; &#x1F510; `Cryptographic hashing` &#xB7; &#x1F517; `Chain of custody` &#xB7; &#x1F6E1;&#xFE0F; `Evidence preservation` &#xB7; &#x1F310; `Web-based case management` &#xB7; &#x1F4C4; `Forensic reporting`

---

<h2 align="center">&#x1F52E; Future Enhancement Ideas</h2>

- [ ] &#x1F50D; Search and filter cases
- [ ] &#x2705; Verify hash button to re-check a stored file
- [ ] &#x1F465; Role-based access
- [ ] &#x1F4CA; Export custody history as CSV
- [ ] &#x1F514; Notifications for status changes

---

<h2 align="center">&#x1F469;&#x200D;&#x1F4BB; Author</h2>

<div align="center">

**Aiswarya**

[![GitHub](https://img.shields.io/badge/GitHub-aishwar--ya-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/aishwar-ya)

</div>

---

<div align="center">

### &#x1F6E1;&#xFE0F; Investigate &#x2022; Verify &#x2022; Protect

If you like this project, please consider giving it a &#x2B50;

**[&#x2B06; Back to top](#top)**

</div>
