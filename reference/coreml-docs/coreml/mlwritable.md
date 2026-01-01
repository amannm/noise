# MLWritable

**Protocol**

**Framework:** Core ML

**Availability:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+, watchOS 6.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

A set of methods that saves a machine learning type to the file system.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
protocol MLWritable : NSObjectProtocol
```

## Overview

You use [MLWritable](mlwritable.md) to save any [MLModel](mlmodel.md) instance that adopts the protocol to the file system.

## Topics

### Saving to a file

- [write(to:)](mlwritable/write(to:).md)
  Exports a machine learning file to the file system.

## See Also

### Saving an updated model

- [model](mlupdatecontext/model.md)
  The underlying Core ML model stored in memory.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
