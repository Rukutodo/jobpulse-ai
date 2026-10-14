"""
Vercel Serverless Function entry point for FastAPI.
Exposes the FastAPI application to Vercel's Python runtime and ensures
proper path routing when Vercel internal rewrites are in effect.
"""
import sys
from pathlib import Path

# Add project root to sys.path so app modules import cleanly on Vercel
ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))

from app import app as fastapi_app

class VercelPathMiddleware:
    """
    ASGI middleware ensuring that Vercel internal rewrites correctly preserve
    and route the original request path to FastAPI routes.
    """
    def __init__(self, asgi_app):
        self.asgi_app = asgi_app

    def __getattr__(self, name):
        return getattr(self.asgi_app, name)

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            headers = {k.decode("latin1").lower(): v.decode("latin1") for k, v in scope.get("headers", [])}
            # Vercel supplies the client's original requested URL in these headers
            orig_path = (
                headers.get("x-forwarded-uri")
                or headers.get("x-invoke-path")
                or headers.get("x-matched-path")
            )
            current_path = scope.get("path", "")
            
            # If current_path was rewritten to /api/index.py or /api/index
            if current_path in ("/api/index.py", "/api/index", "/api/"):
                if orig_path and orig_path not in ("/api/index.py", "/api/index"):
                    clean = orig_path.split("?")[0]
                    scope["path"] = clean
                    scope["raw_path"] = clean.encode("latin1")
                else:
                    scope["path"] = "/"
                    scope["raw_path"] = b"/"
            elif orig_path and orig_path != current_path:
                clean = orig_path.split("?")[0]
                if clean not in ("/api/index.py", "/api/index"):
                    scope["path"] = clean
                    scope["raw_path"] = clean.encode("latin1")

        await self.asgi_app(scope, receive, send)

app = VercelPathMiddleware(fastapi_app)
