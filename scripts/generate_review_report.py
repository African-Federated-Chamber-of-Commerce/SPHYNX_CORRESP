import os
import datetime
from validate_structure import validate_structure

def check_document_sections(filepath):
    if not os.path.exists(filepath):
        return 0, []
    with open(filepath, 'r') as f:
        content = f.read()
        sections = [line for line in content.split('\n') if line.startswith('##')]
        return len(sections), sections

def generate_report():
    root_dir = os.path.dirname(os.path.dirname(__file__))
    report = []
    
    report.append("# Project Review Report")
    report.append(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Structure validation
    structure_errors = validate_structure()
    report.append("## Structure Validation")
    if structure_errors:
        report.append("Status: Failed")
        for error in structure_errors:
            report.append(f"- {error}")
    else:
        report.append("Status: Passed\n")
    
    # Requirements analysis
    req_file = os.path.join(root_dir, 'Entity_Specific/Entity_Banking_Requirements.md')
    section_count, sections = check_document_sections(req_file)
    report.append("\n## Requirements Document Analysis")
    if section_count > 0:
        report.append(f"Status: Complete ({section_count} sections)")
        report.append("\nSections found:")
        for section in sections:
            report.append(f"- {section.strip('#').strip()}")
    else:
        report.append("Status: Incomplete or missing")
    
    # Template analysis
    report.append("\n## Template Validation")
    templates = {
        'SWIFT Template': 'templates/SWIFT_template.md',
        'Agreement Template': 'templates/agreement_template.md'
    }
    
    for template_name, template_path in templates.items():
        full_path = os.path.join(root_dir, template_path)
        section_count, sections = check_document_sections(full_path)
        
        report.append(f"\n### {template_name}")
        if section_count > 0:
            report.append(f"Status: Complete ({section_count} sections)")
            report.append("\nSections found:")
            for section in sections:
                report.append(f"- {section.strip('#').strip()}")
        else:
            report.append("Status: Incomplete or missing")
    
    # Generate summary
    report_path = os.path.join(root_dir, 'review_report.md')
    with open(report_path, 'w') as f:
        f.write('\n'.join(report))
    
    return report_path

if __name__ == "__main__":
    report_file = generate_report()
    print(f"Report generated: {report_file}")
