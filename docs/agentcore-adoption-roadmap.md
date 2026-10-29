# AgentCore Adoption Roadmap

Platform: AI Enabler

Version: 1.0

Status: Strategic Roadmap

Purpose:

Define the migration path from the current AI Enabler implementation
to an AWS AgentCore-based platform.

This document identifies:

- What remains custom
- What will be provided by AWS
- Migration phases
- Technical priorities
- Long-term target architecture

==================================================

CURRENT STATE

==================================================

Current Agents

- analyze_organization
- function_analysis
- ai_opportunity
- roadmap
- executive_report

Current Capabilities

- Agent workflow
- JSON artifact pipeline
- Governance documentation
- Agent catalog
- Authorization matrix
- Audit schema
- Gateway MVP

Current Gaps

- Identity management
- Runtime orchestration
- MCP integration
- Observability
- Production security
- Cost management

==================================================

ADOPTION PRINCIPLES

==================================================

Principle 1

Preserve business logic.

--------------------------------------------------

Principle 2

Adopt cloud-native infrastructure.

--------------------------------------------------

Principle 3

Avoid rebuilding managed AWS services.

--------------------------------------------------

Principle 4

Separate business governance from platform infrastructure.

--------------------------------------------------

Principle 5

Keep agents independent and reusable.

==================================================

WHAT WE KEEP

==================================================

AI Enabler retains ownership of:

- Agent definitions
- Prompt design
- Workflow design
- Agent catalog
- Authorization matrix
- Governance model
- Business rules
- Business policies
- Executive recommendations
- Opportunity frameworks

==================================================

WHAT AWS PROVIDES

==================================================

Target AWS Services

- AgentCore Runtime
- AgentCore Gateway
- AgentCore Identity
- AgentCore Observability
- MCP Connectivity
- Secure Agent Hosting
- Runtime Isolation
- Scaling

==================================================

BUILD VS BUY

==================================================

Component

Agent Definitions

Decision

BUILD

Owner

AI Enabler