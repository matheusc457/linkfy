#!/usr/bin/env python3
"""
Linkfy - A simple CLI tool to shorten URLs
"""

import sys
import argparse
from .database import Database
from .shortener import URLShortener

try:
    import pyperclip

    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False


def shorten_url(url, alias=None, copy=False):
    """Shorten a URL and save to database"""
    db = Database()
    shortener = URLShortener()

    try:
        # Add protocol if missing
        url = shortener.add_protocol(url)

        # Shorten URL
        print(f"Shortening URL: {url}")
        shortened = shortener.shorten(url)

        # Save to database
        db.save_link(url, shortened, alias)

        # Display result
        print(f"\n✓ Shortened URL: {shortened}")

        if alias:
            print(f"  Alias: {alias}")

        # Copy to clipboard if requested
        if copy and CLIPBOARD_AVAILABLE:
            pyperclip.copy(shortened)
            print("  (Copied to clipboard)")
        elif copy and not CLIPBOARD_AVAILABLE:
            print("  (Clipboard not available - install pyperclip)")

        return shortened

    except ValueError as e:
        print(f"✗ Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Error: {e}")
        sys.exit(1)


def show_history(limit=None):
    """Show history of shortened URLs"""
    db = Database()
    links = db.get_all_links()

    if not links:
        print("No links found in history.")
        return

    print(
        f"\n{'ID':<5} {'Original URL':<40} {'Shortened URL':<30} {'Alias':<15} {'Date':<20}"
    )
    print("-" * 110)

    displayed = 0
    for link in links:
        link_id, original, shortened, alias, created = link
        alias_display = alias if alias else "-"

        # Truncate long URLs for display
        original_display = original[:37] + "..." if len(original) > 40 else original

        print(
            f"{link_id:<5} {original_display:<40} {shortened:<30} {alias_display:<15} {created:<20}"
        )

        displayed += 1
        if limit and displayed >= limit:
            break


def show_last():
    """Show the last shortened URL"""
    db = Database()
    link = db.get_last_link()

    if not link:
        print("No links found in history.")
        return

    link_id, original, shortened, alias, created = link

    print(f"\nLast shortened URL:")
    print(f"  Original:  {original}")
    print(f"  Shortened: {shortened}")
    if alias:
        print(f"  Alias:     {alias}")
    print(f"  Date:      {created}")


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Linkfy - A simple CLI tool to shorten URLs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  linkfy https://example.com
  linkfy https://example.com --alias mylink
  linkfy https://example.com --copy
  linkfy --history
  linkfy --last
        """,
    )

    parser.add_argument("url", nargs="?", help="URL to shorten")
    parser.add_argument("--alias", "-a", help="Custom alias for the shortened URL")
    parser.add_argument(
        "--copy", "-c", action="store_true", help="Copy shortened URL to clipboard"
    )
    parser.add_argument(
        "--history", action="store_true", help="Show history of shortened URLs"
    )
    parser.add_argument("--last", action="store_true", help="Show last shortened URL")
    parser.add_argument("--limit", type=int, help="Limit number of results in history")

    args = parser.parse_args()

    # Show history
    if args.history:
        show_history(args.limit)
        return

    # Show last
    if args.last:
        show_last()
        return

    # Shorten URL
    if args.url:
        shorten_url(args.url, args.alias, args.copy)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
