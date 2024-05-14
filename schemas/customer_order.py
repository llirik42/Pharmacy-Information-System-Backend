from .base.order import Order
from .base.customer import Customer


class CustomerOrder(Order):
    customer: Customer
