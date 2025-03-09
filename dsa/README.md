# Algorithms & Data Structures (DSA)

This project is designed to implement and test multiple algorithms. Each function is accompanied by a set of test cases stored in text files and executed using `pytest`.

## Project Structure

```
.
├── palindrome.py           # Palindrome checker function
├── other_algorithm.py      # Additional algorithm files
│── tests/                  # Directory for all test cases
│   ├── __init__.py         # Makes 'tests' a package (optional)
│   ├── test_palindrome.py  # Test file for palindrome function
│   ├── test_other.py       # Test file for another function
│   ├── other_cases.txt     # Test cases for another function
│── requirements.txt        # (Optional) Dependencies
│── README.md               # Project documentation
```

## Installation

1. Clone the repository:
    
    ```sh
    git clone https://github.com/tonybnya/coding-challenges.git
    cd coding-challenges/dsa
    ```
    
2. (Optional) Create a virtual environment and activate it:
    
    ```sh
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate     # On Windows
    ```
    
3. Install dependencies:
    
    ```sh
    pip install -r requirements.txt
    ```
    

## Usage

### Running Tests

Each function has a corresponding test file in `tests/`. Test cases are stored in text files, formatted as:

```
racecar,True
Racecar,True
A man, a plan, a canal: Panama,True
Hello,False
Python,False
```

To run all tests using `pytest`:

```sh
pytest tests/
```

## Adding New Functions

1. Implement the function inside the root directory.
2. Create a test file in `tests/` with the format `test_<function_name>.py`.
3. Store test cases in a corresponding `.txt` file inside `tests/`.
4. Modify the test file to read test cases from the text file and use `@pytest.mark.parametrize`.
5. Run `pytest` to validate the implementation.

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Commit your changes: `git commit -m "Add new algorithm"`.
4. Push to the branch: `git push origin feature-branch`.
5. Create a pull request.

## License

This project is licensed under the MIT License.