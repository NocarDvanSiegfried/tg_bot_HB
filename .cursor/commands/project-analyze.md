# project-analyze

Write your command content here.

This command will be available in chat with /project-analyze

project-analyze:
  description: >
    Perform a deep static analysis of the entire project using context7 and internal rules.
    Detect architectural violations, duplicate logic, cyclic imports, unused files,
    invalid imports, hardcoded values, poor modularity, and structural inconsistencies.
    Produce a detailed report with recommended improvements.

  steps:
    - call: context7.load
    - analyze: duplicates
    - analyze: cyclic-imports
    - analyze: unused-files
    - analyze: invalid-imports
    - analyze: architecture
    - analyze: hardcoded-values
    - output: "Project analysis completed."

