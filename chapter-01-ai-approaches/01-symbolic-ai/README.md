\# Experiment 01 — Symbolic AI Principles



\*\*ISTQB CT-GenAI | Chapter 1: AI Approaches\*\*



\## Learning objective



Understand how symbolic AI uses explicitly represented knowledge and logical rules rather than learning patterns from training data.



\## Business scenario



CVI analyzes vintage jewelry descriptions to identify reported designer signatures.



\## Implementation



I created a minimal Python keyword classifier using predefined rules:



\- `unsigned` → False

\- `signed` → True

\- Otherwise → False



This demonstrates rule-based decision-making, not a complete symbolic AI inference engine.



\## Test results



Three basic scenarios passed.



A fourth scenario introduced an expert-rejected signature:



\- Input: "Signed, but expert says fake"

\- Expected under an extended authenticity-evidence requirement: False

\- Actual: True



This test demonstrates that the classifier does not account for expert rejection.



\## Why is this related to AI?



Historically, symbolic AI represented knowledge through symbols, facts and logical rules to support reasoning without statistical training.



This small experiment illustrates the rule-based principle. Ordinary Python conditions alone do not constitute a complete AI system.



\## QA finding



Detecting a reported signature and determining whether it is authentic are different requirements.



The fourth test exposes this distinction rather than necessarily proving a defect in the original classifier.



\## ISTQB takeaway



Symbolic AI uses explicit knowledge representations and logical rules. Adding another manually written rule does not mean the system has learned.



\## Reproduce



```bash

python -m pytest test\_symbolic\_rules.py -v

```



The fourth test is intentionally expected to fail in this demonstration.:w

