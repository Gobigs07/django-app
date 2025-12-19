import psycopg2
from django.http import JsonResponse
import os

def db_check(request):
    try:
        conn = psycopg2.connect(
            host=os.getenv("EXTERNAL_POSTGRES_HOST"),
            port=os.getenv("EXTERNAL_POSTGRES_PORT"),
            dbname=os.getenv("EXTERNAL_POSTGRES_DB"),
            user=os.getenv("EXTERNAL_POSTGRES_USER"),
            password=os.getenv("EXTERNAL_POSTGRES_PASSWORD"),
            connect_timeout=5
        )
        conn.close()
        return JsonResponse({"db": "connected"})
    except Exception as e:
        return JsonResponse({"db": "failed", "error": str(e)}, status=500)
