from sanic import Sanic

from core.infra.cors import CORS
from core.infra.options import Options
from core.infra.routes import NumberConversionRoute

app = Sanic("NumberSystemConversionAPI")

app.register_listener(Options.setup_options, "before_server_start")
app.register_middleware(CORS.add_cors_headers, "response")
app.add_route(
    NumberConversionRoute.convert_number_from_a_base_to_another_one,
    "/convert",
    methods=["POST"],
)
