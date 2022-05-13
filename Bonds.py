class Bond(object):
    def __init__(self, ACI, nominal, value_coupon, purchase_price, coupon_period, date_buy, date_sale, date_maturity):
        """ACI - accumulated coupon income in RUB; purchase_price - purchase price in % of nominal;
        coupon_period - coupon period in days; value_coupon - the coupon value in RUB;
        date_buy - the date of buy, the date is written in the format [dd/mm/yyyy];
        date_sale - the date of sale, the date is written in the format [dd/mm/yyyy];
        date_maturity - the date of maturity, the date is written in the format [dd/mm/yyyy];
        nominal - the nominal of bond in RUB"""
        self.ACI = ACI
        self.purchase_price = purchase_price
        self.coupon_period = coupon_period
        self.value_coupon = value_coupon
        self.date_buy = date_buy
        self.date_sale = date_sale
        self.date_maturity = date_maturity
        self.nominal = nominal

    def yield_to_maturity_calculation(self):
        """Calculation of the yield to maturity as a percentage per annum also include a tax.
        number_of_coupons - number of coupons during period of circulation of the bond;
        "+1" when calculating "number_of_coupons" includes the current coupon;
        0.87 takes into account the tax in Russia."""
        from datetime import datetime
        date_maturity = datetime.strptime(self.date_maturity, "%d.%m.%Y").date()  #
        date_buy = datetime.strptime(self.date_buy, "%d.%m.%Y").date()
        period_of_ownership = int((date_maturity - date_buy).days)
        number_of_coupons = int(period_of_ownership / self.coupon_period) + 1
        yield_on_body_of_bond = self.nominal - self.purchase_price / 100 * self.nominal
        coupon_profit = self.value_coupon * number_of_coupons * 0.87
        if yield_on_body_of_bond > 0:
            # This condition takes into account the income on the body of the bond
            profit_on_body_of_bond = 0.87 * yield_on_body_of_bond
        yield_in_percent = (coupon_profit + yield_on_body_of_bond) / (
                self.ACI + self.purchase_price / 100 * self.nominal) * 100
        yield_in_percent_year = yield_in_percent / period_of_ownership * 365
        return round(yield_in_percent_year, 1)


if __name__ == "__main__":
    date_buy = []
    bond_1 = Bond(23.86, 1000, 32.41, 87.94, 91, "25.04.2022", None, "15.05.2025")
    bond_1.yield_to_maturity_calculation()
