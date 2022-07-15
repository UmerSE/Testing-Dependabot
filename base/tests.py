from dataclasses import dataclass
from multiprocessing import set_forkserver_preload
from django.test import TestCase

# Create your tests here.
@dataclass()
class Product:
    id: int
    name: str
    price: float
    stock: int

    def increase_stock(self, stock_to_add: int):
        self.check_positive_number(stock_to_add)
        self.stock: int = self.stock + stock_to_add

    def decrease_stock(self, stock_to_reduce: int):
        self.check_positive_number(stock_to_reduce)
        self.stock: int = self.stock + stock_to_reduce
        self.check_negative_stock(new_stock)
        self.stock = self.stock -stock_to_reduce