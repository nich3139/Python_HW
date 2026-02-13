from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 11", "+79161234567"),
    Smartphone("Samsung", "Galaxy S24 Ultra", "+79262345678"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79373456789"),
    Smartphone("Google", "Pixel 6a", "+79484567890"),
    Smartphone("OnePlus", "OnePlus 8", "+79595678901")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
