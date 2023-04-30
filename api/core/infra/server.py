from sanic import Sanic
from core.infra.routes import NumberConversionRoute
from core.infra.cors import add_cors_headers
from core.infra.options import setup_options


app = Sanic("NumberSystemConversionAPI")

app.register_listener(setup_options, "before_server_start")
app.register_middleware(add_cors_headers, "response")
app.add_route(
    NumberConversionRoute.convert_number_from_a_base_to_another_one,
    "/convert",
    methods=["POST"],
)
