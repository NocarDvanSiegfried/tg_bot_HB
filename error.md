Run if [ -z "$DEPLOY_HOST" ] || [ -z "$DEPLOY_USER" ] || [ -z "$DEPLOY_PATH" ]; then
  if [ -z "$DEPLOY_HOST" ] || [ -z "$DEPLOY_USER" ] || [ -z "$DEPLOY_PATH" ]; then
    echo "❌ Required ***ment variables are empty"
    exit 1
  fi
  export DEPLOY_HOST DEPLOY_USER DEPLOY_PATH
  ssh "$DEPLOY_USER@$DEPLOY_HOST" << EOF
    cd "$DEPLOY_PATH"
    # Tag current images as previous for rollback
    docker images --format "{{.Repository}}:{{.Tag}}" | grep -E "(backend|frontend)" | while read image; do
      if [[ ! "\$image" =~ :previous$ ]]; then
        docker tag "\$image" "\${image%:*}:previous" || true
      fi
    done
  EOF
  shell: /usr/bin/bash -e {0}
  env:
    SSH_AUTH_SOCK: /tmp/ssh-l6A641RwR6vK/agent.2124
    SSH_AGENT_PID: 2125
    DEPLOY_HOST: ***
    DEPLOY_USER: ***
    DEPLOY_PATH: ***
Pseudo-terminal will not be allocated because stdin is not a terminal.
Permission denied, please try again.
Permission denied, please try again.
***@***: Permission denied (publickey,password).
Error: Process completed with exit code 255.

Run if [ -z "$DEPLOY_HOST" ] || [ -z "$DEPLOY_USER" ] || [ -z "$DEPLOY_PATH" ]; then
  if [ -z "$DEPLOY_HOST" ] || [ -z "$DEPLOY_USER" ] || [ -z "$DEPLOY_PATH" ]; then
    echo "❌ Required ***ment variables are empty, cannot rollback"
    exit 1
  fi
  export DEPLOY_HOST DEPLOY_USER DEPLOY_PATH
  ssh "$DEPLOY_USER@$DEPLOY_HOST" << EOF
    cd "$DEPLOY_PATH"
    docker compose pull backend:previous frontend:previous || true
    docker compose up -d backend frontend
  EOF
  shell: /usr/bin/bash -e {0}
  env:
    SSH_AUTH_SOCK: /tmp/ssh-l6A641RwR6vK/agent.2124
    SSH_AGENT_PID: 2125
    DEPLOY_HOST: ***
    DEPLOY_USER: ***
    DEPLOY_PATH: ***
Pseudo-terminal will not be allocated because stdin is not a terminal.
Permission denied, please try again.
Permission denied, please try again.
***@***: Permission denied (publickey,password).
Error: Process completed with exit code 255.

Run if [ "failure" == "success" ]; then
  if [ "failure" == "success" ]; then
    echo "✅ Deployment successful to production"
  else
    echo "❌ Deployment failed to production"
  fi
  shell: /usr/bin/bash -e {0}
  env:
    SSH_AUTH_SOCK: /tmp/ssh-l6A641RwR6vK/agent.2124
    SSH_AGENT_PID: 2125
❌ Deployment failed to production