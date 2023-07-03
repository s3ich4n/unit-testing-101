from datetime import (
    datetime,
    timedelta,
)

import pytest


class Delivery:
    date_time: datetime

    def is_delivery_valid(self):
        return self.date_time >= datetime.now() + timedelta(days=1.999)


testdata = [
    (-1, False),
    (0, False),
    (1, False),
    (2, True),
]


class TestDelivery:
    @pytest.mark.parametrize(
            "from_now, expected",
            [(-1, False), (0, False), (1, False), (2, True)]
    )
    def test_can_detect_an_invalid_delivery_date(self, from_now, expected):
        sut: Delivery = Delivery()
        past_date: datetime = datetime.now() + timedelta(days=from_now)
        sut.date_time = past_date

        is_valid = sut.is_delivery_valid()

        assert is_valid == expected

    @pytest.mark.parametrize("from_now, expected", testdata)
    def test_can_detect_an_invalid_delivery_date2(self, from_now, expected):
        sut: Delivery = Delivery()
        past_date: datetime = datetime.now() + timedelta(days=from_now)
        sut.date_time = past_date

        is_valid = sut.is_delivery_valid()

        assert is_valid == expected
