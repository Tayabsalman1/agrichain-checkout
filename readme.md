# Supermarket Checkout Pricing System

## Overview
This project is a submission to an initial interview round with Agrichain (https://agrichain.com/).  
The project implements a **checkout pricing system** that calculates the total price of scanned items.  
Items are represented by single-letter(SKUs) and priced individually, additionally through configurable discount offers.

The solution focuses on **clean design, extensibility, and correctness**, intentionally excluding UI and API layers.

---

## Key Features
- Order-independent scanning
- Configurable, data-driven pricing rules
- Support for multiple offers per SKU
- Clean separation of concerns (OOP)

---

## Design Approach
The solution follows an **MVC-inspired structure**:

- **Model**: `PricingRule`, `Offer`
- **Controller**: `Checkout`
- **View**: Total value of `Checkout.checkout_total`

Pricing and discount logic are encapsulated within pricing rules, keeping checkout logic simple and extensible.

---

## Core Concepts
- **Order Independence**: Pricing depends on item counts, not scan order.
- **Configurable Rules**: Prices and offers are defined in JSON.
- **Greedy Discounts**: Larger-quantity offers are applied first.
- **Separation of Concerns**: Each class has a single responsibility.

---

## Project Structure
```
agrichain-checkout/
├── checkout.py
├── pricing_rule.py
├── offer.py
├── config_loader.py
├── pricing_config.json
├── main.py
└── tests/
```

---

## Execution (Note to evaluator)
You can run the logic with below command, and interact with the pricing system
```
python main.py
```
---

## Testing
All examples from the assignemnt are covered using unit tests.

```bash
pytest -v --html=tests/test_report.html
```

## Assumptions
- Input contains valid SKUs
- Offers apply per SKU only
- Greedy discounting is sufficient for current rules

## Extensibility

The design supports future additions such as new discount types, admin-managed pricing, or API/UI layers without changing the core logic.
