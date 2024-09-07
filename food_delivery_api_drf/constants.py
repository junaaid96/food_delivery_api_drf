USER_ROLES = (
    ('owner', 'owner'),
    ('employee', 'employee'),
    ('customer', 'customer'),
)

RESTAURANT_TYPES = (
    ('american', 'American'),
    ('mexican', 'Mexican'),
    ('chinese', 'Chinese'),
    ('japanese', 'Japanese'),
    ('italian', 'Italian'),
    ('other', 'Other'),
)

MENU_CATEGORIES = (
    ('appetizer', 'Appetizer'),
    ('main_course', 'Main Course'),
    ('dessert', 'Dessert'),
    ('drink', 'Drink'),
)

PAYMENT_METHODS = (
    ('cash', 'Cash'),
    ('card', 'Card'),
    ('mobile_banking', 'Mobile Banking'),
)

ORDER_STATUS = (
    ('pending', 'Pending'),
    ('processing', 'Processing'),
    ('out_for_delivery', 'Out for Delivery'),
    ('delivered', 'Delivered'),
    ('canceled', 'Canceled'),
)
