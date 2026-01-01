# resume(withParameters:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+, watchOS 6.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLUpdateTask](../mlupdatetask.md)

---

Resumes a model update with updated parameter values.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func resume(withParameters updateParameters: [MLParameterKey : Any])
```

### Parameters

- **`updateParameters`**
  Model training parameter values to replace those currently set in the update task.

## Overview

Use this method to resume the model update task with newer parameter values. You use this method within the closures you provide in an [MLUpdateProgressHandlers](../mlupdateprogresshandlers.md) instance to resume the [MLUpdateTask](../mlupdatetask.md).

## See Also

### Starting and Resuming an Update

- [MLParameterKey](../mlparameterkey.md)
  The keys for the parameter dictionary in a model configuration or a model update context.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
