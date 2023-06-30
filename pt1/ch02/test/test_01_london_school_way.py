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


def test_purchase_succeeds_when_enough_inventory(mocker):
    # Arrange
    mock_store = mocker.MagicMock(spec=Store)
    mock_product = mocker.MagicMock(spec=Product("Shampoo", 5))
    mock_store.has_enough_inventory.return_value = True
    customer = Customer()

    # Act
    success = customer.purchase(mock_store, mock_product)

    # Assert
    assert success is True
    mock_store.sell.assert_called_once_with(mock_product)


def test_purchase_fails_when_not_enough_money(mocker):
    # Arrange
    mock_store = mocker.MagicMock(spec=Store)
    mock_product = mocker.MagicMock(spec=Product("Shampoo", 15))
    mock_store.has_enough_inventory.return_value = False
    customer = Customer()

    # Act
    success = customer.purchase(mock_store, mock_product)

    # Assert
    assert success is False
    mock_store.sell.assert_not_called()
