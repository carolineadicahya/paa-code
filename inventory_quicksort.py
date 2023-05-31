# algoritma quicksort
def swap(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

def quicksort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quicksort_helper(my_list, left, pivot_index - 1)
        quicksort_helper(my_list, pivot_index + 1, right)
    return my_list

def quicksort(my_list):
    return quicksort_helper(my_list, 0, len(my_list) - 1)

class Item:
    def __init__(self, item_id, name, quantity):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f"Item ID: {self.item_id}, Name: {self.name}, Quantity: {self.quantity}"

def sort_items_by_quantity(items):
    quantities = [item.quantity for item in items]
    sorted_quantities = quicksort(quantities)
    sorted_items = []
    for quantity in sorted_quantities:
        for item in items:
            if item.quantity == quantity and item not in sorted_items:
                sorted_items.append(item)
                break
    return sorted_items


# Main Program
if __name__ == "__main__":
    items = [
        Item(1, "Item 1", 5),
        Item(2, "Item 2", 3),
        Item(3, "Item 3", 7),
        Item(4, "Item 4", 2),
        Item(5, "Item 5", 1),
    ]
    sorted_items = sort_items_by_quantity(items)
    for item in sorted_items:
        print(item)
