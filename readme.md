This project is a backend API for an online grocery store built using Django and Django REST Framework. It provides all essential functionalities for user authentication, product management by store managers, and shopping by customers.

The backend enables:

1. User registration and JWT-based authentication with role-based permissions (customer vs store manager).

2. Store managers to add, edit, and delete grocery products.

3. Customers to browse and filter products, add items to a cart, save items in a wishlist, and checkout to create orders.

4. Managers to view sales reports showing product purchase statistics filtered by category and popularity.

5. The API is designed to be consumed by any frontend — web or mobile — making it a flexible and scalable grocery store backend.



API Overview

1. Authentication: Register and login to receive JWT tokens.

/api/accounts/register/       -	  POST
/api/accounts/login/          -	  POST
/api/accounts/token/refresh/  -	  POST


2. Products: Browse, filter, and manage products (managers only).

/api/products/  -	GET	
/api/products/  -	POST	
/api/products/<product_id>/  -	GET	
/api/products/<product_id>/  -	PUT	
/api/products/<product_id>/  -	DELETE	

3. Cart: Add/remove items in the shopping cart.

/api/orders/cart/   -	GET	
/api/orders/cart/   -	POST	
/api/orders/cart/<cart_item_id>/    -	DELETE	

4. Wishlist: Save and view items saved for later.

/api/orders/wishlist/   -	GET	
/api/orders/wishlist/   -	POST

5. Checkout: Complete purchases and create orders.

/api/orders/checkout/   -	POST

6. Sales Report: Manager-only endpoint for product sales analytics.

/api/products/sales_report/  -	GET	
/api/products/sales_report/?category=X&ordering=-sold_count  -	GET

All endpoints require authentication except registration and login.