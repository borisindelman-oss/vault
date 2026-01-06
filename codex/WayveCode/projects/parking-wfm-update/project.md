# Parking WFM Update

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
- **What it is:** Update the parking model config to use the latest world model config and align training defaults with release settings.
- **Why it matters:** Avoid config mismatches that previously caused bugs and ensure parking training uses the approved world model.
- **Primary users:** Parking model training owners and release stakeholders.

## Status
- **Phase:** Phase 1 - Discovery
- **Status:** active
- **Last updated:** 2026-01-06
- **Current priorities:**
  - Locate the December release world model config in Notion and confirm its name.
  - Compare BCWFMSt100xYoloCfg vs WFMStOctober2025Cfg defaults used in parking training.
  - Align training module config (STTrainingModuleCfg vs StBcCfg) and document differences.
  - Plan changes on branch soham/12-18-Parking-model before mainline merge.
- **Blockers:**
  - None

## Requirements
- **Problem statement:** Parking training is using BCWFMSt100xYoloCfg and STTrainingModuleCfg, while release uses WFMStOctober2025Cfg and StBcCfg, creating mismatched defaults and prior bugs.
- **Target users:** Parking model trainers and release owners who need consistent configs.
- **Integrations:** WayveCode repo, branch soham/12-18-Parking-model, W&B project parking, Notion release notes for December world model.
- **Constraints:** Changes must be applied on the branch (parking model not in main); preserve training stability; align with December release if available.
- **Success criteria:** Parking training config uses the latest approved world model config (WFMStOctober2025Cfg or December release equivalent) and the release-aligned training module defaults (StBcCfg), with a successful training run logged in W&B.

## Design
### Tech Stack
- Frontend:
- Backend:
- Database:
- Hosting:
- Auth:
- Observability:

### Architecture

### Data Model

### API Integrations

### UI / UX

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
-

## Notes
-
