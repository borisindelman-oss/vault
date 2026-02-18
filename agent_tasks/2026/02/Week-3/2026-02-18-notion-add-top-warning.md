# Notion update: add top TorchScript contract warning

Date: 2026-02-18
Page: Newsletter - Interleaving Models in the Parking Deployment Wrapper
URL: https://www.notion.so/wayve/Newsletter-Interleaving-Models-in-the-Parking-Deployment-Wrapper-30503da5d69a813aa0f7d021923994f5

## Change made
Inserted at beginning of page:
- `## 0) Warning: TorchScript Interface Contract`

Warning states that changing wrapper type, input signature, or output signature requires interleaving code updates, because TorchScript requires fixed interfaces and a fully generic dynamic interleaving wrapper is not practical for this path.
