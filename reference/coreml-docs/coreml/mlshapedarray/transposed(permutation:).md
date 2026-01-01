# transposed(permutation:)

**Instance Method**

**Framework:** Core ML

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+

[Technologies](https://developer.apple.com/documentation/technologies) > [Core ML](../../coreml.md) > [MLShapedArray](../mlshapedarray.md)

---

Returns a transposed shaped array using a custom permutation.

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```objc
func transposed(permutation axes: [Int]) -> MLShapedArray<Scalar>
```

## Overview

Use this method to convert, for example, the image data layout from `[C, H, W]` to `[C, W, H]`, where `C` is channel, `W` is width, and `H` is height.

```swift
// The source tensor has 3 channels, 128 x 64 image in [C, H, W] layout.
let imageCHW = MLShapedArray<Int32>(scalars: pixelValues,
                                    shape: [3, 64, 128])
let imageCWH = imageCHW.transposed(permutation: [0, 2, 1])
imageCHW.shape // [3, 64, 128]
imageCWH.shape // [3, 128, 64]
```

The shape (`shape_out`) is transposed from the input shape (`shape_in`) as follows.

```swift
shape_out[i]
  == permutation.map { shape_in[$0] }
```

The scalar value of the output shaped array (`array_out`) is related to the input shaped array (`array_in`) as follows.

```swift
array_out(scalarAt: permutation.map { indices[$0] })
  == array_in[scalarAt: indices]]
```

## See Also

### Shaping the array

- [changingLayout(to:)](changinglayout(to:).md)
  Returns a copy with the specified buffer layout.

- [expandingShape(at:)](expandingshape(at:).md)
  Returns a new shaped array with expanded dimensions.

- [reshaped(to:)](reshaped(to:).md)
  Returns a new reshaped shaped array.

- [squeezingShape()](squeezingshape().md)
  Returns a new squeezed shaped array.

- [transposed()](transposed().md)
  Returns a new transposed shaped array.

---

*Copyright &copy; 2025 Apple Inc. All rights reserved.*
