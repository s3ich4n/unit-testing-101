class UserRepository:
    last_query: str

    def get_by_id(self, user_id: int):
        ...

    def get_query(self):
        return self.last_query


def test_get_by_id_executes_correct_sql_code():
    sut: UserRepository = UserRepository()

    user = sut.get_by_id(5)

    assert sut.last_query == "SELECT * FROM dbo.User WHERE user_id = 5"
