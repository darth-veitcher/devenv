# Output Format Instructions for Synthetic Data Specialist

This document defines the **required output format** for all synthetic test data scenarios. Following this format ensures automatic integration with the Entity Forge test suite.

## Directory Structure

All test scenarios MUST be created in this structure:

```
tests/data/
└── {domain}/                          # Domain folder (e.g., business, legal, construction)
    └── {scenario_name}/               # Scenario folder (kebab-case)
        ├── doc_001_{type}.{ext}       # Document 1 (sequential numbering)
        ├── doc_002_{type}.{ext}       # Document 2
        ├── ...
        ├── ground_truth.json          # REQUIRED: Entities + annotations
        └── scenario_metadata.json     # REQUIRED: Scenario description
```

### Domain Guidelines

**Domain** defines the business/industry vertical:

- `business` - General business, commerce, companies
- `legal` - Legal documents, contracts, lawsuits
- `construction` - Construction contracts, permits, projects
- `medical` - Healthcare, medical records, patients
- `government` - Government agencies, public sector
- `finance` - Financial services, banking, investments

**Scenario Name** (kebab-case):

- ✅ `ambiguous_company_names`
- ✅ `multifield_context`
- ✅ `construction_permit_entities`
- ❌ `Ambiguous Company Names` (no spaces/capitals)
- ❌ `ambiguous-company-names-v2` (no version suffixes - use git)

## File 1: Documents (REQUIRED)

### Naming Convention

**Pattern**: `doc_{NNN}_{type}.{ext}`

- **NNN**: Zero-padded 3-digit sequential number (001, 002, 003, ...)
- **type**: Document type (see table below)
- **ext**: File extension (.md for Markdown, .txt for plain text)

**Valid Document Types**:

| Type       | Description               | Extension       | Example               |
| ---------- | ------------------------- | --------------- | --------------------- |
| `email`    | Email correspondence      | `.txt`          | `doc_001_email.txt`   |
| `news`     | News articles             | `.md`           | `doc_002_news.md`     |
| `report`   | Business/industry reports | `.md`           | `doc_003_report.md`   |
| `contract` | Legal contracts           | `.md` or `.txt` | `doc_004_contract.md` |
| `web`      | Web page content          | `.md`           | `doc_005_web.md`      |
| `social`   | Social media posts        | `.txt`          | `doc_006_social.txt`  |
| `memo`     | Internal memos            | `.txt`          | `doc_007_memo.txt`    |
| `press`    | Press releases            | `.md`           | `doc_008_press.md`    |
| `invoice`  | Invoices/financial docs   | `.txt`          | `doc_009_invoice.txt` |

### Document Quality Standards

✅ **Required**:

- Natural language (not obviously synthetic)
- Realistic formatting and structure
- 2-5 entity mentions per document (minimum)
- Appropriate length:
  - Emails/memos: 100-300 words
  - News articles: 300-500 words
  - Reports: 500-1000 words
  - Contracts: 400-800 words

✅ **Best Practices**:

- Mix of canonical names, aliases, and contextual references
- Include disambiguation context (location, industry, products, people)
- Some mentions should be ambiguous (test negative cases)
- Vary mention difficulty across documents

❌ **Avoid**:

- JSON or structured data as document content
- Placeholder text like "[Company Name]" or "Lorem ipsum"
- Obvious patterns like "Entity1, Entity2, Entity3"
- Documents with only 1 entity mention

### Example Document: `doc_001_news.md`

```markdown
# Springfield Pharmacy Expands Chronic Disease Management Program

**Springfield, Illinois** — October 1, 2025

Springfield Pharmacy in Illinois announced today a major expansion of its chronic disease management services, adding dedicated programs for diabetes, hypertension, and cardiovascular health monitoring...

[Natural, realistic content continues]
```

## File 2: ground_truth.json (REQUIRED)

This is the **most critical file**. It contains three required arrays: `entities`, `documents`, and `entity_mentions`.

### Schema

```json
{
  "entities": [
    /* Array of entity definitions */
  ],
  "documents": [
    /* Array of document metadata */
  ],
  "entity_mentions": [
    /* Array of mention annotations */
  ]
}
```

### Section 1: Entities Array

Each entity MUST have:

