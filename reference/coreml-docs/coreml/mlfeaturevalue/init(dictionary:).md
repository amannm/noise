# init(dictionary:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLFeatureValue](../mlfeaturevalue.md)

---

Creates a feature value that contains a dictionary of numbers.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
convenience init(dictionary value: [AnyHashable : NSNumber]) throws
```

### Parameters

- **`value`**
  A dictionary of numbers.

## See Also

### Creating collection feature values

- [init(sequence:)](init(sequence:).md)
  Creates a feature value that contains a sequence.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
