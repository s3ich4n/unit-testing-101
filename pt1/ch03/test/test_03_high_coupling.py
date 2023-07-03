from collections import namedtuple


Product = namedtuple("Product", "merch count")


class Store:
    def __init__(
            self,
            item: Product,
    ) -> None:
        self.item: Product = item

    def sell(self, product: Product):
        if self.has_enough_inventory(product):
            self.item = Product(
                self.item.merch,
                self.item.count - product.count,
            )

    def has_enough_inventory(self, product: Product):
        if (self.item.count - product.count) < 0:
            return False

        else:
            return True


class Customer:
    def __init__(self) -> None:
        self.item: Product = None

    def purchase(
            self,
            store: Store,
            product: Product,
    ) -> bool:
        if store.has_enough_inventory(product):
            store.sell(product)
            return True
        else:
            return False


class TestCustomer:
    store = Store(Product("Shampoo", 10))
    sut = Customer()

    def test_purchase_succeeds_when_enough_inventory(self):
        success = self.sut.purchase(self.store, Product("Shampoo", 5))

        assert success is True
        assert 5 == self.store.item.count

    def test_purchase_fails_when_not_enough_money(self):
        success = self.sut.purchase(self.store, Product("Shampoo", 15))

        assert success is False
        assert 10 == self.store.item.count
