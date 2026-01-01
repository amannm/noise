# estimatedCost(of:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.0+, watchOS 10.4+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLComputePlan](../mlcomputeplan-1w21n.md)

---

Returns the estimated cost of executing a MLProgram operation.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func estimatedCost(of operation: MLModelStructure.Program.Operation) -> MLComputePlan.Cost?
```

### Parameters

- **`operation`**
  A MLProgram operation

## Overview

The estimated cost of executing the operation.

## See Also

### Getting the estimated cost

- [MLComputePlan.Cost](cost.md)
  A struct containing information on the estimated cost of executing a layer/operation.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
