from unittest import TestCase


class TestFormatMainData(TestCase):
    expected_column_names = ["user_id", "rating", "date"]

    def __create_test_dataframe(self):
        return list(
            {
                "user_id": ["1:", "212101", "312101", "2:", "401211", "501211"],
                "rating": [1, 2, 3, 1, 5, 5],
                "date": [1, 2, 3, 1, 5, 5],
            }
        )

    def test_column_names(self):
        rating_test_data = self.__create_test_dataframe()
        self.assertListEqual(
            ["user_id", "rating", "date"], self.expected_column_names
        )
