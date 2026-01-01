# MLShapedArray

**Structure**

**Framework:** Core ML

**Availability:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../coreml.md)

---

A machine learning collection type that stores scalar values in a multidimensional array.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
struct MLShapedArray<Scalar> where Scalar : MLShapedArrayScalar
```

## Overview

A shaped array is a multidimensional array type that’s the Swift counterpart to [MLMultiArray](mlmultiarray.md). [MLShapedArray](mlshapedarray.md) is one of the underlying types of `MLFeatureValue` that stores scalar values. You can convert a shaped array to an [MLMultiArray](mlmultiarray.md) with its [init(_:)](https://developer.apple.com/documentation/coreml/mlmultiarray/init(_:)-wk41) initializer, and convert back to a shaped array with its [init(_:)](mlshapedarray/init(_:).md) initializer. All elements in an [MLShapedArray](mlshapedarray.md) are of the same type, and that type must conform to [MLShapedArrayScalar](mlshapedarrayscalar.md):

- [Int32](https://developer.apple.com/documentation/Swift/Int32)
- [Float](https://developer.apple.com/documentation/Swift/Float)
- [Double](https://developer.apple.com/documentation/Swift/Double)

Each dimension in a shaped array is typically significant or meaningful. For example, a model could have an input that accepts images as a three-dimensional array of pixels, C x H x W. The first dimension, *C*,_ _represents the number of color channels, and the second and third dimensions, *H* and *W*, represent the image’s height and width, respectively. The number of dimensions and size of each dimension define the shaped array’s *shape*.

> **Note**
>  Some models use a one-dimensional multiarray for an input or output. This type of shaped array is conceptually identical to a conventional [Array](https://developer.apple.com/documentation/Swift/Array).

A shaped array’s [shape](mlmultiarray/shape.md) property is an integer array in which each element defines the size of the corresponding dimension. To inspect the shape and constraints of a model’s multiarray input or output feature:

1. Access the model’s [modelDescription](mlmodel/modeldescription.md) property.
2. Find the multiarray input or output feature in the model description’s [inputDescriptionsByName](mlmodeldescription/inputdescriptionsbyname.md) or [outputDescriptionsByName](mlmodeldescription/outputdescriptionsbyname.md) property, respectively.
3. Access the feature description’s [multiArrayConstraint](mlfeaturedescription/multiarrayconstraint.md) property.
4. Inspect the multiarray constraint’s [shape](mlmultiarrayconstraint/shape.md) and [shapeConstraint](mlmultiarrayconstraint/shapeconstraint.md).

## Topics

### Creating a shaped array

- [init(scalar:)](mlshapedarray/init(scalar:).md)
  Creates a shaped array with exactly one value and zero dimensions.

- [init(scalars:shape:)](mlshapedarray/init(scalars:shape:).md)
  Initialize with a sequence and the shape.

- [init(mutating:shape:)](mlshapedarray/init(mutating:shape:).md)
  Creates a new `MLShapedArray` using a pixel buffer as the backing storage.

### Creating a shaped array from another type

- [init(_:)](mlshapedarray/init(_:).md)

- [init(concatenating:alongAxis:)](mlshapedarray/init(concatenating:alongaxis:).md)
  Merges a sequence of shaped arrays into one shaped array along an axis.

### Creating a shaped array with pointers to memory

- [init(unsafeUninitializedShape:initializingWith:)](mlshapedarray/init(unsafeuninitializedshape:initializingwith:).md)
  Creates a shaped array from a shape and a closure that initializes its memory.

### Creating a shaped array from data

- [init(data:shape:)](mlshapedarray/init(data:shape:).md)
  Creates a shaped array from a block of data and a shape.

- [init(data:shape:strides:)](mlshapedarray/init(data:shape:strides:).md)
  Creates a shaped array from a block of data, a shape, and strides.

### Shaping the array

- [changingLayout(to:)](mlshapedarray/changinglayout(to:).md)
  Returns a copy with the specified buffer layout.

- [expandingShape(at:)](mlshapedarray/expandingshape(at:).md)
  Returns a new shaped array with expanded dimensions.

- [reshaped(to:)](mlshapedarray/reshaped(to:).md)
  Returns a new reshaped shaped array.

- [squeezingShape()](mlshapedarray/squeezingshape().md)
  Returns a new squeezed shaped array.

- [transposed()](mlshapedarray/transposed().md)
  Returns a new transposed shaped array.

- [transposed(permutation:)](mlshapedarray/transposed(permutation:).md)
  Returns a transposed shaped array using a custom permutation.

### Reading and writing the pixel buffer

- [withMutablePixelBufferIfAvailable(_:)](mlshapedarray/withmutablepixelbufferifavailable(_:).md)
  Writes to the underlying pixel buffer.

- [withPixelBufferIfAvailable(_:)](mlshapedarray/withpixelbufferifavailable(_:).md)
  Reads the underlying pixel buffer.

### Modifying a shaped array

- [withUnsafeMutableShapedBufferPointer(using:_:)](mlshapedarray/withunsafemutableshapedbufferpointer(using:_:).md)
  Calls the given closure with a pointer to the array’s mutable storage that has a specified buffer layout.

### Encoding and decoding

- [init(from:)](mlshapedarray/init(from:).md)
  Creates a shaped array from a decoder.

- [encode(to:)](mlshapedarray/encode(to:).md)
  Encode a shaped array.

### Default Implementations

- [CustomStringConvertible Implementations](mlshapedarray/customstringconvertible-implementations.md)

- [Decodable Implementations](mlshapedarray/decodable-implementations.md)

- [Encodable Implementations](mlshapedarray/encodable-implementations.md)

## See Also

### Supporting types

- [MLFeatureType](mlfeaturetype.md)
  The possible types for feature values, input features, and output features.

- [MLShapedArrayProtocol](mlshapedarrayprotocol.md)
  An interface that defines a shaped array type.

- [MLMultiArray](mlmultiarray.md)
  A machine learning collection type that stores numeric values in an array with multiple dimensions.

- [MLSequence](mlsequence.md)
  A machine learning collection type that stores a series of strings or integers.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
