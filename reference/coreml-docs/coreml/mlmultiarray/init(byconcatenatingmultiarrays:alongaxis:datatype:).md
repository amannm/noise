# init(byConcatenatingMultiArrays:alongAxis:dataType:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLMultiArray](../mlmultiarray.md)

---

Merges an array of multiarrays into one multiarray along an axis.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
convenience init(byConcatenatingMultiArrays multiArrays: [MLMultiArray], alongAxis axis: Int, dataType: MLMultiArrayDataType)
```

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
convenience init(concatenating multiArrays: [MLMultiArray], axis: Int, dataType: MLMultiArrayDataType)
```

### Parameters

- **`multiArrays`**
  An [MLMultiArray](../mlmultiarray.md) array.

- **`axis`**
  A zero-based axis number the instances in `multiArray` merge along.

- **`dataType`**
  An [MLMultiArrayDataType](../mlmultiarraydatatype.md) instance that represents the underlying type of all the instances in `multiArrays`.

## Overview

All multiarray instances in `multiArrays` must have:

- The same data type
- The same number of dimensions
- The same size for each corresponding dimension, except for the concatenation axis

For example, this code concatenates two multiarrays along their first dimension:

```swift
let multiarray1 = try MLMultiArray(shape: [1, 5, 7], dataType: .int32)
let multiarray2 = try MLMultiArray(shape: [2, 5, 7], dataType: .int32)

// Merge the two multiarrays along the first dimension.
let multiArray3 = MLMultiArray(concatenating: [multiarray1, multiarray2],
                               axis: 0,
                               dataType: .int32)

assert(multiArray3.shape == [3, 5, 7])
```

## See Also

### Creating a multiarray

- [init(_:)](init(_:).md)
  An MLMultiArray constructed with the FixedWidthInteger elements of the collection converted to Int32.

- [init(shape:dataType:)](init(shape:datatype:).md)
  Creates a multidimensional array with a shape and type.

- [init(shape:dataType:strides:)](init(shape:datatype:strides:).md)
  Creates the object with specified strides.

- [init(dataPointer:shape:dataType:strides:deallocator:)](init(datapointer:shape:datatype:strides:deallocator:).md)
  Creates a multiarray from a data pointer.

- [init(pixelBuffer:shape:)](init(pixelbuffer:shape:).md)
  Creates a multiarray sharing the surface of a pixel buffer.

- [MLMultiArrayDataType](../mlmultiarraydatatype.md)
  Constants that define the underlying element types a multiarray can store.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
