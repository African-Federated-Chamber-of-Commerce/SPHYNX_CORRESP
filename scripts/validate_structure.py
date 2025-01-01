import os
import sys

def validate_template_content(filepath, required_sections):
    if not os.path.exists(filepath):
        return False
    
    with open(filepath, 'r') as f:
        content = f.read()
        return all(section in content for section in required_sections)

def validate_structure():
    root_dir = os.path.dirname(os.path.dirname(__file__))
    errors = []
    
    # Required directories
    required_dirs = [
        'Entity_Specific',
        'templates',
        'documents',
        'scripts'
    ]
    
    # Required files
    required_files = [
        ('Entity_Specific/Entity_Banking_Requirements.md', 'Banking requirements'),
        ('templates/SWIFT_template.md', 'SWIFT template'),
        ('templates/agreement_template.md', 'Agreement template')
    ]
    
    # Check directories
    for dir_name in required_dirs:
        dir_path = os.path.join(root_dir, dir_name)
        if not os.path.isdir(dir_path):
            errors.append(f"Missing required directory: {dir_name}")
    
    # Check files
    for file_path, desc in required_files:
        full_path = os.path.join(root_dir, file_path)
        if not os.path.isfile(full_path):
            errors.append(f"Missing required {desc}: {file_path}")
    
    # Validate SWIFT template content
    swift_template = os.path.join(root_dir, 'templates/SWIFT_template.md')
    swift_sections = ['Message Header', 'Message Body', 'Message Trailer']
    if not validate_template_content(swift_template, swift_sections):
        errors.append("SWIFT template missing required sections")
    
    # Validate agreement template content
    agreement_template = os.path.join(root_dir, 'templates/agreement_template.md')
    agreement_sections = ['Agreement Details', 'Terms and Conditions']
    if not validate_template_content(agreement_template, agreement_sections):
        errors.append("Agreement template missing required sections")
    
    return errors

if __name__ == "__main__":
    errors = validate_structure()
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)
    print("Structure validation passed")
