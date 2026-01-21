import sqlite3
from datetime import datetime
import os


class Database:
    def __init__(self, db_path="linkfy.db"):
        """Initialize database connection"""
        self.db_path = db_path
        self.create_table()

    def get_connection(self):
        """Returns a database connection"""
        return sqlite3.connect(self.db_path)

    def create_table(self):
        """Creates the links table if it doesn't exist"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS links (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_url TEXT NOT NULL,
                shortened_url TEXT NOT NULL,
                alias TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conn.commit()
        conn.close()

    def save_link(self, original_url, shortened_url, alias=None):
        """Saves a shortened link to the database"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO links (original_url, shortened_url, alias)
            VALUES (?, ?, ?)
        """,
            (original_url, shortened_url, alias),
        )

        conn.commit()
        link_id = cursor.lastrowid
        conn.close()

        return link_id

    def get_all_links(self):
        """Returns all saved links"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, original_url, shortened_url, alias, created_at
            FROM links
            ORDER BY created_at DESC
        """)

        links = cursor.fetchall()
        conn.close()

        return links

    def get_last_link(self):
        """Returns the last shortened link"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, original_url, shortened_url, alias, created_at
            FROM links
            ORDER BY created_at DESC
            LIMIT 1
        """)

        link = cursor.fetchone()
        conn.close()

        return link

    def search_by_alias(self, alias):
        """Searches for a link by alias"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT id, original_url, shortened_url, alias, created_at
            FROM links
            WHERE alias = ?
        """,
            (alias,),
        )

        link = cursor.fetchone()
        conn.close()

        return link
