# Initial items on shelf #1 (provided as a tuple)
#shelf1 = ("celery", "spinach", "cucumbers")

# Items being added to the shelf #1 (provided as a list)
#shelf1_update = ["tomatoes", "celery", "cilantro"]

# Define lists with items that have been put on sale, recording each sale occurrence for different months
janSales_list = ["apples", "oranges", "apples"]
febSales_list = ["bananas", "oranges", "bananas"]
marSales_list = ["apples", "bananas", "apples"]

# Convert the lists to tuples to ensure immutability (unchangeable) 
janSales = tuple(janSales_list)
febSales = tuple(febSales_list)
marSales = tuple(marSales_list)

# Concatenate all monthly sales into a single tuple for the quarter
quarterlySales = janSales + febSales + marSales
print("Consolidated quarterly sales:", quarterlySales)

# Use the `count()` method to determine how many times "apples" have been on sale during the quarter
apples_sale_count = quarterlySales.count("apples")
print("Apples have been on sale:", apples_sale_count, "times.")

# Use the `index()` method to find the first occurrence of "apples" in the quarterly sales
first_apple_sale_index = quarterlySales.index("apples")
print("The first sale of apples this quarter was at index:", first_apple_sale_index)