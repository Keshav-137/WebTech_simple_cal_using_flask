from django.test import TestCase
from django.urls import reverse


class CalculatorTests(TestCase):
    def test_home_page_is_available(self):
        response = self.client.get(reverse("calculator:home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Calculator")

    def test_supported_operations(self):
        cases = [
            ("add", "7"),
            ("subtract", "-1"),
            ("multiply", "12"),
            ("divide", "0.75"),
        ]

        for operation, expected in cases:
            with self.subTest(operation=operation):
                response = self.client.post(
                    reverse("calculator:home"),
                    {
                        "first_number": "3",
                        "second_number": "4",
                        "operation": operation,
                    },
                )

                self.assertContains(response, f"Result: {expected}")

    def test_division_by_zero_shows_an_error(self):
        response = self.client.post(
            reverse("calculator:home"),
            {
                "first_number": "3",
                "second_number": "0",
                "operation": "divide",
            },
        )

        self.assertContains(response, "You cannot divide by zero.")

    def test_invalid_number_shows_an_error(self):
        response = self.client.post(
            reverse("calculator:home"),
            {
                "first_number": "not-a-number",
                "second_number": "4",
                "operation": "add",
            },
        )

        self.assertContains(response, "Enter valid finite numbers.")
