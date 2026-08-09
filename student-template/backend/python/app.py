```python
from flask import Flask, jsonify
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")


@app.route("/api/inventory/alerts", methods=["GET"])
def get_alerts():
    """
    Return inventory products where quantity is less than
    or equal to the reorder level.
    """
    if not DATABASE_URL:
        return jsonify({
            "error": "DATABASE_URL environment variable is not configured"
        }), 500

    connection = None

    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(DATABASE_URL)

        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("""
                SELECT *
                FROM inventory
                WHERE quantity <= reorder_level
            """)

            products = cursor.fetchall()

        return jsonify(products), 200

    except psycopg2.Error as error:
        return jsonify({
            "error": "Database error",
            "message": str(error)
        }), 500

    except Exception as error:
        return jsonify({
            "error": "Unexpected server error",
            "message": str(error)
        }), 500

    finally:
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```
