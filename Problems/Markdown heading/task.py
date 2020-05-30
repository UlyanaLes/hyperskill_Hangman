def heading(title, level=1):
    if level > 6:
        level = 6
    elif level < 1:
        level = 1
    return '#' * level + ' ' + title


# print(heading("A"))  # Returns "# A"
# print(heading("A", 3))  # Returns "### A"
# print(heading("A", 1))  # Returns "# A"
# print(heading("A", 0))  # Returns "# A"
# print(heading("A", 10))  # Returns "###### A"
