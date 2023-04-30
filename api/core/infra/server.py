from sanic import Sanic
from core.infra.routes import NumberConversionRoute


app = Sanic("NumberSystemConversionAPI")

app.add_route(
    NumberConversionRoute.convert_number_from_a_base_to_another_one,
    "/convert",
    methods=["POST"],
)
