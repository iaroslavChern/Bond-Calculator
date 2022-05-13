import Bonds
import Interface
import sys
from PyQt5 import QtWidgets


class ExampleApp(QtWidgets.QMainWindow, Interface.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_calculate.clicked.connect(self.calculation)

    def calculation(self):
        """This function gets values from lineEdits also the function initializes an instance
        of the class, accesses the yield calculation method and sets the value to
        the desired field"""
        ACI = float(self.ACI_lineedit.text())
        purchase_price = float(self.purchase_price_lineedit.text())
        coupon_period = float(self.coupon_period_lineedit.text())
        value_coupon = float(self.value_coupon_lineedit.text())
        date_buy = self.date_buy_dateEdit.text()
        date_sale = self.date_sale_dateEdit.text()
        date_maturity = self.date_maturity_dateEdit.text()
        nominal = float(self.nominal_lineedit.text())
        Bond_1 = Bonds.Bond(ACI, nominal, value_coupon, purchase_price, coupon_period, date_buy, date_sale,
                                date_maturity)
        yield_in_percent_year = Bond_1.yield_to_maturity_calculation()
        self.yield_to_maturity_lineedit.setText(str(yield_in_percent_year) + " %")


def main():
    app = QtWidgets.QApplication(sys.argv)  # New instance of QApplication
    window = ExampleApp()  # initializes an instance of the class ExampleApp
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
