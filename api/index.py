"""
Vercel Serverless Function entry point for FastAPI.
Exposes the FastAPI application to Vercel's Python runtime.
"""
import sys
import json
import urllib.parse
from pathlib import Path

# Add project root to sys.path so app modules import cleanly on Vercel
ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))

from app import app as fastapi_app

class VercelPathMiddleware:
    def __init__(self, asgi_app):
        self.asgi_app = asgi_app

    def __getattr__(self, name):
        return getattr(self.asgi_app, name)

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            headers = {k.decode("latin1").lower(): v.decode("latin1") for k, v in scope.get("headers", [])}
            
            # Inspect endpoint
            if "x-inspect" in headers or scope.get("path") == "/api/inspect":
                body = json.dumps({
                    "path": scope.get("path"),
                    "query_string": scope.get("query_string", b"").decode("latin1"),
                    "headers": headers
                }, indent=2).encode("utf-8")
                await send({
                    "type": "http.response.start",
                    "status": 200,
                    "headers": [
                        [b"content-type", b"application/json"],
                        [b"content-length", str(len(body)).encode("latin1")]
                    ]
                })
                await send({
                    "type": "http.response.body",
                    "body": body,
                    "more_body": False
                })
                return

            raw_qs = scope.get("query_string", b"").decode("latin1")
            params = urllib.parse.parse_qs(raw_qs, keep_blank_values=True)
            
            if "__orig_path" in params:
                target_path = params.pop("__orig_path")[0]
                clean = "/" + target_path.lstrip("/") if target_path.strip("/") else "/"
                scope["path"] = clean
                scope["raw_path"] = clean.encode("latin1")
                new_qs = urllib.parse.urlencode(params, doseq=True)
                scope["query_string"] = new_qs.encode("latin1")
            elif scope.get("path") in ("/api/index.py", "/api/index"):
                # Try header fallback
                orig = headers.get("x-forwarded-uri") or headers.get("x-invoke-path")
                if orig and orig not in ("/api/index.py", "/api/index"):
                    clean = "/" + orig.split("?")[0].lstrip("/")
                    scope["path"] = clean
                    scope["raw_path"] = clean.encode("latin1")
                else:
                    scope["path"] = "/"
                    scope["raw_path"] = b"/"

        await self.asgi_app(scope, receive, send)

app = VercelPathMiddleware(fastapi_app)
