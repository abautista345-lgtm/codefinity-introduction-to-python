#Update an inventory list for a grocery store's vegetable section by removing an item, adding two new items, and sorting the list alphabetically without duplicates.
vegetables = ["tomatoes","potatoes", "onions"]
if "carrots" not in vegetables :
    vegetables.append("carrots")
    print("Carrots are already in the list.")
if "cucumbers" not in vegetables:
    vegetables.append("cucumbers")
    print("Cucumbers are already in the list.")
if "onions" in vegetables:
    vegetables.remove("onions")

vegetables.sort()
print("Updated Vegetable Inventory", vegetables)
