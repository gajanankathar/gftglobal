## Table of Contents

  * [Getting Started](#getting-started)


## Getting Started

### 1. Github

- Clone this repository

  ```
  git clone https://github.com/gajanankathar/gftglobal.git
  ```
  
   
### 2. Virtual environment

- Create a virtual environment using python3.6 or above
  ```
  python -m venv venv
  ```
- Activate it
- Windows
  ```
  .\venv\Scripts\activate.bat
  ```
- Linux
  ```
  source venv/bin/activate
  ```
- Use this virtual environment for subsequent tasks
   
### 3. `pip`

- Find the requirements file
- Install all the requirements from requirements.txt
  ```
  pip install -r requirements.txt
  ```

### 4. Run Django Server.

  ```
  python manage.py runserver
  ```

### 5. Access home page through browser 

- Home page
  ```
  http://localhost:8000/
  ```

- Create customer page
  ```
  http://localhost:8000/register/
  ```
  
- Login - User is created when customer got created in system. Username will be your customer first name in lowercase and default password is "password".
  ```
  http://localhost:8000/login/
  ```
  
- Update customer page
  ```
  http://localhost:8000/update/1/
  ```

