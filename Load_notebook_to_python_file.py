import json

def extract_code_from_notebook(ipynb_file, py_file, keyword=None):
    # Load the notebook
    with open(ipynb_file, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Check the structure of the notebook
    print("Notebook keys:", notebook.keys())
    
    # Collect code from cells
    code_cells = []
    for cell in notebook.get('cells', []):
        print("Processing cell:", cell.get('cell_type'))  # Debugging cell types
        if cell.get('cell_type') == 'code':
            source = ''.join(cell.get('source', []))
            print("Source code found:", source)  # Debugging code content
            if keyword is None or keyword in source:
                code_cells.append(source)
    
    # Check if any code was extracted
    if not code_cells:
        print("No code cells found or matched the keyword!")
    
    # Write the code to a Python file
    with open(py_file, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(code_cells))
    
    print(f"Code extracted to {py_file}")

# Example usage
extract_code_from_notebook('Load_data.ipynb', 'Loaded_data.py', keyword=None)