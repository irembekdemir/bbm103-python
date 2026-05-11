import sys
from typing import Any
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


# Main Logic Part

CART = {}

SPECIAL_OFFER_ITEMS = {"coffee", "apple", "cereal", "cheese", "pasta"}

COUPON_CODES = {"WELCOME10": 0.10, "SAVE20": 0.20, "MEGA25": 0.25}

USED_COUPONS = set()


def add_item_to_cart(item_name: str, quantity: int, unit_price: float) -> None:
    if not item_name or quantity <= 0 or unit_price <= 0:
        return

    item_name = item_name.lower().strip()

    if item_name in CART:
        CART[item_name]["quantity"] += quantity
    else:
        CART[item_name] = {"quantity": quantity, "unit_price": unit_price}


def remove_item_from_cart(item_name: str, quantity: int) -> None:
    if not item_name or quantity <= 0:
        return

    item_name = item_name.lower().strip()

    if item_name not in CART:
        return

    if quantity >= CART[item_name]["quantity"]:
        del CART[item_name]
    else:
        CART[item_name]["quantity"] -= quantity


def display_cart() -> str:
    if not CART:
        return "Your cart is empty."

    output = []

    for item, data in CART.items():
        mark = " *" if item in SPECIAL_OFFER_ITEMS else "  "
        output.append(
            f"{item}{mark} | Qty: {data['quantity']} | Price: {data['unit_price']:.2f}"
        )

    return "\n".join(output)


def get_cart_summary() -> str:
    total_items = len(CART)
    total_quantity = sum(x["quantity"] for x in CART.values())
    total_price = sum(x["quantity"] * x["unit_price"] for x in CART.values())
    special_count = sum(1 for item in CART if item in SPECIAL_OFFER_ITEMS)

    return (
        f"Total Items: {total_items}\n"
        f"Total Quantity: {total_quantity}\n"
        f"Total Price: {total_price:.2f}\n"
        f"Special Items: {special_count}"
    )


def calculate_total_price(coupon_code: str) -> float:
    total = 0.0

    for item, data in CART.items():
        discount = 0.0

        if data["quantity"] > 3:
            discount += 0.10

        if item in SPECIAL_OFFER_ITEMS:
            discount += 0.05

        total += data["quantity"] * data["unit_price"] * (1 - discount)

    code = coupon_code.upper().strip()

    if code in COUPON_CODES and code not in USED_COUPONS:
        total *= (1 - COUPON_CODES[code])
        USED_COUPONS.add(code)

    return round(total, 2)


# GUI Interface

class ShoppingCartWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Shopping Cart System")
        self.setGeometry(600, 200, 600, 500)
        self.initUI()
        self.apply_styles()

    def apply_styles(self):
        self.setStyleSheet("""
            QWidget { background-color: #f7f9fc; font-size: 14px; }
            QGroupBox { background-color: white; border-radius: 8px; }
            QPushButton { background-color: #3498db; color: white; padding: 8px; }
        """)

    def initUI(self):
        layout = QVBoxLayout()

        self.title = QLabel("Smart Cart")
        self.title.setFont(QFont("Arial", 18))
        layout.addWidget(self.title)

        self.item_input = QLineEdit()
        self.qty_input = QLineEdit()
        self.price_input = QLineEdit()

        layout.addWidget(self.item_input)
        layout.addWidget(self.qty_input)
        layout.addWidget(self.price_input)

        add_btn = QPushButton("Add")
        add_btn.clicked.connect(self.add_item)
        layout.addWidget(add_btn)

        self.setLayout(layout)

    def add_item(self):
        item = self.item_input.text()
        qty = self.qty_input.text()
        price = self.price_input.text()

        if qty.isdigit() and price.replace('.', '', 1).isdigit():
            add_item_to_cart(item, int(qty), float(price))

    def is_int(self, v: Any) -> bool:
        try:
            int(v)
            return True
        except:
            return False

    def is_float(self, v: Any) -> bool:
        try:
            float(v)
            return True
        except:
            return False


def main():
    app = QApplication(sys.argv)
    window = ShoppingCartWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
