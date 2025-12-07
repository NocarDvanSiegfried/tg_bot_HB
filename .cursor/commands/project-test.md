# project-test

Write your command content here.

This command will be available in chat with /project-test

project-tdd:
  description: >
    Execute a full TDD cycle: generate tests for the target module, implement logic,
    run the test suite, fix failing tests, and finalize the implementation.
  steps:
    - call: context7.load
    - generate: tests
    - implement: logic
    - run: "npm test"
    - fix: failing-tests
    - output: "TDD cycle completed."
