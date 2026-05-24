from .models import Translation


def return_title(lang, key):
    try:
        if not lang or not key:
            return key

        row = (
            Translation.objects
            .filter(key=key)
            .values("en", "ru", "uz")
            .first()
        )

        if not row:
            return key

        value = row.get(lang)

        return value if value else key

    except Exception:
        return key