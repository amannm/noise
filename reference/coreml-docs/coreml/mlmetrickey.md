# MLMetricKey

**Class**

**Framework:** Core ML

**Availability:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+, watchOS 6.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

A key for the metrics dictionary in an update context.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
class MLMetricKey
```

## Topics

### Getting the keys

- [lossValue](mlmetrickey/lossvalue.md)
  The key you use to access the current loss (a `float` value).

- [epochIndex](mlmetrickey/epochindex.md)
  The key you use to access the epoch index (an `Int64` value).

- [miniBatchIndex](mlmetrickey/minibatchindex.md)
  The key you use to access the mini-batch index (an `Int64` value) within an epoch.

### Supporting types

- [MLKey](mlkey.md)
  An abstract base class for machine learning key types.

## See Also

### Evaluating the update

- [metrics](mlupdatecontext/metrics.md)
  The training metrics of the model for the update task, contained in a dictionary.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
