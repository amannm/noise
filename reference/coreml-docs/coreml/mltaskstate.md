# MLTaskState

**Enumeration**

**Framework:** Core ML

**Availability:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+, watchOS 6.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

The state of a machine learning task.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
enum MLTaskState
```

## Topics

### Transient states

- [MLTaskState.running](mltaskstate/running.md)
  The state of a machine learning task that’s executing.

- [MLTaskState.suspended](mltaskstate/suspended.md)
  The state of a machine learning task that’s paused.

- [MLTaskState.cancelling](mltaskstate/cancelling.md)
  The state of a machine learning task that’s in mid-termination, before it could finish successfully.

### Final states

- [MLTaskState.completed](mltaskstate/completed.md)
  The state of a machine learning task that has finished successfully.

- [MLTaskState.failed](mltaskstate/failed.md)
  The state of a machine learning task that has terminated due to an error.

### Creating a task state

- [init(rawValue:)](mltaskstate/init(rawvalue:).md)

## See Also

### Checking the state of a task

- [state](mltask/state.md)
  The current state of the machine learning task.

- [error](mltask/error.md)
  The underlying error if the task is in a failed state.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
