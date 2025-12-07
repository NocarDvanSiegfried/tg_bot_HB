# project-verify

Write your command content here.

This command will be available in chat with /project-verify

project-verify:
  description: >
    Verify that the entire project builds and runs successfully.
    Check the frontend (npm dev/build), backend (Docker build/up),
    and run Playwright UI checks to validate UI behavior.

  steps:
    - run: "npm run dev"
    - run: "npm run build"
    - run: "docker compose build"
    - run: "docker compose up"
    - call: playwright.run
    - output: "Project verification completed."
