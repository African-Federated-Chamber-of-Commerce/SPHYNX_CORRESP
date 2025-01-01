# Glossary of Banking Terms

## Document Control
- **Version**: 2.1
- **Last Updated**: 2024-01
- **Status**: Active
- **Review Cycle**: Quarterly
- **Owner**: Banking Operations Department

## Categories
### Transaction Terms
- **MT Messages**: Standardized SWIFT message types
  - MT103: Single Customer Credit Transfer
  - MT202: General Financial Institution Transfer
  - MT950: Statement Message

### Regulatory Terms
- **FATF**: Financial Action Task Force
  - Role: International money laundering watchdog
  - Scope: Sets global standards

### Message Standards and Protocols
- **ISO 15022**: Legacy SWIFT message standard
  - Used for: Securities, Treasury, Trade
  - Status: Being phased out
- **ISO 20022**: New message standard
  - XML-based format
  - Enhanced data structure
  - Universal adoption by 2025

### Technical Banking Operations
- **Cut-off Times**: Designated processing deadlines
  - USD: 16:00 GMT
  - EUR: 15:00 GMT
  - GBP: 14:00 GMT
- **Processing Cycles**:
  - EOD: End of Day
  - BOD: Beginning of Day
  - Intraday: Continuous

## Key Terms and Definitions
- **Nostra**: 'Our account with you' - An account held by a domestic bank in a foreign bank.
- **Vostra**: 'Your account with us' - An account held by a foreign bank in a domestic bank.
- **SWIFT**: Society for Worldwide Interbank Financial Telecommunication - A network for secure financial messaging.
- **AML**: Anti-Money Laundering - Regulations and procedures to prevent money laundering.
- **KYC**: Know Your Customer - Procedures to verify the identity of customers.
- **IBAN**: International Bank Account Number - A standardized international numbering system for individual bank accounts.
- **BIC**: Bank Identifier Code - A unique identifier for banks used in international transactions.
- **BIS**: Bank for International Settlements - The central bank of central banks.
- **RTGS**: Real-Time Gross Settlement - System for large-value interbank transfers.
- **ACH**: Automated Clearing House - Electronic network for financial transactions.

## Explanation of Key Banking Terminologies and Their Usage
- **Liquidity**: The ability of a bank to meet its financial obligations as they come due, ensuring smooth operations and customer confidence.
- **Capital Adequacy**: The requirement for banks to maintain a certain level of capital to absorb potential losses and protect depositors.
- **Risk Management**: The process of identifying, assessing, and controlling threats to an organization's capital and earnings.

## Practical Examples of Term Usage
- **Nostra Account Example**: Bank A in New York maintains a EUR account with Deutsche Bank in Frankfurt.
- **SWIFT Example**: Using MT103 message type to transfer $50,000 from a US bank to a UK beneficiary.
- **KYC Example**: Collecting and verifying passport, proof of address, and source of funds documentation.

## Examples of How These Terms Are Used in Real-World Scenarios
- **Nostra Account**: Used by banks to manage foreign currency transactions and facilitate international trade.
- **SWIFT**: Used for secure international financial messaging and transactions, ensuring fast and reliable communication between banks.
- **AML**: Implemented by banks to detect and report suspicious activities that may indicate money laundering.
- **KYC**: Used by banks to verify the identity of their customers, ensuring compliance with regulatory requirements.

## Industry-Specific Applications
- **Trade Finance**: Letters of credit, bank guarantees, and documentary collections.
- **Treasury Operations**: Foreign exchange dealing, money market operations.
- **Risk Management**: Credit risk assessment, market risk monitoring.

## Additional Banking Terms
- **Basel III**: A global regulatory framework for more resilient banks and banking systems, focusing on risk management and capital adequacy.
- **Credit Risk**: The risk of loss due to a borrower's failure to make payments, impacting the bank's financial stability.
- **Operational Risk**: The risk of loss resulting from inadequate or failed internal processes, people, and systems, affecting the bank's operations and reputation.
- **Compliance Risk**: The risk of legal or regulatory sanctions, financial loss, or reputational damage due to non-compliance with laws, regulations, or internal policies.
- **Market Risk**: The risk of losses in on- and off-balance-sheet positions arising from movements in market prices.

