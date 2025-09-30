shares = 1000
purchase_price = 32.87
sale_price = 33.92
commission_rate = 0.02


purchase_total = shares * purchase_price
purchase_commission = purchase_total * 0.02
sale_total = shares * sale_price
sale_commission = sale_total * commission_rate
profit_or_loss = (sale_total - sale_commission) - (purchase_total + purchase_commission)
print(f"Amount paid for the stock: ${purchase_total:}")
print(f"Commission paid on purchase: ${purchase_commission:}")
print(f"Amount stock sold for: ${sale_total:}")
print(f"Commission paid on sale: ${sale_commission:}")
print(f"Profit or Loss: ${profit_or_loss:}")

if profit_or_loss > 0:
    print("Joe made a profit.")
else:
    print("Joe lost money.")    

