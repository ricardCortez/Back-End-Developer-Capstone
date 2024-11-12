# Back-End-Developer-Capstone
# LittleLemon - Restaurant Management System

## Project Description
This project is a management system for the LittleLemon restaurant, featuring:
- Menu querying
- Create, update, and delete menu items
- Table booking management via a protected API with authentication

## API Routes for Testing

Here are the API routes that your peers can test:

### 1. **/api/booking/** (Table Booking)
   - **GET**: Retrieve all table bookings.
   - **POST**: Create a new table booking.

### 2. **/api/menu/** (Menu Management)
   - **GET**: Retrieve all menu items.
   - **POST**: Create a new menu item.

### 3. **/api/menu/{id}/** (Specific Menu Item)
   - **GET**: Retrieve details of a specific menu item by ID.
   - **PUT**: Update a menu item by ID.
   - **DELETE**: Delete a menu item by ID.

### 4. **/api-token-auth/** (Authentication)
   - **POST**: Get an authentication token using user credentials (username and password).

## Steps to Test the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/littlelemon.git
   cd littlelemon

2. Create and activate a virtual environment (optional):
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Linux/Mac
    .\env\Scripts\activate   # On Windows

3. Set up the database (if needed):
    ```bash
    mysql -u root -p
    CREATE DATABASE LittleLemon;

4. Start the server:
    ```bash
    python manage.py runserver

5. To test the API routes, use tools like Postman or curl to make requests to the listed routes.