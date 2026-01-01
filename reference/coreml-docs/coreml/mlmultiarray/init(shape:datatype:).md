# init(shape:dataType:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLMultiArray](../mlmultiarray.md)

---

Creates a multidimensional array with a shape and type.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
init(shape: [NSNumber], dataType: MLMultiArrayDataType) throws
```

### Parameters

- **`shape`**
  An integer array that has an element for each dimension in a multiarray that represents its length.

- **`dataType`**
  An element type defined by [MLMultiArrayDataType](../mlmultiarraydatatype.md).

## Overview

This method allocates a contiguous region of memory for the multiarray’s shape. You must set the contents of memory. The multiarray frees the memory in its deinitializer (Swift) or [dealloc](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/dealloc) method (Objective-C).

The following code creates a 3 x 3 multiarray and sets its contents to the value 3.14159.

## See Also

### Creating a multiarray

- [init(_:)](init(_:).md)
  An MLMultiArray constructed with the FixedWidthInteger elements of the collection converted to Int32.

- [init(shape:dataType:strides:)](init(shape:datatype:strides:).md)
  Creates the object with specified strides.

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
