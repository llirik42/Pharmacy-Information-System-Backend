from .base.customer import Customer
from .base.order import Order


class CustomerOrder(Order):
    customer: Customer
