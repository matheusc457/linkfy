"""Linkfy - A simple CLI tool to shorten URLs"""

__version__ = '1.0.0'
__author__ = 'Matheus Campos'

from .main import main
from .database import Database
from .shortener import URLShortener

__all__ = ['main', 'Database', 'URLShortener']
