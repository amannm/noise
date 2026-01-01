# init(unsafeUninitializedShape:initializingWith:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLShapedArray](../mlshapedarray.md)

---

Creates a shaped array from a shape and a closure that initializes its memory.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
init(unsafeUninitializedShape shape: [Int], initializingWith initializer: (inout UnsafeMutableBufferPointer<Scalar>, [Int]) throws -> Void) rethrows
```

### Parameters

- **`shape`**
  An integer array. Each element represents the size of the shaped array’s corresponding dimension.

- **`initializer`**
  A closure you provide that initializes the shaped array’s underlying memory. The initializer calls your closure with a pointer to the memory and an array of strides that correspond to the shaped array’s dimensions.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
