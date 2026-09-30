# School Management System

A console-based student record manager written in Python with an SQLite database. Staff log in, then add, search, list, update and delete student records that persist between runs.

## Overview
The system replaces paper registers for basic student data. It is a single-process command-line application: a login screen, a numbered menu, validated prompts, and a local `school_data.db` file that is created automatically on first run.

## Features
- Login with three role accounts and a 3-attempt limit
- **Add** a student (roll number, name, class, section, guardian phone) with duplicate-ID protection
- **Search** a student by ID
- **Show all** students (sorted, with total count)
- **Update** name / class / section / phone of an existing student
- **Delete** a student by ID
- Input validation: blank values rejected, numeric-only IDs and menu options
- Parameterised SQL queries (protects against SQL injection)
- Data stored persistently in SQLite

## Technologies / tools used
- Python 3.8+ (uses the walrus operator `:=`)
- `sqlite3` (Python standard library) - no third-party packages
- Git / GitHub for version control

## Project structure
```
school_management_system/
├── school_management.py     # application source
├── README.md
├── statement.md
├── school_data.db           # created automatically on first run
└── docs/
    ├── Project_Report.pdf
    └── diagrams/            # architecture, use case, workflow, sequence, component, ER
```

## Install & run
```bash
git clone <your-repo-url>
cd school_management_system
python school_management.py        # or: python3 school_management.py
```
No installation of extra packages is required.

**Default accounts** (change these before real use)

| Username | Password |
|----------|----------|
| Principal | Boss@123 |
| Teacher | Staff@123 |
| Student | guest2026 |

## Menu
```
1. add  2. search  3. show all  4. update  5. delete  6. exit
```

## Testing
Manual validation tests (delete `school_data.db` first for a clean start):

| # | Action | Expected result |
|---|--------|-----------------|
| 1 | Login with wrong password 3 times | `wrong username/password, N tries left`, then program exits |
| 2 | Login as `Principal` / `Boss@123` | `login successful`, menu appears |
| 3 | Add student 101 with all fields | `saved` |
| 4 | Add student 101 again | `that roll number is already taken` |
| 5 | Search 101 / search 999 | record shown / `no student with that id` |
| 6 | Show all | `total records: N` followed by the rows |
| 7 | Update 101, option 3, new value | `updated`; search shows the change |
| 8 | Update or delete a non-existent ID | `record not found` / `no such student_id` |
| 9 | Delete 101 | `deleted`; no longer listed |
| 10 | Enter `abc` at a numeric prompt; press Enter on a text prompt | `numbers only please` / `can't leave this blank` |
| 11 | Enter `7` at the menu | `not a valid choice` |

You can also drive the program non-interactively:
```bash
printf 'Principal\nBoss@123\n3\n6\n' | python school_management.py
```

## Screenshots
Add your own terminal screenshots to `docs/` (sample console output is included in the project report, section 10).

## Documentation
- `statement.md` - problem statement, scope, users, features
- `docs/Project_Report.pdf` - full project report with design diagrams

## Known limitations
Roles are not enforced per operation; passwords are stored in plain text in the source; there is no logging. See "Future Enhancements" in the report.
# School-Management-System
