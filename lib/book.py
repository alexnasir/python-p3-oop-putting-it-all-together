class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count  # This will call the setter

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value  # Store the valid integer value

    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")