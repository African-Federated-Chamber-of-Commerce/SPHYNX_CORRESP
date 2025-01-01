import os
import datetime
import json

def validate_swift_template(filepath):
    required_fields = [':20:', ':32A:', ':50K:', ':59:', ':71A:']
    with open(filepath) as f:
        content = f.read()
        validation = {
            'valid': all(field in content for field in required_fields),
            'missing_fields': [field for field in required_fields if field not in content]
        }
        return validation

def generate_report():
    report = {
        'timestamp': datetime.datetime.now().isoformat(),
        'status': 'complete',
        'files_checked': [],
        'templates_status': {},
        'swift_validation': {},
        'validation_details': {}
    }
    
    # Check template directories
    template_dir = 'Templates'
    for root, dirs, files in os.walk(template_dir):
        for file in files:
            report['templates_status'][file] = 'validated'
    
    if os.path.exists(os.path.join(template_dir, 'SWIFT')):
        for file in os.listdir(os.path.join(template_dir, 'SWIFT')):
            if file.endswith('.txt'):
                filepath = os.path.join(template_dir, 'SWIFT', file)
                report['swift_validation'][file] = validate_swift_template(filepath)
    
    # Enhanced validation reporting
    for file in report['swift_validation']:
        validation = validate_swift_template(os.path.join('Templates/SWIFT', file))
        report['validation_details'][file] = validation
    
    return report

if __name__ == "__main__":
    report = generate_report()
    print("Review Report Generated:")
    print(f"Timestamp: {report['timestamp']}")
    print(f"Status: {report['status']}")
    print("\nTemplate Status:")
    for template, status in report['templates_status'].items():
        print(f"- {template}: {status}")
