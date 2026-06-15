import sqlite3
import bcrypt
from datetime import datetime

DB_NAME = "users.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # Create users table
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, password TEXT, subscription_status TEXT, join_date TEXT)''')
    # Create usage table
    c.execute('''CREATE TABLE IF NOT EXISTS usage
                 (username TEXT, date TEXT, count INTEGER, PRIMARY KEY (username, date))''')
    conn.commit()
    conn.close()
    migrate_db() # Run migrations for updates

def hash_password(password):
    """Hash a password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(plain_password, hashed_password):
    """Verify a password against a hash."""
    try:
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    except ValueError:
        # Handle cases where existing passwords might be in legacy format (SHA256)
        # For this demo, we'll assume a fail, or you could implement a fallback check here.
        return False

def add_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", 
                  (username, hash_password(password), "free", datetime.now().strftime("%Y-%m-%d"), None))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def login_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username = ?", (username,))
    data = c.fetchone()
    conn.close()
    
    if data:
        stored_password = data[0]
        if verify_password(password, stored_password):
            return True
    return False

def get_user_subscription(username):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT subscription_status FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else "free"

def increment_usage(username):
    today = datetime.now().strftime("%Y-%m-%d")
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    # Check if record exists
    c.execute("SELECT count FROM usage WHERE username = ? AND date = ?", (username, today))
    result = c.fetchone()
    
    if result:
        new_count = result[0] + 1
        c.execute("UPDATE usage SET count = ? WHERE username = ? AND date = ?", (new_count, username, today))
    else:
        new_count = 1
        c.execute("INSERT INTO usage VALUES (?, ?, ?)", (username, today, 1))
        
    conn.commit()
    conn.close()
    return new_count

def check_usage_limit(username, limit=5):
    """Returns True if user is within limit, False if exceeded."""
    # Premium users have no limit
    if get_user_subscription(username) == "premium":
        return True
        
    today = datetime.now().strftime("%Y-%m-%d")
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT count FROM usage WHERE username = ? AND date = ?", (username, today))
    result = c.fetchone()
    conn.close()
    current_count = result[0] if result else 0
    return current_count < limit

def get_usage_count(username):
    """Returns the current daily usage count for a user."""
    today = datetime.now().strftime("%Y-%m-%d")
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT count FROM usage WHERE username = ? AND date = ?", (username, today))
    result = c.fetchone()
    conn.close()
    
    return result[0] if result else 0

# --- NEW FEATURES: ADMIN & SETTINGS ---

def migrate_db():
    """Updates database schema for new features."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute("ALTER TABLE users ADD COLUMN custom_instruction TEXT")
    except sqlite3.OperationalError:
        pass # Column likely exists
    conn.commit()
    conn.close()

def get_all_users():
    """Admin: Get all users."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT username, subscription_status, join_date FROM users")
    data = c.fetchall()
    conn.close()
    return data

def update_user_subscription(username, status):
    """Admin: Update user status."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE users SET subscription_status = ? WHERE username = ?", (status, username))
    conn.commit()
    conn.close()

def update_user_settings(username, instruction):
    """Update user custom instruction."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE users SET custom_instruction = ? WHERE username = ?", (instruction, username))
    conn.commit()
    conn.close()

def get_user_settings(username):
    """Get user custom instruction."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT custom_instruction FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None
