import pytest

from checkout import Checkout

#testing for a single item with varied quantity
@pytest.mark.parametrize("scanned_items, expected_total", [
    ("A", 50),
    ("AA", 100),
    ("AAA", 130),
    ("aAAA", 180),
    ("AAAAA", 200)
])
def test_checkout_single_item(scanned_items, expected_total):
    print(scanned_items, expected_total)
    checkout_obj = Checkout()
    checkout_obj.scan_items(scanned_items)
    checkout_total = checkout_obj.checkout_total
    assert  checkout_total == expected_total


#Testing for the examples given in the assignemnt
@pytest.mark.parametrize("scanned_items, expected_total", [
    ("", 0),
    ("A", 50),
    ("AB", 80),
    ("CDBA", 115),
    ("AA", 100),
    ("AAA", 130),
    ("AAAA", 180),
    ("AAAAA", 200),
    ("AAAAAA", 250),
    ("AAAB", 160),
    ("AAABB", 190),
    ("AAABBD", 205),
    ("DABABA", 205),
])
def test_checkout_assignment_examples(scanned_items, expected_total):
    checkout_obj = Checkout()
    checkout_obj.scan_items(scanned_items)
    checkout_total = checkout_obj.checkout_total
    assert  checkout_total == expected_total


#Testing for independent order sequencing
@pytest.mark.parametrize("sequence1, sequence2, expected_total", [
    ("AAABB", "ABABA", 190)
])
def test_checkout_order_independence(sequence1, sequence2, expected_total):
    co1 = Checkout()
    co2 = Checkout()

    co1.scan_items(sequence1)
    co2.scan_items(sequence2)

    assert co1.checkout_total == co2.checkout_total == 190


#Testing for non-existing items being scanned
@pytest.mark.parametrize("non_existing_items", [
    ("Z"),
    ("ZZ"),
    ("XYZ")
])
def test_checkout_non_existing_items(non_existing_items):
    with pytest.raises(Exception):
        checkout_obj = Checkout()
        checkout_obj.scan_items()