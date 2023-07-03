from datetime import (
    datetime,
    timedelta,
)

import pytest


class Delivery:
    date_time: datetime

    def is_delivery_valid(self):
        return self.date_time >= datetime.now() + timedelta(days=1.999)


class TestDelivery:
    @pytest.mark.parametrize("from_now", [(-1), (0), (1), (2)])
    @pytest.mark.parametrize("expected", [(False), (False), (False), (True)])
    def test_can_detect_an_invalid_delivery_date(self, from_now, expected):
        sut: Delivery = Delivery()
        past_date: datetime = datetime.now() + timedelta(days=from_now)
        sut.date_time = past_date

        is_valid = sut.is_delivery_valid()

        assert is_valid == expected
