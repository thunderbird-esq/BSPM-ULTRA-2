import sqlite3
import json
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

DB_FILE = "gbstudio_hub.db"

def get_db_connection():
    """Creates and returns a database connection."""
    try:
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        logging.error(f"Database connection failed: {e}")
        return None

def initialize_database():
    """Initializes the database and creates tables if they don't exist."""
    conn = get_db_connection()
    if conn is None:
        logging.error("Could not get database connection for initialization.")
        return
        
    try:
        with conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS conversations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    user_message TEXT NOT NULL,
                    agent_response TEXT NOT NULL
                );
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS assets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_name TEXT NOT NULL,
                    asset_type TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    final_prompt TEXT,
                    source_path TEXT,
                    status TEXT NOT NULL DEFAULT 'generated'
                );
            """)
        logging.info("Database initialized successfully.")
    except sqlite3.Error as e:
        logging.error(f"Database initialization failed: {e}")
    finally:
        conn.close()

def update_asset_status(asset_id: int, status: str) -> bool:
    """Updates the status of an asset in the database."""
    conn = get_db_connection()
    if conn is None:
        logging.error("Could not get database connection for updating asset status.")
        return False
    
    try:
        with conn:
            cursor = conn.execute(
                "UPDATE assets SET status = ? WHERE id = ?",
                (status, asset_id)
            )
            if cursor.rowcount == 0:
                logging.warning(f"Attempted to update status for non-existent asset ID: {asset_id}")
                return False
        logging.info(f"Updated asset {asset_id} to status '{status}'")
        return True
    except sqlite3.Error as e:
        logging.error(f"Failed to update asset status for ID {asset_id}: {e}")
        return False
    finally:
        conn.close()

def get_asset(asset_id: int):
    """Retrieves a single asset's data from the database."""
    conn = get_db_connection()
    if conn is None:
        return None
    
    try:
        asset = conn.execute("SELECT * FROM assets WHERE id = ?", (asset_id,)).fetchone()
        return asset
    except sqlite3.Error as e:
        logging.error(f"Failed to retrieve asset ID {asset_id}: {e}")
        return None
    finally:
        conn.close()

def get_approved_assets() -> list:
    """Retrieves all assets with the status 'approved'."""
    conn = get_db_connection()
    if conn is None:
        return []

    try:
        assets = conn.execute("SELECT * FROM assets WHERE status = 'approved'").fetchall()
        return assets
    except sqlite3.Error as e:
        logging.error(f"Failed to retrieve approved assets: {e}")
        return []
    finally:
        conn.close()

def update_asset_source_path(asset_id: int, source_path: str) -> bool:
    """Updates the source_path of an asset in the database."""
    conn = get_db_connection()
    if conn is None:
        logging.error("Could not get database connection for updating asset source path.")
        return False
    
    try:
        with conn:
            cursor = conn.execute(
                "UPDATE assets SET source_path = ? WHERE id = ?",
                (source_path, asset_id)
            )
            if cursor.rowcount == 0:
                logging.warning(f"Attempted to update source path for non-existent asset ID: {asset_id}")
                return False
        logging.info(f"Updated asset {asset_id} with source_path '{source_path}'")
        return True
    except sqlite3.Error as e:
        logging.error(f"Failed to update asset source path for ID {asset_id}: {e}")
        return False
    finally:
        conn.close()

def log_chat_message(user_message: str, agent_response: str):
    """Logs a user message and an agent's response to the database."""
    logging.info(f"Attempting to log chat message: {user_message}")
    conn = get_db_connection()
    if conn is None:
        logging.error("Could not get database connection for logging chat message.")
        return

    try:
        with conn:
            conn.execute(
                "INSERT INTO conversations (timestamp, user_message, agent_response) VALUES (?, ?, ?)",
                (datetime.now().isoformat(), user_message, agent_response)
            )
        logging.info(f"Successfully logged chat message.")
    except sqlite3.Error as e:
        logging.error(f"Failed to log chat message: {e}")
    finally:
        conn.close()

def log_asset_creation(task_name: str, asset_type: str, final_prompt: str, source_path: str) -> int:
    """Logs the creation of a new asset and returns the new asset's ID."""
    conn = get_db_connection()
    if conn is None:
        logging.error("Could not get database connection for logging asset creation.")
        return -1

    try:
        with conn:
            cursor = conn.execute(
                "INSERT INTO assets (task_name, asset_type, timestamp, final_prompt, source_path, status) VALUES (?, ?, ?, ?, ?, ?)",
                (task_name, asset_type, datetime.now().isoformat(), final_prompt, source_path, 'generated')
            )
            new_id = cursor.lastrowid
            logging.info(f"Logged creation of asset '{task_name}' with ID {new_id}")
            return new_id
    except sqlite3.Error as e:
        logging.error(f"Failed to log asset creation for '{task_name}': {e}")
        return -1
    finally:
        conn.close()
