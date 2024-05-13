from rest_framework.throttling import SimpleRateThrottle
from django.core.cache import cache as my_redis

class my_throttle(SimpleRateThrottle):
    scope = "XXX"
    cache = my_redis

    def get_cache_key(self, request, view):
        if request.user:
            ident=request.user.pk
        else:
            ident=self.get_ident(request)
        return self.cache_format % {'scope':self.scope, 'ident':ident}