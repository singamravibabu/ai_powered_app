# Exploring Workflows
---
## Exploring workflow capabilities
- **Structure of a workflow**
    - Events/triggers: Workflows are triggered for specific events.
    - Jobs: Workflow consists multiple jobs, and each running a sequence of steps. Jobs can run in parallel or squentially.
    - Steps: Jobs consists of steps that performs individual tasks.

### Events or triggers
- GitHub Actions workflows are driven by events.
- Events are grouped into categories:
    - Code-related events
        - push, pull_request, and pull_request_events
    - Issue and project management events
        - issue, issue_comment, and milestone
    - Scheduled events
        - cron, workflow_dispatch, and repository_dispatch
    - Manual events
        - workflow_dispatch
    - Repository and organizational management events
        - repository, team, and organization
    - External events
        - repository_dispatch and workflow_run

### Jobs
- Jobs are building blocks of GitHub Actions workflows.
- Invidual unit of work consisting of series of steps.
- A structure of a job includes:
    - Name: descriptive name for the job
    - Runs on: using the keyword `runs-on`
        - ubuntu-latest, windows-latest, or macos-latest, or a self-hosted lastest
    - Steps: sequence of steps that perform individual tasks