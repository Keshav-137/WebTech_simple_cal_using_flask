# Practical 6: Calculator Using Django Framework

## Aim

To create a web-based calculator using the Django framework. The application
accepts two numbers and performs addition, subtraction, multiplication, or
division.

## Objectives

- Create a Django project and a calculator application.
- Map the root URL to a Django view.
- Process calculator form submissions using HTTP `POST`.
- Validate user input and display a result or a helpful error message.
- Write automated tests for the calculator.

## Requirements

- Python 3.10 or later
- pip
- A web browser

Django is installed from the project's `requirements.txt` file.

## Project structure

```text
.
├── manage.py
├── requirements.txt
├── calculator_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── calculator/
    ├── apps.py
    ├── urls.py
    ├── views.py
    ├── tests.py
    └── templates/
        └── calculator/
            └── index.html
```

### Important files

- `manage.py` provides the command-line entry point for Django tasks.
- `calculator_project/settings.py` contains project settings and registers the
  calculator app.
- `calculator_project/urls.py` includes the calculator app's URL configuration.
- `calculator/urls.py` maps the root page to the calculator view.
- `calculator/views.py` reads the submitted values, performs the calculation,
  and renders the page with the result or an error.
- `calculator/templates/calculator/index.html` contains the calculator form and
  its styling.
- `calculator/tests.py` contains automated tests for the page and calculations.
- `requirements.txt` lists the Django dependency.

## Setup and installation

Open PowerShell in the project directory and run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
```

If PowerShell does not recognize the `py` command, use the Python executable
installed on your system in its place.

## Start the development server

```powershell
py manage.py runserver
```

Open <http://127.0.0.1:8000/> in a browser. Stop the server with `Ctrl+C`.

## Using the calculator

1. Enter a value in **First number**.
2. Enter a value in **Second number**.
3. Select one of the operation buttons:
   - `+` adds the numbers.
   - `−` subtracts the second number from the first.
   - `×` multiplies the numbers.
   - `÷` divides the first number by the second.
4. The result or an error message appears below the form.

The calculator accepts decimal values and negative numbers. For example, with
`3` and `4`, the results are `7`, `-1`, `12`, and `0.75`, respectively.

## How it works

This application follows Django's Model-Template-View (MTV) pattern:

1. The browser requests `/`, and `calculator_project/urls.py` passes the
   request to `calculator/urls.py`.
2. The URL configuration calls the `calculator` view.
3. On a `GET` request, the view renders an empty calculator form.
4. When an operation button is pressed, the form sends both values and the
   selected operation to the same URL using `POST`.
5. The view checks that both numbers are present and that the operation is
   supported. It converts values to Python `Decimal` objects before calculating,
   which avoids the common binary floating-point rounding issues of `float`.
6. The view passes the calculation result or validation message to the template,
   which displays it to the user.

The form includes Django's CSRF token. Division by zero, missing values,
malformed numbers, and non-finite values such as `NaN` or `Infinity` are not
accepted.

This small calculator does not need to save data, so it does not define a model
or require database migrations.

## Run the tests

With the virtual environment activated, run:

```powershell
py manage.py test
```

The test suite checks:

- The calculator page responds successfully.
- All four arithmetic operations return the expected results.
- Division by zero produces an error message.
- Invalid numeric input produces an error message.

## Result

A Django web application was created that performs four arithmetic operations,
validates user input, and displays calculation results in the browser.
