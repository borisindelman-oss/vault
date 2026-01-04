# Dummy Project

| Section | Link |
| --- | --- |
| Overview | [Overview](#overview) |
| Status | [Status](#status) |
| Requirements | [Requirements](#requirements) |
| Design | [Design](#design) |
| Build Phases | [Build Phases](#build-phases) |
| Quality Checklist | [Quality Checklist](#quality-checklist) |
| Runbook | [Runbook](#runbook) |
| Decisions | [Decisions](#decisions) |
| Notes | [Notes](#notes) |

## Overview
- **What it is:** Sample project to demonstrate the vault-based workflow.
- **Why it matters:** Shows the single-file structure and status tracking.
- **Primary users:** Boris + Codex

## Status
- **Phase:** Phase 1 - Foundation
- **Status:** active
- **Last updated:** 2026-01-04
- **Current priorities:**
  - Define initial requirements
  - Choose tech stack
  - Set up repo skeleton
- **Blockers:**
  - None

## Requirements
- **Problem statement:** Provide an example project layout in the vault.
- **Target users:** Internal (Codex workflow).
- **Integrations:** None.
- **Constraints:** Vault-first, no GitHub tracker.
- **Success criteria:** Project file exists, readable, and demonstrates sections.

## Design
### Tech Stack
- Frontend: TBD
- Backend: TBD
- Database: TBD
- Hosting: TBD
- Auth: TBD
- Observability: TBD

### Architecture
- TBD

### Data Model
- TBD

### API Integrations
- TBD

### UI / UX
- TBD

## Build Phases
### Phase 1: Foundation
- [ ] Initialize project with chosen framework
- [ ] Set up database with schema
- [ ] Implement authentication system
- [ ] Create base UI layout
- [ ] Configure deployment pipeline
- [ ] Verify deployment works

### Phase 2: Core Features
- [ ] Build all main pages/views
- [ ] Connect to real data (CRUD operations)
- [ ] Implement user management
- [ ] Create settings/configuration UI
- [ ] Add loading and error states
- [ ] Test core user flows

### Phase 3: Integration & Automation
- [ ] Integrate external APIs
- [ ] Set up webhooks/background jobs
- [ ] Implement business logic
- [ ] Add notifications
- [ ] Create admin tools
- [ ] Test all integrations

### Phase 4: Polish & Delivery
- [ ] Comprehensive error handling
- [ ] User onboarding flow
- [ ] Documentation complete
- [ ] Performance optimization
- [ ] Security review
- [ ] Final user testing

## Quality Checklist
### Functionality
- [ ] All features work as specified
- [ ] Happy path tested thoroughly
- [ ] Edge cases handled
- [ ] Error states implemented

### Code Quality
- [ ] No console errors
- [ ] Types/linters clean
- [ ] API routes have error handling
- [ ] Database queries optimized

### Security
- [ ] Authentication required where needed
- [ ] Input validation implemented
- [ ] RLS policies active (if applicable)
- [ ] Environment variables secure

### User Experience
- [ ] Loading states on async operations
- [ ] Error messages helpful
- [ ] Mobile responsive
- [ ] Accessible (keyboard nav, screen readers)

### Documentation
- [ ] README updated
- [ ] Setup instructions clear
- [ ] Environment variables documented
- [ ] Common issues noted

## Runbook
### Setup
```sh
# example
# pnpm install
```

### Dev
```sh
# example
# pnpm dev
```

### Test
```sh
# example
# pnpm test
```

### Build
```sh
# example
# pnpm build
```

### Deploy
```sh
# example
# pnpm deploy
```

## Decisions
- Vault-first project management (no GitHub tracker).

## Notes
- Legacy multi-file docs still exist in this folder; safe to remove once you confirm.
