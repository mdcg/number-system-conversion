from sanic.response import json

from core.usecase.base_converter import BaseConverter


class NumberConversionRoute:
    @staticmethod
    async def convert_number_from_a_base_to_another_one(request):
        payload = request.json
        try:
            converted_value = BaseConverter.process(
                from_base=payload.get("fromBase"),
                to_base=payload.get("toBase"),
                value=payload.get("value"),
            )
        except Exception as err:
            return json({"msg": str(err)}, status=400)

        return json({"value": converted_value}, status=200)
