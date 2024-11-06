
# MongoDB Case Converter

> A mini library that converts MongoDB database fields from `snake_case` to `camelCase`.

## Description

This library helps to convert field names in a MongoDB database from `snake_case` to `camelCase`. It automatically updates the structure of collections, making it easier to interact with APIs that use `camelCase` for field naming.

## Installation

1. Make sure you have Python 3 installed.
2. Clone the repository and navigate to the project directory:

    ```bash
    git clone <your-repo-url>
    cd <project-directory>
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To convert the fields, run the `convert.py` script using Python:

```bash
python convert.py
```

## How It Works

The library performs the following steps:

1. Connects to your MongoDB database.
2. Finds all fields in `snake_case`.
3. Converts them to `camelCase`.
4. Updates the database, preserving data structure and relationships.

## Example

### Before

```json
{
    "first_name": "John",
    "last_name": "Doe",
    "phone_number": "123456789"
}
```

### After

```json
{
    "firstName": "John",
    "lastName": "Doe",
    "phoneNumber": "123456789"
}
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
