import sqlite3

from django.conf import settings
from django.core.management.base import BaseCommand


def _clean_text(value):
    if value is None:
        return None
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="ignore")
    # If it's already str, ensure it is valid UTF-8 by round-tripping.
    return value.encode("utf-8", errors="ignore").decode("utf-8", errors="ignore")


class Command(BaseCommand):
    help = "Fix invalid UTF-8 bytes in sqlite text columns (news and comments)."

    def handle(self, *args, **options):
        engine = settings.DATABASES.get("default", {}).get("ENGINE", "")
        if engine != "django.db.backends.sqlite3":
            self.stderr.write(
                "This command currently supports only sqlite3. "
                f"Detected engine: {engine}"
            )
            return

        db_path = settings.DATABASES["default"]["NAME"]
        conn = sqlite3.connect(db_path)
        # Return raw bytes for text so we can decode safely
        conn.text_factory = bytes
        cur = conn.cursor()

        updates = 0

        def fix_table(table, columns):
            nonlocal updates
            col_list = ", ".join(columns)
            cur.execute(f"SELECT id, {col_list} FROM {table}")
            rows = cur.fetchall()
            for row in rows:
                row_id = row[0]
                raw_vals = row[1:]
                cleaned = [_clean_text(v) for v in raw_vals]
                if list(raw_vals) != cleaned:
                    set_clause = ", ".join([f"{c}=?" for c in columns])
                    cur.execute(
                        f"UPDATE {table} SET {set_clause} WHERE id=?",
                        (*cleaned, row_id),
                    )
                    updates += 1

        # Core content tables likely to affect detail pages
        fix_table(
            "news_app_news",
            [
                "title",
                "title_uz",
                "title_uz_cyrl",
                "body",
                "body_uz",
                "body_uz_cyrl",
                "author",
                "author_uz",
                "author_uz_cyrl",
            ],
        )
        fix_table(
            "news_app_comment",
            [
                "body",
            ],
        )

        conn.commit()
        conn.close()

        self.stdout.write(f"Done. Updated rows: {updates}")
