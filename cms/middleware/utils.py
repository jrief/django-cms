from django.utils.deprecation import MiddlewareMixin

from cms.utils import apphook_reload


class ApphookReloadMiddleware(MiddlewareMixin):
    """
    If the URLs are stale, reload them.
    """
    def process_request(self, request):
        apphook_reload.ensure_urlconf_is_up_to_date()
        return self.get_response(request)

    async def __acall__(self, request):
        apphook_reload.ensure_urlconf_is_up_to_date()
        return await self.get_response(request)
