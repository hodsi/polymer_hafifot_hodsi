import random

from flask import Flask, Blueprint
import json

from backend.entities.api_result import APIResult
from backend.entities.product import Product

blueprint = Blueprint('products', __name__)


@blueprint.route('/api/products')
def get_products():
    products = [
        Product(1, "i7 computer", 60, "A solid computer with an i7 processor"),
        Product(2, "Atvash Ayosh", 2, "A 7-day vacation at selected settlements across Ayosh"),
        Product(3, "Gil's Ptorim", 999, "Exclusive Ptorim"),
        Product(4, "Massage by Tomer", 85, "One of the best masseuse in the country. Or at least in Tesla."),
        Product(5, "Corona", 1, "What doesn't kill you makes you sick")
    ]
    return json.dumps({
        "products": [product.dictify() for product in products]
    })


@blueprint.route('/api/products_')
def get_products_():
    should_api_request_work = random.randint(0, 1)
    if not should_api_request_work:
        return APIResult("error", json.dumps({
            "message": "Something's Not Working"
        })).dictify()
    products = [
        Product(1, "i7 computer", 60, "A solid computer with an i7 processor"),
        Product(2, "Atvash Ayosh", 2, "A 7-day vacation at selected settlements across Ayosh"),
        Product(3, "Gil's Ptorim", 999, "Exclusive Ptorim"),
        Product(4, "Massage by Tomer", 85, "One of the best masseuse in the country. Or at least in Tesla."),
        Product(5, "Corona", 1, "What doesn't kill you makes you sick")
    ]
    dictified_products = json.dumps({
        "products": [product.dictify() for product in products]
    })
    return APIResult("success", dictified_products).dictify()
