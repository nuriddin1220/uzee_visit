from django.utils.deprecation import MiddlewareMixin


class LanguageMiddleware(MiddlewareMixin):

    def process_request(self, request):

        parts = request.path.strip("/").split("/")

        lang = parts[0] if parts else "uz"

        if lang not in ["uz", "ru", "en"]:
            lang = "uz"

        request.CURRENT_LANG = lang