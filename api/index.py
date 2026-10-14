"""
Vercel Serverless Function entry point for FastAPI.
Exposes the FastAPI application to Vercel's Python runtime.
"""
import sys
from pathlib import Path

# Add project root to sys.path so app modules import cleanly on Vercel
ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))

from app import app
