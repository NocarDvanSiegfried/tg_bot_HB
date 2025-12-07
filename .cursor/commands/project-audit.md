# project-audit

Write your command content here.

This command will be available in chat with /project-audit

project-audit:
  description: >
    Run a full project quality audit before commit or release.
    Perform static analysis, architecture validation, duplicate detection,
    hardcoded value detection, verify production build, and run Playwright UI checks.

  steps:
    - call: context7.load
    - analyze: duplicates
    - analyze: cyclic-imports
    - analyze: invalid-imports
    - analyze: architecture
    - analyze: hardcoded-values
    - run: "npm run build"
    - run: "docker compose build"
    - call: playwright.run
    - output: "Full audit completed."
