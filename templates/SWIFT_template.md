# SWIFT Message Template

## Header Information
- Message Type: {MESSAGE_TYPE}
- Sender: {SENDER_BIC}
- Receiver: {RECEIVER_BIC}
- Reference: {MESSAGE_REFERENCE}

## Message Body
{MESSAGE_CONTENT}

## Authentication
- Signature: {DIGITAL_SIGNATURE}
- Timestamp: {TIMESTAMP}

## Validation Rules
- Transaction Reference: Must be unique, max 16 characters
- Date Format: YYMMDD
- Amount Format: Max 15 digits, 2 decimal places
- BIC Codes: Valid SWIFT directory codes only
