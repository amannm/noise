# init(shape:dataType:strides:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLMultiArray](../mlmultiarray.md)

---

Creates the object with specified strides.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
convenience init(shape: [Int], dataType: MLMultiArrayDataType, strides: [Int])
```

### Parameters

- **`shape`**
  The shape

- **`dataType`**
  The data type

- **`strides`**
  The strides.

## Overview

The contents of the object are left uninitialized; the client must initialize it.

## See Also

### Creating a multiarray

- [init(_:)](init(_:).md)
  An MLMultiArray constructed with the FixedWidthInteger elements of the collection converted to Int32.

- [init(shape:dataType:)](init(shape:datatype:).md)
  Creates a multidimensional array with a shape and type.

- [init(dataPointer:shape:dataType:strides:deallocator:)](init(datapointer:shape:datatype:strides:deallocator:).md)
  Creates a multiarray from a data pointer.

- [init(byConcatenatingMultiArrays:alongAxis:dataType:)](init(byconcatenatingmultiarrays:alongaxis:datatype:).md)
  Merges an array of multiarrays into one multiarray along an axis.

- [init(pixelBuffer:shape:)](init(pixelbuffer:shape:).md)
  Creates a multiarray sharing the surface of a pixel buffer.

- [MLMultiArrayDataType](../mlmultiarraydatatype.md)
  Constants that define the underlying element types a multiarray can store.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
