The Argonaut Schedule Notification Profile is defined for use as the payload when sending  notifications to a subscriber as described in the updating slots step in [Use Case 3 Prefetching Open Slots](patient-scheduling.html#use-case-3-prefetching-open-slots). It identifies which core elements, extensions, vocabularies and value sets SHALL be present in the resource when using this profile.

### Mandatory Data Elements

**Each Slot must have:**

1. an actor ("lowest schedulable unit for subscriber")
1. a date range (preferably a single day)


**Additional Profile specific implementation guidance:**

- None

#### Examples

- [Example 1](Schedule-example1.html)
