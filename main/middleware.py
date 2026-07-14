from django.http import Http404
from django.utils.deprecation import MiddlewareMixin


class LanguageMiddleware(MiddlewareMixin):

    def process_request(self, request):

        parts = request.path.strip("/").split("/")

        if not parts or parts == [""]:
            request.CURRENT_LANG = "uz"
            return

        # Til talab qilmaydigan URLlar
        if parts[0] in (
            "admin",
            "robots.txt",
            "sitemap.xml",
            "static",
            "media",
        ):
            request.CURRENT_LANG = "uz"
            return

        if parts[0] not in ("uz", "ru", "en"):
            raise Http404()

        request.CURRENT_LANG = parts[0]