# AI Agent Guidelines

This repository follows secure AI-agent harness practices inspired by zeekiankok92/aixtech-agent-harness-demo.

- Never commit secrets, private keys, API keys, or personal data.
- All strategy logic is paper-only research. No live order placement.
- Use redaction for any sensitive patterns in logs or outputs.
- Prefer synthetic fixtures for testing.
- Run CI gates (tests, lint, secret scan) before considering changes complete.
- Document AI assistance in commit messages or docs when relevant.
- Respect data residency and PDPA-style tripwires.
