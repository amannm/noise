# MLComputePlan.Cost

**Structure**

**Framework:** Core ML

**Availability:** iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.0+, watchOS 10.4+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLComputePlan](../mlcomputeplan-1w21n.md)

---

A struct containing information on the estimated cost of executing a layer/operation.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
struct Cost
```

## Topics

### Accessing the weight

- [weight](cost/weight.md)
  The estimated workload of executing the operation over the total model evaluation. The value is between [0.0, 1.0].

## See Also

### Getting the estimated cost

- [estimatedCost(of:)](estimatedcost(of:).md)
  Returns the estimated cost of executing a MLProgram operation.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
