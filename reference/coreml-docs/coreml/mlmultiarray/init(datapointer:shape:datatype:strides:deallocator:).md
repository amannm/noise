# init(dataPointer:shape:dataType:strides:deallocator:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLMultiArray](../mlmultiarray.md)

---

Creates a multiarray from a data pointer.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
init(dataPointer: UnsafeMutableRawPointer, shape: [NSNumber], dataType: MLMultiArrayDataType, strides: [NSNumber], deallocator: ((UnsafeMutableRawPointer) -> Void)? = nil) throws
```

### Parameters

- **`dataPointer`**
  A pointer to data in memory.

- **`shape`**
  An integer array with an element for each dimension. An element represents the size of the corresponding dimension.

- **`dataType`**
  An [MLMultiArrayDataType](../mlmultiarraydatatype.md) instance that represents the pointer’s data type.

- **`strides`**
  An integer array with an element for each dimension. An element represents the number of memory locations that span the length of the corresponding dimension.

- **`deallocator`**
  In Swift, a closure the multiarray calls in its deinitializer. In Objective-C, a block the multiarray calls in its [dealloc](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/dealloc) method.

## Overview

The caller is responsible for freeing the memory the `dataPointer` points to, by providing a `deallocator` closure.

## See Also

### Creating a multiarray

- [init(_:)](init(_:).md)
  An MLMultiArray constructed with the FixedWidthInteger elements of the collection converted to Int32.

- [init(shape:dataType:)](init(shape:datatype:).md)
  Creates a multidimensional array with a shape and type.

- [init(shape:dataType:strides:)](init(shape:datatype:strides:).md)
  Creates the object with specified strides.

- [init(byConcatenatingMultiArrays:alongAxis:dataType:)](init(byconcatenatingmultiarrays:alongaxis:datatype:).md)
  Merges an array of multiarrays into one multiarray along an axis.

- [init(pixelBuffer:shape:)](init(pixelbuffer:shape:).md)
  Creates a multiarray sharing the surface of a pixel buffer.

- [MLMultiArrayDataType](../mlmultiarraydatatype.md)
  Constants that define the underlying element types a multiarray can store.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
