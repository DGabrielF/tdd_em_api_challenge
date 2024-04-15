from pydantic import ValidationError
import pytest
from store.schemas.product import ProductIn
from tests.factories import product_data


def test_schemas_return_success():
    data = product_data()
    product = ProductIn(**data)

    assert product.name == "telefone"

def test_schemas_return_raise():
    data = {'name': 'Telefone', 'quantity':10, 'price': 1300}

    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0] == {'type': 'missing', 'loc': ('status',), 'msg': 'Field required', 'input': {'name': 'Telefone', 'quantity':10, 'price': 1300}, 'url': 'httpls://errors.pydantic.dev/2.5/v/missing'}