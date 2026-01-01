# MLShapedArraySlice

**Structure**

**Framework:** Core ML

**Availability:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

A multidimensional subset of elements from a shaped array type.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
struct MLShapedArraySlice<Scalar> where Scalar : MLShapedArrayScalar
```

## Topics

### Creating a shaped array slice

- [init(scalar:)](mlshapedarrayslice/init(scalar:).md)
  Creates a shaped array slice with exactly one value and zero dimensions.

- [init(scalars:shape:)](mlshapedarrayslice/init(scalars:shape:).md)
  Initialize with a sequence and the shape.

- [init(mutating:shape:)](mlshapedarrayslice/init(mutating:shape:).md)
  Creates a new `MLShapedArraySlice` using a pixel buffer as the backing storage.

### Creating a shaped array slice from another type

- [init(_:)](mlshapedarrayslice/init(_:).md)
  Creates a new MLShapedArraySlice using a `MLMultiArray` as a backing storage.

- [init(concatenating:alongAxis:)](mlshapedarrayslice/init(concatenating:alongaxis:).md)
  Merges a sequence of shaped arrays into one shaped array along an axis.

### Creating a shaped array slice with pointers to memory

- [init(unsafeUninitializedShape:initializingWith:)](mlshapedarrayslice/init(unsafeuninitializedshape:initializingwith:).md)
  Creates a shaped array slice from a shape and a closure that initializes its memory.

### Creating a shaped array slice with data

- [init(data:shape:)](mlshapedarrayslice/init(data:shape:).md)
  Creates a shaped array with a defined data and shape.

- [init(data:shape:strides:)](mlshapedarrayslice/init(data:shape:strides:).md)
  Creates a shaped array with defined data, shape, and strides.

### Shaping the array slice

- [changingLayout(to:)](mlshapedarrayslice/changinglayout(to:).md)
  Returns a copy with the specified buffer layout.

- [expandingShape(at:)](mlshapedarrayslice/expandingshape(at:).md)
  Returns a new shaped array with expanded dimensions

- [reshaped(to:)](mlshapedarrayslice/reshaped(to:).md)
  Returns a new reshaped shaped array.

- [squeezingShape()](mlshapedarrayslice/squeezingshape().md)
  Returns a new squeezed shaped array.

- [transposed()](mlshapedarrayslice/transposed().md)
  Returns a new transposed shaped array

- [transposed(permutation:)](mlshapedarrayslice/transposed(permutation:).md)
  Returns a new transposed shaped array using a custom permutation.

### Modifying a shaped array type

- [withUnsafeMutableShapedBufferPointer(using:_:)](mlshapedarrayslice/withunsafemutableshapedbufferpointer(using:_:).md)
  Calls the given closure with a pointer to the array’s mutable storage that has a specified buffer layout.

### Encoding and decoding an array slice

- [init(from:)](mlshapedarrayslice/init(from:).md)
  Creates an array slice from the passed decoder.

- [encode(to:)](mlshapedarrayslice/encode(to:).md)
  Encodes the array slice.

### Default Implementations

- [Decodable Implementations](mlshapedarrayslice/decodable-implementations.md)

- [Encodable Implementations](mlshapedarrayslice/encodable-implementations.md)

## See Also

### Supporting types

- [Scalar](mlshapedarrayprotocol/scalar-swift.associatedtype.md)
  Represents the underlying scalar type of the shaped array type.

- [MLShapedArrayScalar](mlshapedarrayscalar.md)
  A type that associates a scalar with a shaped array.

- [MLShapedArrayRangeExpression](mlshapedarrayrangeexpression.md)
  An interface for a range expression, which you typically use with subscripts of shaped array types.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
