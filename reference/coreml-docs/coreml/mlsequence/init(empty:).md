# init(empty:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLSequence](../mlsequence.md)

---

Creates an empty sequence of strings or integers.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
convenience init(empty type: MLFeatureType)
```

### Parameters

- **`type`**
  An [MLFeatureType](../mlfeaturetype.md) instance that determines the sequence’s element type, which must be either [MLFeatureType.string](../mlfeaturetype/string.md) or [MLFeatureType.int64](../mlfeaturetype/int64.md).

## See Also

### Creating a sequence

- [init(strings:)](init(strings:).md)
  Creates a sequence of strings from a string array.

- [init(int64s:)](init(int64s:).md)
  Creates a sequence of integers from an array of numbers.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
