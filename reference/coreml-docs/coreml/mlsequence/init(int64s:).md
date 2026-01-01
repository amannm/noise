# init(int64s:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLSequence](../mlsequence.md)

---

Creates a sequence of integers from an array of numbers.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
convenience init(int64s int64Values: [NSNumber])
```

### Parameters

- **`int64Values`**
  An array of integer values represented as [NSNumber](https://developer.apple.com/documentation/Foundation/NSNumber) instances.

## See Also

### Creating a sequence

- [init(strings:)](init(strings:).md)
  Creates a sequence of strings from a string array.

- [init(empty:)](init(empty:).md)
  Creates an empty sequence of strings or integers.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
