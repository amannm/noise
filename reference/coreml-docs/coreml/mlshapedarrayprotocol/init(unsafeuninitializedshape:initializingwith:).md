# init(unsafeUninitializedShape:initializingWith:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLShapedArrayProtocol](../mlshapedarrayprotocol.md)

---

Creates a shaped array type from a shape and a closure that initializes its memory.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
init(unsafeUninitializedShape shape: [Int], initializingWith initializer: (inout UnsafeMutableBufferPointer<Self.Scalar>, [Int]) throws -> Void) rethrows
```

### Parameters

- **`shape`**
  An integer array. Each element represents the size of the shaped array’s corresponding dimension.

- **`initializer`**
  A closure you provide that initializes the shaped array’s underlying memory. The initializer calls your closure with a pointer to the memory and an array of strides that correspond to the shaped array’s dimensions.

## See Also

### Creating a shaped array type

- [init(scalars:shape:)](init(scalars:shape:).md)
  Creates a shaped array type from an array of values.

- [init(repeating:shape:)](init(repeating:shape:).md)
  Creates a shaped array type that initializes every element to the same value.

- [init(identityMatrixOfSize:)](init(identitymatrixofsize:).md)
  Initialize as an identity matrix.

- [init(randomScalarsIn:shape:)](init(randomscalarsin:shape:).md)
  Initialize the shaped array with random scalar values.

- [init(bytesNoCopy:shape:deallocator:)](init(bytesnocopy:shape:deallocator:).md)
  Creates a shaped array type from a data pointer.

- [init(bytesNoCopy:shape:strides:deallocator:)](init(bytesnocopy:shape:strides:deallocator:).md)
  Creates a shaped array type from a data pointer with memory strides.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
