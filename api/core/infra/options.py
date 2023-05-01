from collections import defaultdict

from sanic import response

from core.infra.cors import CORS


class Options:
    @staticmethod
    def _compile_routes_needing_options(routes):
        needs_options = defaultdict(list)

        for route in routes.values():
            if "OPTIONS" not in route.methods:
                needs_options[route.uri].extend(route.methods)

        return {
            uri: frozenset(methods)
            for uri, methods in dict(needs_options).items()  # noqa
        }

    @staticmethod
    def _options_wrapper(handler, methods):
        def wrapped_handler(request, *args, **kwargs):
            return handler(request, methods)

        return wrapped_handler

    @staticmethod
    async def options_handler(request, methods):
        resp = response.empty()
        CORS._add_cors_headers(resp, methods)

        return resp

    @classmethod
    def setup_options(cls, app, *args, **kwargs):
        app.router.reset()
        needs_options = cls._compile_routes_needing_options(
            app.router.routes_all
        )  # noqa

        for uri, methods in needs_options.items():
            app.add_route(
                cls._options_wrapper(cls.options_handler, methods),
                uri,
                methods=["OPTIONS"],
            )

        app.router.finalize()
