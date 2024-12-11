def function_with_closed_file(filename):
    try:
        with open(filename, 'w') as f:
            # ... some code that might raise an exception ...
            f.write('This is some text.')
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File closed properly.") # Optional - just for demonstration