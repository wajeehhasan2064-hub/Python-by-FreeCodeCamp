class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ""):
        self.ledger.append(
            {
                "amount": amount,
                "description": description
            }
        )

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance

    def check_funds(self, amount):
        balance = self.get_balance()
        if amount > balance:
            return False
        return True

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append(
                {
                    "amount": -amount,
                    "description": description
                }
            )
            return True
        return False

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination.name}")
            destination.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        output = ""
        output += self.name.center(30, "*") + "\n"
        for transaction in self.ledger:
            description = transaction["description"]
            description_text = description[:23].ljust(23)
            amount = transaction["amount"]
            amount_text = f"{amount:>7.2f}"
            output += description_text + amount_text + "\n"
        output += f"Total: {self.get_balance()}"
        return output


def create_spend_chart(categories):
    spend = []
    for category in categories:
        total = 0
        for transaction in category.ledger:
            if transaction["amount"] < 0:
                total += abs(transaction["amount"])
        spend.append(total)

    total_spent = sum(spend)
    percentages = []
    for amount in spend:
        percentage = int((amount / total_spent) * 100)
        percentage = percentage // 10 * 10
        percentages.append(percentage)

    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"       
        for percentage in percentages:
            if percentage >= i:
                chart += " o "
            else:
                chart += "   "       
        chart += " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    names = [category.name for category in categories]
    max_length = max(len(name) for name in names)
    for i in range(max_length):
        chart += "     "
        for name in names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        chart += "\n"
    return chart.rstrip("\n")