```json
{
  "entity_id": "11111111-1111-4a1a-8a1a-111111111111",
  "canonical_name": "Springfield Pharmacy (Illinois)",
  "kind": "company",
  "aliases": [
    "Springfield Pharmacy",
    "Springfield Rx",
    "Springfield Pharmacies"
  ],
  "attributes": {
    "location": "Springfield, IL",
    "state": "Illinois",
    "industry": "Healthcare - Retail Pharmacy",
    "services": [
      "prescription filling",
      "vaccinations",
      "chronic disease management"
    ],
    "founded": "1995",
    "ceo": "Michael Thompson"
  }
}
```

**Required Fields**:

- `entity_id` (string): UUID v4 format (use deterministic UUIDs for consistency)
- `canonical_name` (string): Official/full entity name
- `kind` (string): Entity type - `"company"`, `"person"`, `"organization"`, `"product"`, `"location"`
- `aliases` (array[string]): Alternative names/variations (can be empty `[]`)
- `attributes` (object): Key-value pairs (can be empty `{}`)

**Common Attribute Keys** (domain-specific):

- Business: `location`, `industry`, `products`, `services`, `ceo`, `founded`, `employees`
- People: `role`, `organization`, `location`, `specialization`
- Locations: `city`, `state`, `country`, `type`

**UUID Generation**:
Use deterministic UUIDs based on entity name for consistency:

```python
import uuid
entity_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, canonical_name))
```

### Section 2: Documents Array

Each document MUST have:

```json
{
  "document_id": "doc_001",
  "original_filename": "news_pharmacy_expansion.md",
  "document_type": "news",
  "word_count": 342
}
```

**Required Fields**:

- `document_id` (string): Must match filename prefix (e.g., "doc_001" for "doc_001_news.md")
- `original_filename` (string): Optional - original filename before renumbering
- `document_type` (string): One of the valid document types
- `word_count` (integer): Approximate word count

### Section 3: Entity Mentions Array

This is the **ground truth annotations**. Each mention MUST have:

```json
{
  "mention_id": "mention_001_001",
  "document_id": "doc_001",
  "mention_text": "Springfield Pharmacy in Illinois",
  "mention_span": [78, 110],
  "expected_entity_id": "11111111-1111-4a1a-8a1a-111111111111",
  "expected_canonical_name": "Springfield Pharmacy (Illinois)",
  "kind": "company",
  "context_signals": [
    "location:Illinois",
    "location:Springfield, IL",
    "service:chronic disease management"
  ],
  "difficulty": "easy",
  "why_easy_or_hard": "Location explicitly stated as 'in Illinois' with city in dateline"
}
```

**Required Fields**:

- `mention_id` (string): Unique ID - format: `"mention_{doc_num}_{mention_num}"` (e.g., "mention_001_001", "mention_001_002")
- `document_id` (string): Must reference a document in `documents` array
- `mention_text` (string): Exact text of the entity mention in the document
- `mention_span` (array[int, int]): `[start, end]` character offsets in document (0-indexed, end-exclusive)
- `expected_entity_id` (string | null): UUID of expected entity, or `null` if ambiguous
- `expected_canonical_name` (string | null): Name of expected entity, or `null` if ambiguous
- `kind` (string): Entity type
- `context_signals` (array[string]): List of context clues (see format below)
- `difficulty` (string): `"easy"`, `"medium"`, `"hard"`, or `"n/a"` (for non-target entities)
- `why_easy_or_hard` (string): Explanation of difficulty rating

**Context Signals Format**:

```json
["signal_type:value", "signal_type:value", ...]
```

Common signal types:

- `location:Springfield, IL` - Geographic context
- `product:iPhone` - Product/service mention
- `industry:Technology` - Industry context
- `service:prescription filling` - Service offering
- `role:CEO` - Person's role
- `year_founded:1995` - Temporal context

**Difficulty Guidelines**:

| Difficulty | Definition                                  | Example                                                                   |
| ---------- | ------------------------------------------- | ------------------------------------------------------------------------- |
| `easy`     | Single strong signal explicitly in text     | "Springfield Pharmacy in Illinois"                                        |
| `medium`   | Multiple weak signals or inference required | "Springfield chronic disease management" (implies IL, no location stated) |
| `hard`     | Genuinely ambiguous or conflicting signals  | "Springfield Pharmacy" (no context, 3 possible matches)                   |
| `n/a`      | Not a target entity (context only)          | "Illinois Department of Public Health"                                    |

