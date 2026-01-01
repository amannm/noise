# usesCPUOnly

**Instance Property**

**Framework:** Core ML

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLPredictionOptions](../mlpredictionoptions.md)

---

A Boolean value that indicates whether a prediction is computed using only the CPU.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
var usesCPUOnly: Bool { get set }
```

## Overview

Your model should be restricted to the CPU if it might run in the background or if your app has other GPU intensive tasks.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
