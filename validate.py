import os
import json

REQUIRED_DIRS = [
    'General_Guidelines',
    'Entity_Specific',
    'Templates',
    'Reports',
    'Templates/SWIFT',
    'Templates/Agreements'
]

REQUIRED_FILES = [
    'General_Guidelines/Glossary_of_Banking_Terms.md',
    'Entity_Specific/Entity_Banking_Requirements.md',
    'README.md',
    'Templates/SWIFT/MT103_template.txt',
    'Templates/SWIFT/MT202_template.txt',
    'Templates/Agreements/standard_agreement.txt'
]

def validate_swift_template(filepath):
    required_fields = [':20:', ':32A:', ':50K:', ':59:']
    with open(filepath) as f:
        content = f.read()
        return all(field in content for field in required_fields)

def validate_templates():
    template_errors = []
    
    # Check SWIFT templates
    swift_dir = 'Templates/SWIFT'
    if os.path.exists(swift_dir):
        for template in os.listdir(swift_dir):
            if template.endswith('.txt'):
                filepath = os.path.join(swift_dir, template)
                if not validate_swift_template(filepath):
                    template_errors.append(f"Invalid SWIFT format in: {template}")
    
    return template_errors

def validate_structure():
    errors = []
    
    # Check directories
    for dir in REQUIRED_DIRS:
        if not os.path.isdir(dir):
            errors.append(f"Missing directory: {dir}")
    
    # Check files
    for file in REQUIRED_FILES:
        if not os.path.isfile(file):
            errors.append(f"Missing file: {file}")
    
    # Add template validation
    template_errors = validate_templates()
    errors.extend(template_errors)
    
    return errors

if __name__ == "__main__":
    errors = validate_structure()
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        exit(1)
    print("Validation successful!")
