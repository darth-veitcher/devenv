# Docker MCP Server Integration Guide

**Date**: July 31, 2025  
**Status**: Implemented ✅

## Overview

The Docker MCP server has been successfully integrated into our solo developer containerized environment. This enables AI agents to manage Docker containers, images, and compose stacks directly through natural language commands.

## Installation Details

### Configuration Added

1. **Root Project** (`/workspace/.mcp.json`):
```json
"docker": {
  "type": "stdio",
  "command": "uvx",
  "args": ["docker-mcp"],
  "env": {}
}
```

2. **Template Project** (`/workspace/{{cookiecutter.project_slug}}/.mcp.json`):
- Same configuration, automatically included in generated projects

3. **Settings Files Updated**:
- `.claude/settings.json` - Added "docker" to enabledMcpjsonServers
- `.claude/settings.local.json` - Added "docker" to enabledMcpjsonServers
- `{{cookiecutter.project_slug}}/.claude/settings.json` - Added "docker" to enabledMcpjsonServers

## Available Docker MCP Commands

The Docker MCP server provides four core tools:

### 1. `create-container`
Creates and runs a standalone Docker container.

**Parameters**:
- `image`: Docker image to use (required)
- `name`: Container name (optional)
- `ports`: Port mapping as "host:container" (optional)
- `env`: Environment variables as key-value pairs (optional)

**Example Usage**:
```yaml
# In deploy.yml agent
- tool: docker.create-container
  params:
    image: "nginx:latest"
    name: "web-server"
    ports: "8080:80"
```

### 2. `deploy-compose`
Deploys a Docker Compose stack from YAML configuration.

**Parameters**:
- `project_name`: Name for the compose project (required)
- `compose_yaml`: Docker Compose YAML content (required)

**Example Usage**:
```yaml
# In feature.yml agent
- tool: docker.deploy-compose
  params:
    project_name: "my-app"
    compose_yaml: |
      version: '3.8'
      services:
        web:
          image: my-app:latest
          ports:
            - "3000:3000"
```

### 3. `list-containers`
Lists all Docker containers (running and stopped).

**Example Usage**:
```yaml
# In debug.yml agent
- tool: docker.list-containers
```

### 4. `get-logs`
Retrieves logs from a specific container.

**Parameters**:
- `container`: Container name or ID (required)

**Example Usage**:
```yaml
# In debug.yml agent
- tool: docker.get-logs
  params:
    container: "my-app-web-1"
```

## Agent Integration Examples

### Deploy Agent Enhancement

```yaml
# .claude/agents/deploy.yml
name: "Deploy Master"
description: "Handles all deployment tasks autonomously"
tools:
  - Bash
  - Read
  - Write
  - Edit
  - docker  # NEW: Docker MCP integration
triggers:
  - "git push to main"
  - "make deploy"
prompt: |
  You are a deployment specialist with Docker MCP access.
  
  For local testing before cloud deployment:
  1. Use docker.list-containers to check running services
  2. Use docker.create-container to test the application locally
  3. Use docker.get-logs to verify it's working correctly
  4. Then proceed with Railway/Fly.io deployment
  
  For Docker Compose deployments:
  1. Read the docker-compose.yml file
  2. Use docker.deploy-compose to launch the stack
  3. Monitor with docker.get-logs
```

### Debug Agent Enhancement

```yaml
# .claude/agents/debug.yml
name: "Error Eliminator"
description: "Finds and fixes errors autonomously"
tools:
  - Read
  - Grep
  - Edit
  - Bash
  - Sequential
  - docker  # NEW: Docker MCP integration
prompt: |
  You are an expert debugger with Docker access.
  
  When debugging containerized applications:
  1. Use docker.list-containers to see all containers
  2. Use docker.get-logs to retrieve error logs
  3. Analyze logs to identify root causes
  4. Fix issues in code or configuration
  5. Restart containers with docker.create-container
```

### Feature Agent Enhancement

```yaml
# .claude/agents/feature.yml
name: "Feature Builder"
description: "Creates complete features from descriptions"
tools:
  - Read
  - Write
  - MultiEdit
  - Bash
  - Task
  - docker  # NEW: Docker MCP integration
prompt: |
  When building features that require containers:
  1. Create necessary Docker configurations
  2. Use docker.deploy-compose for multi-service features
  3. Test locally with docker.create-container
  4. Verify with docker.get-logs before marking complete
  
  Example: Adding Redis caching
  - Deploy Redis with docker.create-container
  - Configure app to connect to Redis container
  - Test caching functionality
```

## Makefile Integration

Update the Makefile to leverage Docker MCP:

```makefile
# Docker-powered commands
docker-status:
	@echo "🐳 Checking Docker containers..."
	@claude-code agent run docker "List all containers and their status"

docker-logs:
	@echo "📋 Fetching container logs..."
	@claude-code agent run debug "Get logs from all running containers"

docker-cleanup:
	@echo "🧹 Cleaning up Docker resources..."
	@claude-code agent run docker "Stop and remove all project containers"

# Local testing before deployment
test-local:
	@echo "🧪 Testing locally with Docker..."
	@claude-code agent run deploy "Deploy the app locally using Docker first"
```

## Security Considerations

1. **Container Isolation**: All containers run in isolated environments
2. **Resource Limits**: Currently not supported by docker-mcp (planned feature)
3. **Network Security**: Containers use default Docker networking
4. **Volume Mounting**: Not yet supported (security feature)

## Current Limitations

The Docker MCP server v0.1.0 has these limitations:
- ❌ No environment variable support in compose
- ❌ No volume management
- ❌ No network management
- ❌ No health checks
- ❌ No restart policies
- ❌ No resource limits

## Future Enhancements

As the Docker MCP server evolves, we plan to:
1. Add volume support for persistent data
2. Implement health check monitoring
3. Add resource limit controls
4. Support custom networks
5. Enable container exec functionality

## Testing the Integration

To verify Docker MCP is working:

```bash
# In Claude Code
> List all Docker containers
> Create a test nginx container on port 8080
> Get logs from the test container
> Deploy a compose stack with Redis and PostgreSQL
```

## Troubleshooting

If Docker MCP commands fail:
1. Ensure Docker Desktop/Engine is running
2. Check `uvx` is installed: `pip install uv`
3. Verify Docker permissions: `docker ps`
4. Check MCP server logs in Claude Code

## Conclusion

The Docker MCP integration significantly enhances our AI agents' capabilities, allowing them to:
- Test applications locally before cloud deployment
- Debug containerized services effectively
- Manage multi-container applications
- Provide instant feedback on container status

This aligns perfectly with our goal of enabling solo developers to build and deploy applications at superhuman speed.