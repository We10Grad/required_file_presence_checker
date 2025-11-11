# File Presence Checker CI/CD Pipeline
Testing the workflow again

## Overview
This project uses GitHub Actions to automatically check for required files in the repository and logs successful runs to AWS CloudWatch.

## Required Files
The pipeline validates these files exist in the repo root:
- `README.md`
- `.gitignore`

## Setup

### AWS CloudWatch
Create these log groups in the AWS CloudWatch Console:
- `/github-actions/required-files-checker/beta` (for pull requests)
- `/github-actions/required-files-checker/prod` (for merges to main)

### GitHub Secrets
Add these secrets in your repository settings (Settings > Secrets and variables > Actions):

| Secret Name | Description |
|-------------|-------------|
| `AWS_ACCESS_KEY_ID` | Your AWS access key |
| `AWS_SECRET_ACCESS_KEY` | Your AWS secret key |
| `AWS_REGION` | AWS region (e.g., `us-east-1`) |

## How It Works

### Workflows
- **`on_pull_request.yml`**: Runs on pull requests to main, logs to beta
- **`on_merge.yml`**: Runs on push to main, logs to prod

### Process
1. Checkout code
2. Run `check_required_files.py` to verify files exist
3. If successful, log workflow metadata to CloudWatch using AWS CLI

### AWS CLI Logging
The workflow creates a log stream with the current timestamp and sends a log entry containing:
- Workflow name
- Commit SHA
- GitHub actor
- Timestamp

Commands used:
```bash
aws logs create-log-stream --log-group-name <GROUP> --log-stream-name <TIMESTAMP>
aws logs put-log-events --log-group-name <GROUP> --log-stream-name <TIMESTAMP> --log-events timestamp=<EPOCH>,message='<JSON>'
```

## Running Manually
To test the file check script locally:
```bash
python3 check_required_files.py
```
- Exits with code 0 if all files present (silent)
- Exits with code 1 and prints missing files if any are missing

## Viewing CloudWatch Logs
1. Go to AWS CloudWatch Console
2. Navigate to Logs > Log groups
3. Select `/github-actions/required-files-checker/beta` or `/github-actions/required-files-checker/prod`
4. Click on a log stream (timestamp) to view entries

## What Happens When Files Are Missing
- Script prints: `Missing Files: <filename>`
- Workflow fails with exit code 1
- Pull request check shows as failed
- No log is sent to CloudWatch (only logs successful runs)
- PR cannot be merged until files are added

## Troubleshooting
- **AWS authentication errors**: Check that all three secrets are set correctly
- **Log groups not found**: Create them in CloudWatch before running workflows
- **Script fails but files exist**: Files must be in repo root with exact names (case-sensitive)
Test edit to trigger workflow
