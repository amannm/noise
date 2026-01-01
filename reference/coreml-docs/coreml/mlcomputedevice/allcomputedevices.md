# allComputeDevices

**Type Property**

**Framework:** Core ML

**Availability:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLComputeDevice](../mlcomputedevice.md)

---

Returns an array that contains all of the compute devices that are accessible.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
static var allComputeDevices: [MLComputeDevice] { get }
```

## Overview

If a compute device becomes inaccessible, this array won’t include it. For example, this array won’t contain the GPU device after it’s removed.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
