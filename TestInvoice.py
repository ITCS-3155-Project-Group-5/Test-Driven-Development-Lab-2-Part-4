import pytest
from Invoice import Invoice

@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}

    return products


def test_CanCalculateTotalImpurePrice(products):
    invoice = Invoice()
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalculateTotalDiscount(products):
    invoice = Invoice()
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def testCanCalculateTotalPurePrice(products):
    invoice = Invoice()
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

# new test case
def test_CanAddProduct():
    product = {'qnt': 5, 'unit_price': 7.5, 'discount': 10}
    invoice = Invoice()
    assert invoice.addProduct(5, 7.5, 10) == product

# new test case
def testCanRemoveProduct(products):
    invoice = Invoice()
    invoice.addProduct(5, 7.5, 10)
    assert invoice.items['qnt'] == 5 and invoice.items['unit_price'] == 7.5
    invoice.changeQuanityAndPrice(2,8)
    print(invoice.items['qnt'])
    assert invoice.items['qnt'] == 2 and invoice.items['unit_price'] == 8
