"""
SQLite database storage for tracking job applications, statuses, and notes.
"""
import sqlite3
import os
from pathlib import Path
import time
from typing import List, Dict, Any, Optional

if os.environ.get("VERCEL"):
    DB_PATH = Path("/tmp/jobsearch.db")
else:
    DB_PATH = Path(__file__).parent / "jobsearch.db"

def get_connection():
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id TEXT,
                title TEXT NOT NULL,
                company TEXT NOT NULL,
                location TEXT DEFAULT 'Remote',
                salary TEXT DEFAULT 'Not Disclosed',
                url TEXT,
                source TEXT DEFAULT 'Manual',
                status TEXT DEFAULT 'Saved',
                match_score INTEGER DEFAULT 0,
                notes TEXT DEFAULT '',
                applied_date TEXT DEFAULT '',
                created_at TEXT DEFAULT (datetime('now', 'localtime')),
                updated_at TEXT DEFAULT (datetime('now', 'localtime'))
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS saved_analyses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                company TEXT NOT NULL,
                jd_text TEXT NOT NULL,
                analysis_json TEXT NOT NULL,
                created_at TEXT DEFAULT (datetime('now', 'localtime'))
            );
        """)
        conn.commit()

def save_application(data: Dict[str, Any]) -> int:
    init_db()
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # Check if already saved
        cursor.execute("SELECT id FROM applications WHERE company = ? AND title = ?", 
                       (data.get("company", "").strip(), data.get("title", "").strip()))
        existing = cursor.fetchone()
        if existing:
            # Update status or match score
            cursor.execute("""
                UPDATE applications 
                SET match_score = coalesce(?, match_score),
                    updated_at = datetime('now', 'localtime')
                WHERE id = ?
            """, (data.get("match_score"), existing["id"]))
            conn.commit()
            return existing["id"]
        
        cursor.execute("""
            INSERT INTO applications 
            (job_id, title, company, location, salary, url, source, status, match_score, notes, applied_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data.get("job_id", ""),
            data.get("title", "").strip(),
            data.get("company", "").strip(),
            data.get("location", "Remote"),
            data.get("salary", "Not Disclosed"),
            data.get("url", ""),
            data.get("source", "Manual"),
            data.get("status", "Saved"),
            data.get("match_score", 0),
            data.get("notes", ""),
            data.get("applied_date", "")
        ))
        conn.commit()
        return cursor.lastrowid

def get_applications(status: Optional[str] = None) -> List[Dict[str, Any]]:
    init_db()
    with get_connection() as conn:
        cursor = conn.cursor()
        if status and status.lower() != "all":
            cursor.execute("SELECT * FROM applications WHERE status = ? ORDER BY id DESC", (status,))
        else:
            cursor.execute("SELECT * FROM applications ORDER BY id DESC")
        rows = cursor.fetchall()
        return [dict(r) for r in rows]

def update_application(app_id: int, updates: Dict[str, Any]) -> bool:
    init_db()
    allowed = ["status", "notes", "applied_date", "salary"]
    set_clause = []
    values = []
    for k in allowed:
        if k in updates:
            set_clause.append(f"{k} = ?")
            values.append(updates[k])
            
    if not set_clause:
        return False
        
    set_clause.append("updated_at = datetime('now', 'localtime')")
    values.append(app_id)
    
    with get_connection() as conn:
        cursor = conn.cursor()
        sql = f"UPDATE applications SET {', '.join(set_clause)} WHERE id = ?"
        cursor.execute(sql, values)
        conn.commit()
        return cursor.rowcount > 0

def delete_application(app_id: int) -> bool:
    init_db()
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM applications WHERE id = ?", (app_id,))
        conn.commit()
        return cursor.rowcount > 0

def get_stats() -> Dict[str, int]:
    init_db()
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT status, count(*) as cnt FROM applications GROUP BY status")
        counts = {r["status"]: r["cnt"] for r in cursor.fetchall()}
        
        cursor.execute("SELECT count(*) as total FROM applications")
        total = cursor.fetchone()["total"]
        
        return {
            "total": total,
            "saved": counts.get("Saved", 0),
            "applied": counts.get("Applied", 0),
            "interviewing": counts.get("Interviewing", 0),
            "offer": counts.get("Offer", 0),
            "rejected": counts.get("Rejected", 0)
        }
