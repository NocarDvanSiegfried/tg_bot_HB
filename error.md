0s
Run ssh-keyscan -H *** >> ~/.ssh/known_hosts
  ssh-keyscan -H *** >> ~/.ssh/known_hosts
  shell: /usr/bin/bash -e {0}
  env:
    SSH_AUTH_SOCK: /tmp/ssh-doyLBU1Z0I5J/agent.2119
    SSH_AGENT_PID: 2120
getaddrinfo ***: Temporary failure in name resolution
getaddrinfo ***: Temporary failure in name resolution
getaddrinfo ***: Temporary failure in name resolution
getaddrinfo ***: Temporary failure in name resolution
getaddrinfo ***: Temporary failure in name resolution
Error: Process completed with exit code 1.

Run ssh $DEPLOY_USER@$*** << EOF
  ssh $DEPLOY_USER@$*** << EOF
    cd $DEPLOY_PATH
    docker compose pull backend:previous frontend:previous || true
    docker compose up -d backend frontend
  EOF
  shell: /usr/bin/bash -e {0}
  env:
    SSH_AUTH_SOCK: /tmp/ssh-doyLBU1Z0I5J/agent.2119
    SSH_AGENT_PID: 2120
    ***: ***
    DEPLOY_USER: ***
    DEPLOY_PATH: ***
Pseudo-terminal will not be allocated because stdin is not a terminal.
ssh: Could not resolve hostname deploy_host: Temporary failure in name resolution
Error: Process completed with exit code 255.