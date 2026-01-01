# init(randomUniform:in:seed:scalarType:)

**Initializer**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLTensor](../mltensor.md)

---

Creates a tensor with the specified shape, randomly sampling scalar values from a uniform distribution in `bounds`.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
init<Scalar>(randomUniform shape: [Int], in bounds: ClosedRange<Scalar> = 0...1, seed: UInt64? = nil, scalarType: Scalar.Type = Scalar.self) where Scalar : MLTensorScalar, Scalar : BinaryInteger
```

### Parameters

- **`shape`**
  The shape of the tensor.

- **`bounds`**
  The bounds of the distribution. The default value is `0...1`.

- **`seed`**
  The random seed.

- **`scalarType`**
  The scalar type.

## Overview

> **Note**
> Using the same seed produces the same result only when dispatched to the same compute device.

## See Also

### Creating a tensor

- [init(_:)](init(_:).md)
  Creates a one-dimensional tensor from scalars.

- [init(_:alongAxis:)](init(_:alongaxis:).md)
  Creates a tensor by stacking the given tensors along the specified axis.

- [init(_:scalarType:)](init(_:scalartype:).md)
  Creates a one-dimensional tensor from scalars.

- [init(bytesNoCopy:shape:scalarType:deallocator:)](init(bytesnocopy:shape:scalartype:deallocator:).md)
  Creates a tensor with memory content without copying the bytes.

- [init(concatenating:alongAxis:)](init(concatenating:alongaxis:).md)
  Concatenates `tensors` along the `axis` dimension.

- [init(linearSpaceFrom:through:count:)](init(linearspacefrom:through:count:).md)
  Creates a one-dimensional tensor representing a sequence from a starting value, up to and including an end value, spaced evenly to generate the number of values specified.

- [init(linearSpaceFrom:through:count:scalarType:)](init(linearspacefrom:through:count:scalartype:).md)
  Creates a one-dimensional tensor representing a sequence from a starting value, up to and including an end value, spaced evenly to generate the number of values specified.

- [init(ones:scalarType:)](init(ones:scalartype:).md)
  Creates a tensor with all scalars set to ones.

- [init(randomNormal:mean:standardDeviation:seed:scalarType:)](init(randomnormal:mean:standarddeviation:seed:scalartype:).md)
  Creates a tensor with the specified shape, randomly sampling scalar values from a normal distribution.

- [init(rangeFrom:to:by:)](init(rangefrom:to:by:).md)
  Creates a one-dimensional tensor representing a sequence from a starting value to, but not including, an end value, stepping by the specified amount.

- [init(rangeFrom:to:by:scalarType:)](init(rangefrom:to:by:scalartype:).md)
  Creates a one-dimensional tensor representing a sequence from a starting value to, but not including, an end value, stepping by the specified amount.

- [init(repeating:shape:)](init(repeating:shape:).md)
  Creates a tensor with the specified shape and a single, repeated scalar value.

- [init(repeating:shape:scalarType:)](init(repeating:shape:scalartype:).md)
  Creates a tensor with the specified shape and a single, repeated scalar value.

- [init(shape:data:scalarType:)](init(shape:data:scalartype:).md)
  Creates a tensor by copying the given block of data.

- [init(shape:scalars:)](init(shape:scalars:).md)
  Creates a tensor with the specified shape and contiguous scalars in first-major order.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
