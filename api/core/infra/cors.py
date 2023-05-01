class CORS:
    @staticmethod
    def _add_cors_headers(response, methods):
        allow_methods = set(methods)
        allow_methods.add("OPTIONS")

        headers = {
            "Access-Control-Allow-Methods": ",".join(allow_methods),
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": "true",
            "Access-Control-Allow-Headers": "origin, content-type, accept, authorization, x-xsrf-token, x-request-id",  # noqa
        }
        response.headers.update(headers)

    @classmethod
    def add_cors_headers(cls, request, response):
        if request.method != "OPTIONS":
            methods = request.route.methods
            cls._add_cors_headers(response, methods)
