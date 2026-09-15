# Example — Software

## Problem statement
Users can manually connect to a supported network path through the OS UI, but the product needs a one-click native connection experience.

## Desired outcome
A user presses Connect in our application and the OS establishes the connection without third-party helper software or manual Settings navigation.

## Success criteria
- Works repeatedly on the target managed Windows build/device.
- No custom kernel driver unless every acceptable user-mode path is evidence-backed as unavailable and a human approves escalation.
- Connection state is observable by the app.
- Failure produces a recoverable user-visible state.

## Non-goals
Replacing the operating system networking stack.