## Emerging Banking Terms
- **Fintech**: Financial technology companies that leverage technology to offer innovative financial services.
- **Regtech**: Regulatory technology solutions designed to help financial institutions comply with regulations efficiently.
- **Cryptocurrency**: Digital or virtual currencies that use cryptography for security and operate independently of a central bank.
- **Blockchain**: A decentralized digital ledger that records transactions across many computers in a way that the registered transactions cannot be altered retroactively.

## Technical Specifications
### Message Formats
- **SWIFT Message Structure**
  - Header: Basic reference data
  - Body: Transaction details
  - Trailer: Authentication codes

### Technical Message Standards
### Field Requirements
| Field Code | Format | Required | Description |
|------------|--------|----------|-------------|
| :20 | 16x | M | Transaction Reference |
| :32A | 6!n3!a15d | M | Value Date/Currency/Amount |
| :50K | 35x | M | Ordering Customer |
| :59 | 35x | M | Beneficiary Customer |

### Message Validation Rules
- **Sequence Validation**: Fields must appear in correct sequence
- **Character Set**: SWIFT-compliant character set only
- **Field Dependencies**: Proper field relationships maintained

### Message Types Overview
| Message Type | Category | Usage |
|-------------|----------|--------|
| MT1xx | Customer Payments | Fund transfers |
| MT2xx | Financial Institution Transfers | Bank-to-bank |
| MT9xx | Cash Management | Statements |

### SWIFT Message Fields
- **Field 20**: Transaction Reference Number
- **Field 32A**: Value Date/Currency/Amount
- **Field 50K**: Ordering Customer
- **Field 59**: Beneficiary Customer

### ISO 20022 Structures
- **pacs.008**: Customer Credit Transfer
- **pacs.009**: Financial Institution Transfer
- **camt.053**: Bank to Customer Statement

### Validation Rules
- **BIC Format**: 8 or 11 characters
- **IBAN Validation**: MOD-97 algorithm
- **Amount Format**: Max 15 digits

### Protocol Standards
- **ISO 20022**
  - XML-based messaging
  - Universal financial industry message scheme

### Message Format Details
| Field | Format | Usage | Validation |
|-------|--------|--------|------------|
| :20 | 16x | Reference | Unique, no spaces |
| :32A | 6!n3!a15d | Amount | Valid date + currency |
| :50K | 35x | Ordering | Name mandatory |
| :59 | 35x | Beneficiary | Account required |

### System Integration Points
- **Core Banking**
  - Transaction posting
  - Account maintenance
  - Balance reporting
- **Payment Gateways**
  - SWIFT Alliance
  - Local clearing
  - Card networks

## Importance of Understanding Banking Terms
A clear understanding of banking terms is essential for effective communication, compliance, and decision-making within the financial industry. It helps professionals navigate complex regulations and procedures, and ensures that they can effectively manage risks and maintain the stability of financial institutions.

## Additional Resources
- **Regulatory Guidelines**: Refer to relevant regulatory guidelines for detailed definitions and usage of banking terms.
- **Industry Publications**: Consult industry publications for the latest trends and updates in banking terminology.
- **Online Courses**: Enroll in online courses to deepen your understanding of banking terms and their applications.

## Summary of Key Points
- **Key Terms**: Nostra, Vostra, SWIFT, AML, KYC, IBAN, BIC.
- **Usage**: Real-world applications of these terms.
- **Additional Terms**: Basel III, credit risk, operational risk, compliance risk, market risk.
- **Emerging Terms**: Fintech, regtech, cryptocurrency, blockchain.
- **Resources**: Regulatory guidelines, industry publications, online courses.