**Ambiguous Mentions** (`expected_entity_id: null`):

- Use `null` when the mention CANNOT be resolved with available context
- Example: "Apple" without context could be Apple Inc., Apple Orchard, or Apple Corps
- These test the system's ability to recognize ambiguity (should return low confidence or null)

**Span Calculation**:

```python
# Find mention in document
start = document.find(mention_text)
end = start + len(mention_text)
mention_span = [start, end]

# Verify (CRITICAL):
assert document[start:end] == mention_text
```

**CRITICAL**: Spans MUST be accurate. Test suite validates that `document[start:end] == mention_text`.

## File 3: scenario_metadata.json (REQUIRED)

Describes the scenario for reporting and documentation.

```json
{
  "scenario_name": "Ambiguous Company Names",
  "scenario_id": "ambiguous_company_names",
  "domain": "business",
  "focus": "Disambiguating companies with identical names using context",
  "description": "Tests entity resolution when multiple real-world entities share names...",
  "created_date": "2025-10-07",
  "entities_count": 9,
  "documents_count": 9,
  "mentions_count": 50,
  "difficulty_distribution": {
    "easy": 20,
    "medium": 20,
    "hard": 10
  },
  "success_criteria": {
    "overall_accuracy": 0.8,
    "easy_accuracy": 0.9,
    "medium_accuracy": 0.75,
    "hard_accuracy": 0.4
  },
  "context_signals": ["location", "industry", "products", "services"]
}
```

**Required Fields**:

- `scenario_name` (string): Human-readable name
- `scenario_id` (string): Kebab-case identifier (must match folder name)
- `domain` (string): Domain classification
- `focus` (string): One-sentence description of what's being tested
- `description` (string): Detailed description (2-3 sentences)
- `created_date` (string): ISO 8601 date (YYYY-MM-DD)
- `entities_count` (integer): Total number of entities
- `documents_count` (integer): Total number of documents
- `mentions_count` (integer): Total entity mentions (excluding `n/a` difficulty)
- `difficulty_distribution` (object): Count by difficulty
- `success_criteria` (object): Accuracy targets (0.0-1.0 range)
- `context_signals` (array[string]): Types of context signals used

**Success Criteria Guidelines**:

- `overall_accuracy`: Target overall accuracy (typically 0.70-0.90)
- `easy_accuracy`: Easy case target (typically 0.85-0.95)
- `medium_accuracy`: Medium case target (typically 0.70-0.85)
- `hard_accuracy`: Hard case target (typically 0.30-0.50)

## Validation Checklist

Before delivering a scenario, validate:

✅ **Structure**:

- [ ] Directory follows `tests/data/{domain}/{scenario_name}/` pattern
- [ ] All documents follow `doc_NNN_{type}.{ext}` naming
- [ ] `ground_truth.json` exists with all 3 arrays
- [ ] `scenario_metadata.json` exists

✅ **ground_truth.json**:

- [ ] All `entity_id` fields are valid UUIDs
- [ ] All `entity_id` references in mentions exist in entities array
- [ ] All `document_id` references in mentions exist in documents array
- [ ] All mention spans are accurate: `document[start:end] == mention_text`
- [ ] `mention_id` values are unique across all mentions
- [ ] Difficulty distribution includes easy/medium/hard cases
- [ ] Ambiguous cases use `null` for expected_entity_id

✅ **scenario_metadata.json**:

- [ ] `scenario_id` matches folder name
- [ ] `entities_count` matches actual entity count
- [ ] `documents_count` matches actual document count
- [ ] `mentions_count` matches actual mention count (excluding `n/a`)
- [ ] `difficulty_distribution` matches actual distribution

✅ **Documents**:

- [ ] All documents are realistic and natural
- [ ] All documents have 2+ entity mentions
- [ ] Mix of document types (not all one type)
- [ ] Varied difficulty levels across documents

## Testing Your Scenario

After creating a scenario, test it with the scenario loader:

```bash
# List all scenarios
python -m tests.lib.scenario_loader list

# Validate structure
python -m tests.lib.scenario_loader validate {domain}/{scenario_name}

# Get scenario info
python -m tests.lib.scenario_loader info {domain}/{scenario_name}
```

**Validation will check**:

- File structure correctness
- JSON validity
- Ground truth completeness
- Span accuracy
- Reference integrity (entity IDs, document IDs)
- Statistics consistency

