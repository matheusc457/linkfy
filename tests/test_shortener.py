import unittest
from linkfy.shortener import URLShortener


class TestURLShortener(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.shortener = URLShortener()

    def test_validate_url_valid(self):
        """Test URL validation with valid URLs"""
        valid_urls = [
            "https://www.google.com",
            "http://example.com",
            "https://github.com/user/repo",
        ]

        for url in valid_urls:
            self.assertTrue(self.shortener.validate_url(url))

    def test_validate_url_invalid(self):
        """Test URL validation with invalid URLs"""
        invalid_urls = [
            "not a url",
            "ftp://example.com",  # No scheme validation for ftp
            "",
            "just-text",
        ]

        for url in invalid_urls:
            self.assertFalse(self.shortener.validate_url(url))

    def test_add_protocol(self):
        """Test adding protocol to URLs"""
        self.assertEqual(
            self.shortener.add_protocol("google.com"), "https://google.com"
        )

        self.assertEqual(
            self.shortener.add_protocol("https://google.com"), "https://google.com"
        )

        self.assertEqual(
            self.shortener.add_protocol("http://google.com"), "http://google.com"
        )

    def test_shorten_invalid_url(self):
        """Test that shortening invalid URL raises ValueError"""
        with self.assertRaises(ValueError):
            self.shortener.shorten("not a valid url")


if __name__ == "__main__":
    unittest.main()
