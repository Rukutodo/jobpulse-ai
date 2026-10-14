"""
Vercel Serverless Function entry point for FastAPI.
Exposes the FastAPI application to Vercel's Python runtime and ensures
exact path and query parameter routing when Vercel rewrites are in effect.
"""
import sys
import urllib.parse
from pathlib import Path

# Add project root to sys.path so app modules import cleanly on Vercel
ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))

from app import app as fastapi_app

class VercelPathMiddleware:
    """
    ASGI middleware ensuring that Vercel internal rewrites preserve
    exact request paths and query parameters.
    """
    def __init__(self, asgi_app):
        self.asgi_app = asgi_app

    def __getattr__(self, name):
        return getattr(self.asgi_app, name)

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            raw_qs = scope.get("query_string", b"").decode("latin1")
            params = urllib.parse.parse_qs(raw_qs, keep_blank_values=True)
            
            # Check if Vercel passed the original path via rewrite
            if "__orig_path" in params:
                target_path = params.pop("__orig_path")[0]
                if not target_path or target_path == "/":
                    scope["path"] = "/"
                    scope["raw_path"] = b"/"
                else:
                    clean = target_path if target_path.startswith("/") else f"/{target_path}"
                    scope["path"] = clean
                    scope["raw_path"] = clean.encode("latin1")
                
                # Rebuild query string without __orig_path
                new_qs = urllib.parse.urlencode(params, doseq=True)
                scope["query_string"] = new_qs.encode("latin1")
            elif scope.get("path") in ("/api/index.py", "/api/index", "/api/"):
                scope["path"] = "/"
                scope["raw_path"] = b"/"

        await self.asgi_app(scope, receive, send)

app = VercelPathMiddleware(fastapi_app)
