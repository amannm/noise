# MLUpdateProgressEvent

**Structure**

**Framework:** Core ML

**Availability:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+, watchOS 6.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

A type of event during a model update task.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
struct MLUpdateProgressEvent
```

## Topics

### Getting progress event types

- [trainingBegin](mlupdateprogressevent/trainingbegin.md)
  An event that represents the start of training.

- [miniBatchEnd](mlupdateprogressevent/minibatchend.md)
  An event that represents the end of a mini-batch within a training epoch.

- [epochEnd](mlupdateprogressevent/epochend.md)
  An event that represents the end of training epoch.

### Creating a progress event

- [init(rawValue:)](mlupdateprogressevent/init(rawvalue:).md)
  Creates a progress event for the given integer.

## See Also

### Getting the update context

- [event](mlupdatecontext/event.md)
  The event type that triggered an update task to notify your app’s completion and update progress handlers.

- [task](mlupdatecontext/task.md)
  The update task that generated the update context.

- [parameters](mlupdatecontext/parameters.md)
  The parameters for the update task.

- [MLParameterKey](mlparameterkey.md)
  The keys for the parameter dictionary in a model configuration or a model update context.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
