shipments = {
    "SHP101": "Delivered",
    "SHP102": "In Transit",
    "SHP103": "Pending"
}
print("Shipment IDs:")
print(shipments.keys())

print("Current statuses:")
print(shipments.values())

print("Shipment ID and status:")
print(shipments.items())