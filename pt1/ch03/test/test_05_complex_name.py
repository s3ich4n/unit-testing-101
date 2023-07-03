from datetime import (
    datetime,
    timedelta,
)


class Delivery:
    date_time: datetime

    def is_delivery_valid(self):
        return self.date_time >= self.date_time + timedelta(days=1.99)


class TestDelivery:
    def test_isdeliveryvalid_invaliddate_returnsfalse(self):
        sut: Delivery = Delivery()
        past_date: datetime = datetime.now() - timedelta(days=1)
        sut.date_time = past_date

        is_valid = sut.is_delivery_valid()

        assert is_valid is False
