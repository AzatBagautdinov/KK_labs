import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("Alice", 100.0)
        self.target = BankAccount("Bob", 50.0)

    def test_deposit_positive(self):
        self.account.deposit(50.0)
        self.assertEqual(self.account.balance, 150.0)

    def test_deposit_negative(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

    def test_withdraw_valid(self):
        self.account.withdraw(40.0)
        self.assertEqual(self.account.balance, 60.0)

    def test_withdraw_insufficient(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200.0)

    def test_transfer(self):
        self.account.transfer(self.target, 50.0)
        self.assertEqual(self.account.balance, 50.0)
        self.assertEqual(self.target.balance, 100.0)

    def test_rename_owner(self):
        self.account.rename_owner("Charlie")
        self.assertEqual(self.account.owner, "Charlie")

    def test_rename_owner_invalid(self):
        with self.assertRaises(ValueError):
            self.account.rename_owner("   ")

    def test_get_summary(self):
        summary = self.account.get_summary()
        self.assertEqual(summary["owner"], "Alice")
        self.assertEqual(summary["balance"], 100.0)
        self.assertIsInstance(summary["transactions"], list)

if __name__ == '__main__':
    unittest.main()
