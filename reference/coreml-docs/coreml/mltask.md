# MLTask

**Class**

**Framework:** Core ML

**Availability:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+, watchOS 6.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

An abstract base class for machine learning tasks.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
class MLTask
```

## Overview

You don’t create use this class directly. Instead, use a class that inherits from this one, such as [MLUpdateTask](mlupdatetask.md).

## Topics

### Identifying a task

- [taskIdentifier](mltask/taskidentifier.md)
  A unique name of the task to distinguish it from all other tasks at runtime.

### Starting and stopping a task

- [resume()](mltask/resume().md)
  Begins or resumes a machine learning task.

- [cancel()](mltask/cancel().md)
  Cancels a machine learning task before it completes.

### Checking the state of a task

- [state](mltask/state.md)
  The current state of the machine learning task.

- [MLTaskState](mltaskstate.md)
  The state of a machine learning task.

- [error](mltask/error.md)
  The underlying error if the task is in a failed state.

## See Also

### On-device model updates

- [Personalizing a Model with On-Device Updates](personalizing-a-model-with-on-device-updates.md)
  Modify an updatable Core ML model by running an update task with labeled data.

- [MLUpdateTask](mlupdatetask.md)
  A task that updates a model with additional training data.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
