
# Experiment 01 — Symbolic AI Principles

**ISTQB CT-GenAI | AI Approaches**

## Learning Objective

Understand how symbolic AI uses explicitly represented knowledge and logical rules rather than learning patterns from training data.

## Business Scenario

CVI analyzes vintage jewelry descriptions to identify reported designer signatures.

## Implementation

I created a minimal Python keyword classifier using predefined rules:

```python
def has_signature_evidence(description: str) -> bool:
    text = description.lower()

    if "unsigned" in text:
        return False

    if "signed" in text:
        return True

    return False
```

This illustrates rule-based decision-making, not a complete symbolic AI inference engine.

## Test Results

| Scenario | Expected | Result |
|---|---|---|
| Signed MONET earrings | True | Passed |
| Unsigned Dior-style earrings | False | Passed |
| No signature information | False | Passed |
| Signed, but expert says fake | False | Failed |

The fourth test introduces an extended requirement: expert-rejected signatures should not count as valid authenticity evidence.

The original classifier only detects reported signatures. Therefore, this failure also highlights a difference between the original and extended requirements.

## Why Is It Called Symbolic AI?

Historically, symbolic AI represented knowledge through symbols, facts and logical rules to derive conclusions.

Unlike machine learning, it does not require learning statistical patterns from training examples.

Our Python classifier illustrates only the simplest rule-based principle. It is not a complete symbolic AI system.

## ISTQB Takeaway

**Symbolic AI:** Explicit knowledge representation and logical reasoning.

**Machine Learning:** Patterns learned from training data.

Adding a manually written rule does not mean the system has learned.

## Reproduce the Experiment

Run:

```bash
python -m pytest test_symbolic_rules.py -v
```

The expert-rejection test is intentionally expected to fail.

## Knowledge Check

**Question:** If I add a rule for expert rejection, has the system learned anything?

**Answer:** No. The developer has manually expanded the system's rules.
