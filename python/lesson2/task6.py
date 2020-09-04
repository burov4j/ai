products = []
productId = 1

while True:
    shouldContinue = input("Do you want to continue (y/n)? ")
    if shouldContinue == "n":
        break
    name = input("Enter a product name: ")
    price = input("Enter a product price: ")
    count = input("Enter count of products: ")
    measurement = input("Enter unit of measurement: ")
    products.append((productId, {
        "name": name,
        "price": price,
        "count": count,
        "measurement": measurement
    }))
    print(f"Your products: {products}")
    productId = productId + 1

report = {
    "name": set(),
    "price": set(),
    "count": set(),
    "measurement": set()
}
for product in products:
    report["name"].add(product[1]["name"])
    report["price"].add(product[1]["price"])
    report["count"].add(product[1]["count"])
    report["measurement"].add(product[1]["measurement"])

print(f"Report: {report}")
