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


def test_purchase_succeeds_when_enough_inventory():
    # Arrange
    store = Store(Product("Shampoo", 10))
    customer = Customer()

    # Act
    is_available = store.has_enough_inventory(Product("Shampoo", 5))
    success = customer.purchase(store, Product("Shampoo", 5))

    # Assert
    assert is_available is True
    assert success is True
    assert 5 == store.item.count


def test_purchase_fails_when_not_enough_money():
    # Arrange
    store = Store(Product("Shampoo", 10))
    customer = Customer()

    # Act
    is_available = store.has_enough_inventory(Product("Shampoo", 15))
    success = customer.purchase(store, Product("Shampoo", 15))

    # Assert
    assert is_available is False
    assert success is False
    assert 10 == store.item.count
