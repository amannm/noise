# epochIndex

**Type Property**

**Framework:** Core ML

**Availability:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+, watchOS 6.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLMetricKey](../mlmetrickey.md)

---

The key you use to access the epoch index (an `Int64` value).

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
class var epochIndex: MLMetricKey { get }
```

## Overview

Use this key to fetch the epoch index value in the [metrics](../mlupdatecontext/metrics.md) dictionary.

## See Also

### Getting the keys

- [lossValue](lossvalue.md)
  The key you use to access the current loss (a `float` value).

- [miniBatchIndex](minibatchindex.md)
  The key you use to access the mini-batch index (an `Int64` value) within an epoch.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
