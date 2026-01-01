# init(pixelBuffer:shape:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLMultiArray](../mlmultiarray.md)

---

Creates a multiarray sharing the surface of a pixel buffer.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
init(pixelBuffer: CVPixelBuffer, shape: [NSNumber])
```

### Parameters

- **`pixelBuffer`**
  The pixel buffer owned by the instance.

- **`shape`**
  The shape of the `MLMultiArray`. The last dimension of `shape` must match the pixel buffer’s width. The product of the rest of the dimensions must match the height.

## Overview

Use this initializer to create an [IOSurface](https://developer.apple.com/documentation/IOSurface)-backed `MLMultiArray` that reduces the inference latency by avoiding the buffer copy to and from some compute units.

The instance will own the pixel buffer and release it on the deallocation.

The pixel buffer’s pixel format type must be [kCVPixelFormatType_OneComponent16Half](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_OneComponent16Half). The `MLMultiArray` data type is [MLMultiArrayDataType.float16](../mlmultiarraydatatype/float16.md).

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

- [init(byConcatenatingMultiArrays:alongAxis:dataType:)](init(byconcatenatingmultiarrays:alongaxis:datatype:).md)
  Merges an array of multiarrays into one multiarray along an axis.

- [MLMultiArrayDataType](../mlmultiarraydatatype.md)
  Constants that define the underlying element types a multiarray can store.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