## Common Mistakes to Avoid

❌ **Wrong document naming**:

```
doc_1_news.md          # Missing zero padding
doc_01_news.md         # Only 2 digits (should be 3)
news_001.md            # Wrong order (type comes after number)
doc_001.md             # Missing type
```

✅ **Correct document naming**:

```
doc_001_news.md
doc_002_email.txt
doc_003_report.md
```

❌ **Wrong mention_id format**:

```
"mention_1_1"          # Missing zero padding
"mention_001"          # Missing mention number
"m_001_001"            # Wrong prefix
```

✅ **Correct mention_id format**:

```
"mention_001_001"
"mention_001_002"
"mention_002_001"
```

❌ **Wrong span calculation**:

```json
{
  "mention_text": "Apple Inc.",
  "mention_span": [45, 55]  # If document[45:55] != "Apple Inc.", THIS IS WRONG
}
```

✅ **Correct span calculation**:

```python
text = "Apple Inc."
start = document.find(text)
end = start + len(text)
assert document[start:end] == text  # MUST be true
```

❌ **Missing context signals**:

```json
{
  "mention_text": "Apple iPhone developer",
  "context_signals": [],  # Should list: product:iPhone, context:developer
  "difficulty": "easy"
}
```

✅ **Complete context signals**:

```json
{
  "mention_text": "Apple iPhone developer",
  "context_signals": ["product:iPhone", "context:developer program"],
  "difficulty": "easy"
}
```

## Example: Complete Minimal Scenario

Here's a minimal valid scenario:

**Directory**: `tests/data/business/simple_test/`

**File**: `doc_001_email.txt`

```
Subject: Meeting with Acme Corp

Hi team,

We have a meeting with Acme Corporation tomorrow at 10 AM to discuss the new project.

Thanks,
John
```

**File**: `ground_truth.json`

```json
{
  "entities": [
    {
      "entity_id": "aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa",
      "canonical_name": "Acme Corporation",
      "kind": "company",
      "aliases": ["Acme Corp", "Acme"],
      "attributes": {
        "industry": "Manufacturing"
      }
    }
  ],
  "documents": [
    {
      "document_id": "doc_001",
      "original_filename": "email_meeting.txt",
      "document_type": "email",
      "word_count": 25
    }
  ],
  "entity_mentions": [
    {
      "mention_id": "mention_001_001",
      "document_id": "doc_001",
      "mention_text": "Acme Corp",
      "mention_span": [31, 40],
      "expected_entity_id": "aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa",
      "expected_canonical_name": "Acme Corporation",
      "kind": "company",
      "context_signals": ["context:meeting"],
      "difficulty": "easy",
      "why_easy_or_hard": "Alias matches entity directly"
    },
    {
      "mention_id": "mention_001_002",
      "document_id": "doc_001",
      "mention_text": "Acme Corporation",
      "mention_span": [50, 66],
      "expected_entity_id": "aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa",
      "expected_canonical_name": "Acme Corporation",
      "kind": "company",
      "context_signals": [],
      "difficulty": "easy",
      "why_easy_or_hard": "Exact match to canonical name"
    }
  ]
}
```

**File**: `scenario_metadata.json`

```json
{
  "scenario_name": "Simple Test",
  "scenario_id": "simple_test",
  "domain": "business",
  "focus": "Basic entity recognition test",
  "description": "Minimal test scenario with one entity and two mentions for validation.",
  "created_date": "2025-10-08",
  "entities_count": 1,
  "documents_count": 1,
  "mentions_count": 2,
  "difficulty_distribution": {
    "easy": 2
  },
  "success_criteria": {
    "overall_accuracy": 1.0
  },
  "context_signals": ["context"]
}
```

## Summary: Quick Checklist

When generating a scenario, create:

1. ✅ **Directory**: `tests/data/{domain}/{scenario_name}/`
2. ✅ **Documents**: `doc_001_{type}.{ext}`, `doc_002_{type}.{ext}`, ...
3. ✅ **ground_truth.json**: With `entities`, `documents`, `entity_mentions` arrays
4. ✅ **scenario_metadata.json**: With scenario description and success criteria
5. ✅ **Validate**: Run `python -m tests.lib.scenario_loader validate {domain}/{scenario_name}`

Follow this format exactly, and your scenarios will automatically integrate with the test suite!
