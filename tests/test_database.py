import unittest
import os
from linkfy.database import Database


class TestDatabase(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.test_db = "test_linkfy.db"
        self.db = Database(self.test_db)

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_create_table(self):
        """Test that table is created successfully"""
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name='links'
        """)

        result = cursor.fetchone()
        conn.close()

        self.assertIsNotNone(result)
        self.assertEqual(result[0], "links")

    def test_save_link(self):
        """Test saving a link to database"""
        link_id = self.db.save_link(
            "https://example.com", "https://tinyurl.com/test123"
        )

        self.assertIsNotNone(link_id)
        self.assertGreater(link_id, 0)

    def test_save_link_with_alias(self):
        """Test saving a link with alias"""
        link_id = self.db.save_link(
            "https://example.com", "https://tinyurl.com/test123", "myalias"
        )

        link = self.db.search_by_alias("myalias")

        self.assertIsNotNone(link)
        self.assertEqual(link[1], "https://example.com")
        self.assertEqual(link[3], "myalias")

    def test_get_all_links(self):
        """Test retrieving all links"""
        self.db.save_link("https://example1.com", "https://tinyurl.com/1")
        self.db.save_link("https://example2.com", "https://tinyurl.com/2")

        links = self.db.get_all_links()

        self.assertEqual(len(links), 2)

    def test_get_last_link(self):
        """Test retrieving the last link"""
        self.db.save_link("https://example1.com", "https://tinyurl.com/1")
        self.db.save_link("https://example2.com", "https://tinyurl.com/2")

        last_link = self.db.get_last_link()

        self.assertIsNotNone(last_link)
        self.assertEqual(last_link[1], "https://example2.com")

    def test_search_by_alias_not_found(self):
        """Test searching for non-existent alias"""
        link = self.db.search_by_alias("nonexistent")

        self.assertIsNone(link)


if __name__ == "__main__":
    unittest.main()
