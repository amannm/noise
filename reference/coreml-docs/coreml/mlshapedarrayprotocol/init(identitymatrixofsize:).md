# init(identityMatrixOfSize:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLShapedArrayProtocol](../mlshapedarrayprotocol.md)

---

Initialize as an identity matrix.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
init(identityMatrixOfSize size: Int)
```

### Parameters

- **`size`**
  The size (order) of the matrix

## Overview

The initializer creates a shaped array of shape size x size where the contents are zeros except array[scalarAt: x, x], which are ones.

## See Also

### Creating a shaped array type

- [init(scalars:shape:)](init(scalars:shape:).md)
  Creates a shaped array type from an array of values.

- [init(repeating:shape:)](init(repeating:shape:).md)
  Creates a shaped array type that initializes every element to the same value.

- [init(randomScalarsIn:shape:)](init(randomscalarsin:shape:).md)
  Initialize the shaped array with random scalar values.

- [init(bytesNoCopy:shape:deallocator:)](init(bytesnocopy:shape:deallocator:).md)
  Creates a shaped array type from a data pointer.

- [init(bytesNoCopy:shape:strides:deallocator:)](init(bytesnocopy:shape:strides:deallocator:).md)
  Creates a shaped array type from a data pointer with memory strides.

- [init(unsafeUninitializedShape:initializingWith:)](init(unsafeuninitializedshape:initializingwith:).md)
  Creates a shaped array type from a shape and a closure that initializes its memory.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
