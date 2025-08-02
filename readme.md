This project is a backend API for an online grocery store built using Django and Django REST Framework. It provides all essential functionalities for user authentication, product management by store managers, and shopping by customers.

The backend enables:

1. User registration and JWT-based authentication with role-based permissions (customer vs store manager).

2. Store managers to add, edit, and delete grocery products.

3. Customers to browse and filter products, add items to a cart, save items in a wishlist, and checkout to create orders.

4. Managers to view sales reports showing product purchase statistics filtered by category and popularity.

5. The API is designed to be consumed by any frontend — web or mobile — making it a flexible and scalable grocery store backend.



API Overview

1. Authentication: Register and login to receive JWT tokens.

2. Products: Browse, filter, and manage products (managers only).

3. Cart: Add/remove items in the shopping cart.

4. Wishlist: Save and view items saved for later.

5. Checkout: Complete purchases and create orders.

6. Sales Report: Manager-only endpoint for product sales analytics.

All endpoints require authentication except registration and login.