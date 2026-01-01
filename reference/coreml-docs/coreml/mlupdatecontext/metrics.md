# metrics

**Instance Property**

**Framework:** Core ML

**Availability:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+, watchOS 6.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLUpdateContext](../mlupdatecontext.md)

---

The training metrics of the model for the update task, contained in a dictionary.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
var metrics: [MLMetricKey : Any] { get }
```

## Overview

Use the [MLMetricKey](../mlmetrickey.md) to access the values within the dictionary.

## See Also

### Evaluating the update

- [MLMetricKey](../mlmetrickey.md)
  A key for the metrics dictionary in an update context.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
