# parameters

**Instance Property**

**Framework:** Core ML

**Availability:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+, watchOS 6.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLUpdateContext](../mlupdatecontext.md)

---

The parameters for the update task.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
var parameters: [MLParameterKey : Any] { get }
```

## See Also

### Getting the update context

- [event](event.md)
  The event type that triggered an update task to notify your app’s completion and update progress handlers.

- [MLUpdateProgressEvent](../mlupdateprogressevent.md)
  A type of event during a model update task.

- [task](task.md)
  The update task that generated the update context.

- [MLParameterKey](../mlparameterkey.md)
  The keys for the parameter dictionary in a model configuration or a model update context.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
