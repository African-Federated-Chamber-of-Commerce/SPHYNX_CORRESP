import os

REQUIRED_STRUCTURE = {
    'Entity_Specific': ['Entity_Banking_Requirements.md'],
    'templates': ['SWIFT_template.md', 'agreement_template.md'],
    'scripts': ['generate_review_report.py']
}

def validate_structure():
    errors = []
    root_dir = os.path.dirname(__file__)

    for directory, files in REQUIRED_STRUCTURE.items():
        dir_path = os.path.join(root_dir, directory)
        
        if not os.path.exists(dir_path):
            errors.append(f"Missing directory: {directory}")
            continue
            
        for file in files:
            file_path = os.path.join(dir_path, file)
            if not os.path.exists(file_path):
                errors.append(f"Missing file: {directory}/{file}")
            elif os.path.getsize(file_path) == 0:
                errors.append(f"Empty file: {directory}/{file}")

    return errors
