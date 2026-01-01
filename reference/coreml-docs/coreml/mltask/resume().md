# resume()

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+, watchOS 6.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTask](../mltask.md)

---

Begins or resumes a machine learning task.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func resume()
```

## Overview

Use this method to start a task for the first time or resumes a task that has paused. Tasks pause when they notify your app’s progress handlers, such as those you provide to an [MLUpdateProgressHandlers](../mlupdateprogresshandlers.md) instance.

## See Also

### Starting and stopping a task

- [cancel()](cancel().md)
  Cancels a machine learning task before it completes.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
